import os
import sys
import json
from typing import Any, Dict, List, Optional
from datetime import datetime, timedelta, timezone
from urllib.parse import quote, urlparse, unquote
from pathlib import Path

from dotenv import load_dotenv

# Azure Identity + Storage
from azure.identity import AzureCliCredential
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions

# Content Understanding
from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisInput, AnalysisResult

# Cosmos DB
from azure.cosmos import CosmosClient, PartitionKey


# ----------------------------
# Load environment
# ----------------------------
load_dotenv(override=True)

# Storage
AZURE_STORAGE_ACCOUNT_NAME = os.environ["AZURE_STORAGE_ACCOUNT_NAME"]
AZURE_BLOB_CONTAINER = os.environ["AZURE_BLOB_CONTAINER"]

# Content Understanding
AZURE_AI_ENDPOINT = os.environ["AZURE_AI_ENDPOINT"]
ANALYZER_ID = os.environ["ANALYZER_ID"]
API_VERSION = os.environ.get("CU_API_VERSION", "2025-11-01")

# Cosmos
COSMOS_ENDPOINT = os.environ["COSMOS_ENDPOINT"]
COSMOS_KEY = os.environ["COSMOS_KEY"]
COSMOS_DB = os.environ.get("COSMOS_DB", "testDB1")
COSMOS_CONTAINER = os.environ.get("COSMOS_CONTAINER", "CallQuality")

# Container partition key path (matches your CSV loader design)
PARTITION_KEY_PATH = os.environ.get("COSMOS_PARTITION_KEY", "/originalFileName")

# Behavior knobs
LOOKBACK_HOURS = int(os.environ.get("LOOKBACK_HOURS", "24"))
SAS_VALID_MINUTES = int(os.environ.get("SAS_VALID_MINUTES", "60"))

# IMPORTANT:
# - This script does NOT generate/store a "playback SAS" URL.
# - If blobs are private, Content Understanding still needs access to the input URL.
#   Set USE_SAS_FOR_ANALYSIS=1 (default) to generate a short SAS ONLY for analysis input.
#   Set USE_SAS_FOR_ANALYSIS=0 only if your blob URLs are publicly readable.
USE_SAS_FOR_ANALYSIS = os.environ.get("USE_SAS_FOR_ANALYSIS", "1") not in ("0", "false", "False")


# ----------------------------
# Small utilities
# ----------------------------
def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def safe_basename_from_blobname(blob_name: str) -> str:
    # blob_name can contain virtual folders; we want the filename only
    return os.path.basename(blob_name)


def strip_key_frames_from_markdown(markdown: str) -> str:
    # remove the "Key Frames" section if present
    if not markdown:
        return markdown
    marker = "\n\nKey Frames"
    if marker in markdown:
        return markdown.split(marker, 1)[0].rstrip()
    return markdown


def flatten_field_value(field_obj: Any) -> Any:
    """
    Normalize CU field objects to scalar / JSON-friendly values.
    CU often returns: {type:..., valueString/valueNumber/valueArray...}
    """
    if not isinstance(field_obj, dict):
        return field_obj

    ftype = field_obj.get("type")
    if ftype == "string":
        return field_obj.get("valueString")
    if ftype == "number":
        return field_obj.get("valueNumber")
    if ftype == "boolean":
        return field_obj.get("valueBoolean")
    if ftype == "array":
        return field_obj.get("valueArray")
    if ftype == "object":
        return field_obj.get("valueObject")

    # fallback: first key that looks like a value
    for k, v in field_obj.items():
        if isinstance(k, str) and k.startswith("value"):
            return v
    return field_obj


def normalize_cu_payload(wrapper: Dict[str, Any]) -> Dict[str, Any]:
    """
    CU SDK can return:
      - payload directly: { analyzerId, createdAt, contents, ... }
      - or wrapper-like: { id, status, result: {...}, usage: {...} }
    This function returns the "payload" dict that contains `contents`.
    """
    if isinstance(wrapper.get("result"), dict) and "contents" in wrapper["result"]:
        return wrapper["result"]
    return wrapper


# ----------------------------
# Storage enumeration (no playback SAS)
# ----------------------------
def list_recent_mp4_blobs() -> List[Dict[str, Any]]:
    """
    Returns stable references only:
      - blobName (path in container)
      - videoBlobUrl (no SAS)
      - lastModified
    """
    cred = AzureCliCredential()
    account_url = f"https://{AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net"
    service = BlobServiceClient(account_url=account_url, credential=cred)
    container = service.get_container_client(AZURE_BLOB_CONTAINER)

    cutoff = utcnow() - timedelta(hours=LOOKBACK_HOURS)
    items: List[Dict[str, Any]] = []

    for blob in container.list_blobs():
        if not blob.name.lower().endswith(".mp4"):
            continue
        if blob.last_modified < cutoff:
            continue

        encoded = quote(blob.name, safe="/~")
        video_blob_url = f"{account_url}/{AZURE_BLOB_CONTAINER}/{encoded}"

        items.append({
            "blobName": blob.name,
            "videoBlobUrl": video_blob_url,   # stable, no SAS
            "lastModified": blob.last_modified.isoformat() if blob.last_modified else None,
        })

    return items


# ----------------------------
# Analysis URL builder
# ----------------------------
def make_analysis_url_factory() -> Any:
    """
    Returns a function(blobName)->url that CU can access.

    - If USE_SAS_FOR_ANALYSIS: generate short-lived SAS URLs only for analyzer input.
      (Not stored in Cosmos, not returned as playback links.)
    - Else: return the plain blob URL (requires public blob/container access).
    """
    account_url = f"https://{AZURE_STORAGE_ACCOUNT_NAME}.blob.core.windows.net"
    cred = AzureCliCredential()
    service = BlobServiceClient(account_url=account_url, credential=cred)

    if not USE_SAS_FOR_ANALYSIS:
        def _plain(blob_name: str) -> str:
            encoded = quote(blob_name, safe="/~")
            return f"{account_url}/{AZURE_BLOB_CONTAINER}/{encoded}"
        return _plain

    # SAS for analysis input only (short lived). Generation method per Microsoft guidance. 
    start = utcnow() - timedelta(minutes=5)
    expiry = utcnow() + timedelta(minutes=SAS_VALID_MINUTES)
    delegation_key = service.get_user_delegation_key(start, expiry)

    def _sas(blob_name: str) -> str:
        sas = generate_blob_sas(
            account_name=AZURE_STORAGE_ACCOUNT_NAME,
            container_name=AZURE_BLOB_CONTAINER,
            blob_name=blob_name,
            user_delegation_key=delegation_key,
            permission=BlobSasPermissions(read=True),
            expiry=expiry,
            start=start,
        )
        encoded = quote(blob_name, safe="/~")
        return f"{account_url}/{AZURE_BLOB_CONTAINER}/{encoded}?{sas}"

    return _sas


# ----------------------------
# Cosmos connection
# ----------------------------
def get_cosmos_container():
    client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
    db = client.create_database_if_not_exists(id=COSMOS_DB)
    container = db.create_container_if_not_exists(
        id=COSMOS_CONTAINER,
        partition_key=PartitionKey(path=PARTITION_KEY_PATH),
        offer_throughput=400
    )
    return container


# ----------------------------
# Convert CU result -> Cosmos docs (wide, one per contentIndex)
# ----------------------------
def cu_result_to_docs(
    wrapper: Dict[str, Any],
    *,
    original_filename: str,
    blob_name: str,
    video_blob_url: str,
) -> List[Dict[str, Any]]:
    """
    Produces Cosmos-ready documents:
    - Partition key: originalFileName (matches your CSV approach)
    - id: originalFileName_contentIndex (idempotent)
    - Stores stable playback references only (videoBlobUrl + blobName)
    - Stores markdown (Key Frames stripped) + all analyzer fields flattened
    """
    payload = normalize_cu_payload(wrapper)

    # wrapper metadata (if present)
    analysis_id = wrapper.get("id")
    status = wrapper.get("status")
    usage = wrapper.get("usage")

    analyzer_id = payload.get("analyzerId")
    created_at = payload.get("createdAt")
    api_version = payload.get("apiVersion")

    contents = payload.get("contents", []) or []
    docs: List[Dict[str, Any]] = []

    for idx, c in enumerate(contents):
        fields = c.get("fields", {}) or {}
        flat_fields = {k: flatten_field_value(v) for k, v in fields.items()}

        markdown = strip_key_frames_from_markdown(c.get("markdown") or "")

        doc: Dict[str, Any] = {
            # Identity + partition
            "originalFileName": original_filename,
            "contentIndex": idx,
            "id": f"{original_filename}_{idx}",

            # Analysis metadata
            "analysisId": analysis_id,
            "status": status,
            "analyzerId": analyzer_id,
            "apiVersion": api_version,
            "createdAt": created_at,

            # Stable video reference (NO SAS stored)
            "blobName": blob_name,
            "videoBlobUrl": video_blob_url,
            "storageAccount": AZURE_STORAGE_ACCOUNT_NAME,
            "containerName": AZURE_BLOB_CONTAINER,

            # Content metadata
            "kind": c.get("kind"),
            "mimeType": c.get("mimeType"),
            "startTimeMs": c.get("startTimeMs"),
            "endTimeMs": c.get("endTimeMs"),
            "width": c.get("width"),
            "height": c.get("height"),

            # Useful derived counts
            "phraseCount": len(c.get("transcriptPhrases", []) or []),
            "keyFrameCount": len(c.get("KeyFrameTimesMs", []) or []),

            # Text artifacts used in your UI
            "markdown": markdown,
        }

        # Add flattened analyzer fields (wide shape)
        doc.update(flat_fields)

        # Optional: attach usage block for tracking
        if usage is not None:
            doc["usage"] = usage

        docs.append(doc)

    return docs


# ----------------------------
# Main pipeline
# ----------------------------
def main():
    print(f"LOOKBACK_HOURS={LOOKBACK_HOURS}")
    print(f"USE_SAS_FOR_ANALYSIS={USE_SAS_FOR_ANALYSIS} (SAS is NOT stored; only used for analyzer input if enabled)")
    print(f"Cosmos: {COSMOS_DB}/{COSMOS_CONTAINER} PK={PARTITION_KEY_PATH}")

    # 1) enumerate recent videos
    videos = list_recent_mp4_blobs()
    print(f"Found {len(videos)} recent .mp4 blobs")

    if not videos:
        return

    # 2) clients
    cred = AzureCliCredential()
    cu_client = ContentUnderstandingClient(
        endpoint=AZURE_AI_ENDPOINT,
        credential=cred,
        api_version=API_VERSION
    )

    cosmos_container = get_cosmos_container()
    print("Connected to Cosmos DB")

    # 3) analysis url function
    to_analysis_url = make_analysis_url_factory()

    # 4) process end-to-end
    for v in videos:
        blob_name = v["blobName"]
        video_blob_url = v["videoBlobUrl"]
        original_filename = safe_basename_from_blobname(blob_name)

        analysis_url = to_analysis_url(blob_name)

        print(f"\nAnalyzing: {original_filename}")
        print(f"Input URL (analysis): {analysis_url[:120]}{'...' if len(analysis_url) > 120 else ''}")

        poller = cu_client.begin_analyze(
            analyzer_id=ANALYZER_ID,
            inputs=[AnalysisInput(url=analysis_url)],
        )
        result: AnalysisResult = poller.result()
        wrapper = result.as_dict()

        docs = cu_result_to_docs(
            wrapper,
            original_filename=original_filename,
            blob_name=blob_name,
            video_blob_url=video_blob_url,
        )

        for d in docs:
            cosmos_container.upsert_item(d)

        print(f"✅ Upserted {len(docs)} docs for {original_filename}")

    print("\n✅ DONE: Direct-to-Cosmos pipeline complete (no CSV, no playback SAS stored).")


if __name__ == "__main__":
    main()
