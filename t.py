import os
import logging
from datetime import datetime, timedelta, timezone
from urllib.parse import quote

import azure.functions as func
import azure.durable_functions as df

# Azure SDKs
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from azure.ai.contentunderstanding import ContentUnderstandingClient
from azure.ai.contentunderstanding.models import AnalysisInput
from azure.cosmos import CosmosClient

# Initialize the Durable Function App
app = df.DFApp(http_auth_level=func.AuthLevel.FUNCTION)

# ---------------------------------------------------------
# HELPER FUNCTIONS (From your original script)
# ---------------------------------------------------------
def flatten_field_value(field_obj):
    if not isinstance(field_obj, dict):
        return field_obj
    ftype = field_obj.get("type")
    if ftype == "string": return field_obj.get("valueString")
    if ftype == "number": return field_obj.get("valueNumber")
    if ftype == "boolean": return field_obj.get("valueBoolean")
    if ftype == "array": return field_obj.get("valueArray")
    if ftype == "object": return field_obj.get("valueObject")
    for k, v in field_obj.items():
        if isinstance(k, str) and k.startswith("value"):
            return v
    return field_obj

def strip_key_frames_from_markdown(markdown: str) -> str:
    if not markdown: return markdown
    marker = "\n\nKey Frames"
    if marker in markdown:
        return markdown.split(marker, 1)[0].rstrip()
    return markdown

# ---------------------------------------------------------
# 1. STARTER: Triggered when an .mp4 is uploaded
# ---------------------------------------------------------
@app.blob_trigger(arg_name="myblob", path="labhrdocs/{name}", connection="BlobStorageConnection")
@app.durable_client_input(client_name="client")
async def blob_trigger_starter(myblob: func.InputStream, client: df.DurableOrchestrationClient):
    # myblob.name will be "labhrdocs/filename.mp4"
    if not myblob.name.lower().endswith('.mp4'):
        logging.info(f"Ignoring non-mp4 file: {myblob.name}")
        return

    blob_name = myblob.name.split('/', 1)[-1] 
    
    input_data = {
        "blob_name": blob_name,
        "blob_uri": myblob.uri
    }
    
    instance_id = await client.start_new("video_orchestrator", client_input=input_data)
    logging.info(f"Started orchestration with ID = '{instance_id}' for blob '{blob_name}'.")

# ---------------------------------------------------------
# 2. ORCHESTRATOR: Manages the workflow
# ---------------------------------------------------------
@app.orchestration_trigger(context_name="context")
def video_orchestrator(context: df.DurableOrchestrationContext):
    input_data = context.get_input()
    
    # Call the activity to process the video. 
    result = yield context.call_activity("process_video_activity", input_data)
    return result

# ---------------------------------------------------------
# 3. ACTIVITY: The Heavy Lifting
# ---------------------------------------------------------
@app.activity_trigger(input_name="inputData")
def process_video_activity(inputData: dict):
    blob_name = inputData['blob_name']
    video_blob_url = inputData['blob_uri']
    logging.info(f"Activity started for blob: {blob_name}")
    
    # Environment Variables
    storage_account = os.environ["AZURE_STORAGE_ACCOUNT_NAME"]
    container_name = os.environ.get("AZURE_BLOB_CONTAINER", "labhrdocs")
    ai_endpoint = os.environ["AZURE_AI_ENDPOINT"]
    analyzer_id = os.environ["ANALYZER_ID"]
    api_version = os.environ.get("CU_API_VERSION", "2024-12-01-preview")
    
    cosmos_endpoint = os.environ["COSMOS_ENDPOINT"]
    cosmos_db_name = os.environ.get("COSMOS_DB", "testDB1")
    cosmos_container_name = os.environ.get("COSMOS_CONTAINER", "CallQuality")
    
    # Use DefaultAzureCredential (Uses Managed Identity in Cloud, Azure CLI/VS Code locally)
    cred = DefaultAzureCredential()
    
    try:
        # --- A. GENERATE SAS URL FOR AI CONTENT UNDERSTANDING ---
        account_url = f"https://{storage_account}.blob.core.windows.net"
        blob_service = BlobServiceClient(account_url=account_url, credential=cred)
        
        start = datetime.now(timezone.utc) - timedelta(minutes=5)
        expiry = datetime.now(timezone.utc) + timedelta(minutes=60)
        delegation_key = blob_service.get_user_delegation_key(start, expiry)
        
        sas_token = generate_blob_sas(
            account_name=storage_account,
            container_name=container_name,
            blob_name=blob_name,
            user_delegation_key=delegation_key,
            permission=BlobSasPermissions(read=True),
            expiry=expiry,
            start=start,
        )
        sas_url = f"{account_url}/{container_name}/{quote(blob_name, safe='/~')}?{sas_token}"
        logging.info("SAS URL generated.")

        # --- B. PROCESS VIA AI CONTENT UNDERSTANDING ---
        cu_client = ContentUnderstandingClient(endpoint=ai_endpoint, credential=cred, api_version=api_version)
        poller = cu_client.begin_analyze(
            analyzer_id=analyzer_id,
            inputs=[AnalysisInput(url=sas_url)],
        )
        
        logging.info("Waiting for AI Content Understanding to finish processing...")
        result = poller.result() 
        wrapper = result.as_dict()
        logging.info("AI Processing Complete.")

        # --- C. SAVE TO COSMOS DB ---
        cosmos_client = CosmosClient(cosmos_endpoint, credential=cred)
        database = cosmos_client.get_database_client(cosmos_db_name)
        cosmos_container = database.get_container_client(cosmos_container_name)
        
        # Extract payload
        payload = wrapper.get("result", wrapper) if "result" in wrapper else wrapper
        contents = payload.get("contents", [])
        
        docs_upserted = 0
        for idx, c in enumerate(contents):
            fields = c.get("fields", {})
            flat_fields = {k: flatten_field_value(v) for k, v in fields.items()}
            markdown = strip_key_frames_from_markdown(c.get("markdown") or "")

            doc = {
                "id": f"{blob_name}_{idx}",
                "originalFileName": blob_name,
                "contentIndex": idx,
                "analysisId": wrapper.get("id"),
                "status": wrapper.get("status"),
                "analyzerId": payload.get("analyzerId"),
                "createdAt": payload.get("createdAt"),
                "blobName": blob_name,
                "videoBlobUrl": video_blob_url,
                "storageAccount": storage_account,
                "containerName": container_name,
                "markdown": markdown,
            }
            doc.update(flat_fields)
            
            cosmos_container.upsert_item(doc)
            docs_upserted += 1

        logging.info(f"Successfully upserted {docs_upserted} records to Cosmos DB.")
        return f"Success: {blob_name} processed."

    except Exception as e:
        logging.error(f"Error processing {blob_name}: {str(e)}", exc_info=True)
        raise e
