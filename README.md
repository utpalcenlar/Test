2026-06-22T14:21:13   [Verbose]   [HostMonitor] Checking worker statuses (Count=1)
2026-06-22T14:21:13   [Verbose]   [HostMonitor] Worker status: ID=788f0a3b-fad5-4de0-b3dd-9699fa2a79e5, Latency=1ms
2026-06-22T14:21:13   [Verbose]   [HostMonitor] Host process CPU stats (PID 52): History=(0,1,0,0,0), AvgCpuLoad=0.2, MaxCpuLoad=1
2026-06-22T14:21:13   [Verbose]   [HostMonitor] Host process CPU stats (PID 27): History=(2,2,1,2,1), AvgCpuLoad=2, MaxCpuLoad=2
2026-06-22T14:21:13   [Verbose]   [HostMonitor] Host aggregate CPU load 2
2026-06-22T14:21:13   [Information]   Executing StatusCodeResult, setting HTTP status code 200
2026-06-22T14:21:18   [Information]   Request [ebac95e1-46fe-421f-ab8c-d8c6fa4026f6] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1400&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:ebac95e1-46fe-421f-ab8c-d8c6fa4026f6
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Request [0f91dca7-17cf-41aa-bd1f-175ee0deca0f] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs?restype=container&comp=list&marker=&maxresults=10000
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:0f91dca7-17cf-41aa-bd1f-175ee0deca0f
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Response [0f91dca7-17cf-41aa-bd1f-175ee0deca0f] 200 OK (00.0s)
Transfer-Encoding:chunked
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23c884-f01e-0015-5252-0211a4000000
x-ms-client-request-id:0f91dca7-17cf-41aa-bd1f-175ee0deca0f
x-ms-version:2026-02-06
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Type:application/xml

2026-06-22T14:21:18   [Information]   Response [ebac95e1-46fe-421f-ab8c-d8c6fa4026f6] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:5a23a0e5-901e-0000-1352-026bbf000000
x-ms-client-request-id:ebac95e1-46fe-421f-ab8c-d8c6fa4026f6
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Type:application/xml

2026-06-22T14:21:18   [Verbose]   Poll for blobs newer than '2026-06-19T18:22:01.000Z' in container 'labhrdocs' with ClientRequestId '57d65800-4658-4348-a55f-346de9ae397c' found 1 blobs in 5 ms. ContinuationToken: False.
2026-06-22T14:21:18   [Information]   Request [b7234b00-f479-4da8-af84-58122cb6ec0c] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1300&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:b7234b00-f479-4da8-af84-58122cb6ec0c
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Request [ccccf82f-78f0-40dc-a169-59941147fd8d] HEAD https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:ccccf82f-78f0-40dc-a169-59941147fd8d
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Response [ccccf82f-78f0-40dc-a169-59941147fd8d] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Vary:Origin
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23c886-f01e-0015-5352-0211a4000000
x-ms-client-request-id:ccccf82f-78f0-40dc-a169-59941147fd8d
x-ms-version:2026-02-06
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Length:41837686
Content-Type:video/mp4
Content-MD5:FDGtsdzxt+wnqxE3hlFsqg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:18   [Information]   Request [bb7cbb3d-65fa-4016-8798-d7ab65473294] HEAD https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/blobreceipts/funccallmonitoring/Host.Functions.blob_trigger_starter/%220x8DED069863F6A51%22/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:bb7cbb3d-65fa-4016-8798-d7ab65473294
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Warning]   Error response [bb7cbb3d-65fa-4016-8798-d7ab65473294] 404 The specified blob does not exist. (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:b3475b09-301e-0036-5b52-02e6cf000000
x-ms-client-request-id:bb7cbb3d-65fa-4016-8798-d7ab65473294
x-ms-version:2026-02-06
x-ms-error-code:BlobNotFound
Date:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:18   [Information]   Request [b3858cf2-c173-4ed4-b930-edb49a7e4547] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/blobreceipts/funccallmonitoring/Host.Functions.blob_trigger_starter/%220x8DED069863F6A51%22/labhrdocs/bb12.mp4
x-ms-blob-type:BlockBlob
x-ms-meta-Incomplete:REDACTED
If-None-Match:*
x-ms-version:2026-02-06
Accept:application/xml
Content-Length:0
Content-Type:application/octet-stream
x-ms-client-request-id:b3858cf2-c173-4ed4-b930-edb49a7e4547
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Response [b7234b00-f479-4da8-af84-58122cb6ec0c] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:5a23a0ea-901e-0000-1652-026bbf000000
x-ms-client-request-id:b7234b00-f479-4da8-af84-58122cb6ec0c
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Type:application/xml

2026-06-22T14:21:18   [Information]   Response [b3858cf2-c173-4ed4-b930-edb49a7e4547] 201 Created (00.0s)
ETag:"0x8DED0698663FC14"
x-ms-request-id:b3475b18-301e-0036-6552-02e6cf000000
x-ms-client-request-id:b3858cf2-c173-4ed4-b930-edb49a7e4547
x-ms-version:2026-02-06
x-ms-content-crc64:AAAAAAAAAAA=
x-ms-request-server-encrypted:true
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Length:0
Content-MD5:1B2M2Y8AsgTpgAmY7PhCfg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:18   [Information]   Request [57428d10-ac43-4c02-ab67-d9bd241b4f9c] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/blobreceipts/funccallmonitoring/Host.Functions.blob_trigger_starter/%220x8DED069863F6A51%22/labhrdocs/bb12.mp4?comp=lease
x-ms-lease-action:acquire
x-ms-version:2026-02-06
Accept:application/xml
x-ms-lease-duration:30
x-ms-proposed-lease-id:3603b5d1-a528-49cb-b1a7-3ebfc5d586e0
x-ms-client-request-id:57428d10-ac43-4c02-ab67-d9bd241b4f9c
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Response [57428d10-ac43-4c02-ab67-d9bd241b4f9c] 201 Created (00.0s)
ETag:"0x8DED0698663FC14"
x-ms-request-id:b3475b1d-301e-0036-6852-02e6cf000000
x-ms-client-request-id:57428d10-ac43-4c02-ab67-d9bd241b4f9c
x-ms-version:2026-02-06
x-ms-lease-id:3603b5d1-a528-49cb-b1a7-3ebfc5d586e0
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Length:0
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:18   [Information]   Request [236add3c-8dff-4648-b5d2-e2e1a69d9c1d] HEAD https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/blobreceipts/funccallmonitoring/Host.Functions.blob_trigger_starter/%220x8DED069863F6A51%22/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:236add3c-8dff-4648-b5d2-e2e1a69d9c1d
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Response [236add3c-8dff-4648-b5d2-e2e1a69d9c1d] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED0698663FC14"
x-ms-request-id:b3475b22-301e-0036-6d52-02e6cf000000
x-ms-client-request-id:236add3c-8dff-4648-b5d2-e2e1a69d9c1d
x-ms-version:2026-02-06
x-ms-meta-Incomplete:REDACTED
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:locked
x-ms-lease-state:leased
x-ms-lease-duration:fixed
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Length:0
Content-Type:application/octet-stream
Content-MD5:1B2M2Y8AsgTpgAmY7PhCfg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:18   [Information]   Request [dc37061d-07df-4764-9cb7-0a89a188b5c7] POST https://rgd1tsandboxaiapp01846c.queue.core.windows.net/azure-webjobs-blobtrigger-funccallmonitoring/messages
x-ms-version:2025-11-05
Accept:application/xml
Content-Type:application/xml
x-ms-client-request-id:dc37061d-07df-4764-9cb7-0a89a188b5c7
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:18   [Information]   Response [dc37061d-07df-4764-9cb7-0a89a188b5c7] 201 Created (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:97a8c2a2-a003-00d0-0452-0256e9000000
x-ms-client-request-id:dc37061d-07df-4764-9cb7-0a89a188b5c7
x-ms-version:2025-11-05
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Type:application/xml

2026-06-22T14:21:18   [Information]   Request [8745a9c6-4d36-4087-a923-8911bfb4ae68] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/azure-webjobs-blobtrigger-funccallmonitoring/messages?numofmessages=9&visibilitytimeout=600
x-ms-version:2025-11-05
Accept:application/xml
x-ms-client-request-id:8745a9c6-4d36-4087-a923-8911bfb4ae68
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:18   [Verbose]   Blob 'bb12.mp4' is ready for processing by function 'blob_trigger_starter'. A message with id '80a5d654-5a2c-4875-9a56-f55e8344c71a' has been added to queue 'azure-webjobs-blobtrigger-funccallmonitoring'. This message will be dequeued and processed by the BlobTrigger. PollId: '57d65800-4658-4348-a55f-346de9ae397c'. Source: 'ContainerScan'.
2026-06-22T14:21:18   [Information]   Request [4ff3d284-d5b1-4dc6-9988-306631406952] HEAD https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/blobreceipts/funccallmonitoring/Host.Functions.blob_trigger_starter/%220x8DED069863F6A51%22/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:4ff3d284-d5b1-4dc6-9988-306631406952
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Response [4ff3d284-d5b1-4dc6-9988-306631406952] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED0698663FC14"
x-ms-request-id:b3475b2b-301e-0036-7552-02e6cf000000
x-ms-client-request-id:4ff3d284-d5b1-4dc6-9988-306631406952
x-ms-version:2026-02-06
x-ms-meta-Incomplete:REDACTED
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:locked
x-ms-lease-state:leased
x-ms-lease-duration:fixed
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Length:0
Content-Type:application/octet-stream
Content-MD5:1B2M2Y8AsgTpgAmY7PhCfg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:18   [Information]   Response [8745a9c6-4d36-4087-a923-8911bfb4ae68] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c2a7-a003-00d0-0752-0256e9000000
x-ms-client-request-id:8745a9c6-4d36-4087-a923-8911bfb4ae68
x-ms-version:2025-11-05
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Type:application/xml

2026-06-22T14:21:18   [Verbose]   Poll for function 'blob_trigger_starter' on queue 'azure-webjobs-blobtrigger-funccallmonitoring' with ClientRequestId '8745a9c6-4d36-4087-a923-8911bfb4ae68' found 1 messages in 4 ms.
2026-06-22T14:21:18   [Information]   Request [842277e4-1c1a-4095-b68a-bce316de3d3a] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/blobreceipts/funccallmonitoring/Host.Functions.blob_trigger_starter/%220x8DED069863F6A51%22/labhrdocs/bb12.mp4?comp=metadata
x-ms-lease-id:3603b5d1-a528-49cb-b1a7-3ebfc5d586e0
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:842277e4-1c1a-4095-b68a-bce316de3d3a
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Request [162b7f54-1868-4af8-b5c7-68c8d4d41a8d] HEAD https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:162b7f54-1868-4af8-b5c7-68c8d4d41a8d
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Request [38eff262-f929-4779-a1ff-8b32799ff313] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/azure-webjobs-blobtrigger-funccallmonitoring/messages?numofmessages=9&visibilitytimeout=600
x-ms-version:2025-11-05
Accept:application/xml
x-ms-client-request-id:38eff262-f929-4779-a1ff-8b32799ff313
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:18   [Information]   Response [162b7f54-1868-4af8-b5c7-68c8d4d41a8d] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Vary:Origin
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23c899-f01e-0015-6552-0211a4000000
x-ms-client-request-id:162b7f54-1868-4af8-b5c7-68c8d4d41a8d
x-ms-version:2026-02-06
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Length:41837686
Content-Type:video/mp4
Content-MD5:FDGtsdzxt+wnqxE3hlFsqg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:18   [Information]   Response [38eff262-f929-4779-a1ff-8b32799ff313] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c2a9-a003-00d0-0952-0256e9000000
x-ms-client-request-id:38eff262-f929-4779-a1ff-8b32799ff313
x-ms-version:2025-11-05
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Type:application/xml

2026-06-22T14:21:18   [Information]   Request [ab77c4ed-39e6-4617-a223-dd23de244048] HEAD https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:ab77c4ed-39e6-4617-a223-dd23de244048
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Verbose]   Poll for function 'blob_trigger_starter' on queue 'azure-webjobs-blobtrigger-funccallmonitoring' with ClientRequestId '38eff262-f929-4779-a1ff-8b32799ff313' found 0 messages in 3 ms.
2026-06-22T14:21:18   [Verbose]   Function 'blob_trigger_starter' will wait 100 ms before polling queue 'azure-webjobs-blobtrigger-funccallmonitoring'.
2026-06-22T14:21:18   [Information]   Response [842277e4-1c1a-4095-b68a-bce316de3d3a] 200 OK (00.0s)
ETag:"0x8DED06986690316"
x-ms-request-id:b3475b2c-301e-0036-7652-02e6cf000000
x-ms-client-request-id:842277e4-1c1a-4095-b68a-bce316de3d3a
x-ms-version:2026-02-06
x-ms-request-server-encrypted:true
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Length:0
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:18   [Information]   Request [d9c43b62-9330-44d8-9efe-b9d836068ceb] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/blobreceipts/funccallmonitoring/Host.Functions.blob_trigger_starter/%220x8DED069863F6A51%22/labhrdocs/bb12.mp4?comp=lease
x-ms-lease-action:release
x-ms-lease-id:3603b5d1-a528-49cb-b1a7-3ebfc5d586e0
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:d9c43b62-9330-44d8-9efe-b9d836068ceb
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Response [ab77c4ed-39e6-4617-a223-dd23de244048] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Vary:Origin
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23c89c-f01e-0015-6852-0211a4000000
x-ms-client-request-id:ab77c4ed-39e6-4617-a223-dd23de244048
x-ms-version:2026-02-06
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Length:41837686
Content-Type:video/mp4
Content-MD5:FDGtsdzxt+wnqxE3hlFsqg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:18   [Information]   Response [d9c43b62-9330-44d8-9efe-b9d836068ceb] 200 OK (00.0s)
ETag:"0x8DED06986690316"
x-ms-request-id:b3475b35-301e-0036-7e52-02e6cf000000
x-ms-client-request-id:d9c43b62-9330-44d8-9efe-b9d836068ceb
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Length:0
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:18   [Information]   Request [2c413c9b-5892-46ce-9c2d-084644155657] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/blobscaninfo/funccallmonitoring/aiinnovationstoragedev/labhrdocs/scanInfo
x-ms-blob-type:BlockBlob
x-ms-version:2026-02-06
Accept:application/xml
Content-Length:41
Content-Type:application/octet-stream
x-ms-client-request-id:2c413c9b-5892-46ce-9c2d-084644155657
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Request [bcbccbaf-a3ba-4f63-9600-9fe61503a7f6] HEAD https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:bcbccbaf-a3ba-4f63-9600-9fe61503a7f6
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Response [2c413c9b-5892-46ce-9c2d-084644155657] 201 Created (00.0s)
ETag:"0x8DED069866AD717"
x-ms-request-id:b3475b3c-301e-0036-0552-02e6cf000000
x-ms-client-request-id:2c413c9b-5892-46ce-9c2d-084644155657
x-ms-version:2026-02-06
x-ms-content-crc64:e6hMe6ZMc2w=
x-ms-request-server-encrypted:true
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Length:0
Content-MD5:hDLBABMOP1DKnh0e4xqDFw==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:18   [Information]   Response [bcbccbaf-a3ba-4f63-9600-9fe61503a7f6] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Vary:Origin
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23c89d-f01e-0015-6952-0211a4000000
x-ms-client-request-id:bcbccbaf-a3ba-4f63-9600-9fe61503a7f6
x-ms-version:2026-02-06
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Length:41837686
Content-Type:video/mp4
Content-MD5:FDGtsdzxt+wnqxE3hlFsqg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:18   [Information]   Request [1294664e-569d-4f04-bed4-ba3a5e50da69] HEAD https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:1294664e-569d-4f04-bed4-ba3a5e50da69
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Response [1294664e-569d-4f04-bed4-ba3a5e50da69] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Vary:Origin
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23c89f-f01e-0015-6b52-0211a4000000
x-ms-client-request-id:1294664e-569d-4f04-bed4-ba3a5e50da69
x-ms-version:2026-02-06
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Length:41837686
Content-Type:video/mp4
Content-MD5:FDGtsdzxt+wnqxE3hlFsqg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:18   [Information]   Request [5ccc3058-6fa2-4b77-99be-55c1dba865f7] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-range:bytes=0-4194303
If-Match:"0x8DED069863F6A51"
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:5ccc3058-6fa2-4b77-99be-55c1dba865f7
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Request [3205ba2a-bbc9-45e8-8f25-c227080edb7e] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/azure-webjobs-blobtrigger-funccallmonitoring/messages?numofmessages=9&visibilitytimeout=600
x-ms-version:2025-11-05
Accept:application/xml
x-ms-client-request-id:3205ba2a-bbc9-45e8-8f25-c227080edb7e
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:17 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:18   [Information]   Response [3205ba2a-bbc9-45e8-8f25-c227080edb7e] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c2bc-a003-00d0-1c52-0256e9000000
x-ms-client-request-id:3205ba2a-bbc9-45e8-8f25-c227080edb7e
x-ms-version:2025-11-05
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Type:application/xml

2026-06-22T14:21:18   [Verbose]   Poll for function 'blob_trigger_starter' on queue 'azure-webjobs-blobtrigger-funccallmonitoring' with ClientRequestId '3205ba2a-bbc9-45e8-8f25-c227080edb7e' found 0 messages in 5 ms.
2026-06-22T14:21:18   [Verbose]   Function 'blob_trigger_starter' will wait 183.078 ms before polling queue 'azure-webjobs-blobtrigger-funccallmonitoring'.
2026-06-22T14:21:18   [Information]   Response [5ccc3058-6fa2-4b77-99be-55c1dba865f7] 206 Partial Content (00.1s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23c8a2-f01e-0015-6e52-0211a4000000
x-ms-client-request-id:5ccc3058-6fa2-4b77-99be-55c1dba865f7
x-ms-version:2026-02-06
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-blob-content-md5:FDGtsdzxt+wnqxE3hlFsqg==
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Length:4194304
Content-Type:video/mp4
Content-Range:bytes 0-4194303/41837686
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:18   [Information]   Request [09fb454c-115d-41f8-993d-ee1e978d76f3] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-range:bytes=4194304-8388607
If-Match:"0x8DED069863F6A51"
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:09fb454c-115d-41f8-993d-ee1e978d76f3
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Request [bf005a44-3636-446f-a83e-d89b17bff400] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/locks/funccallmonitoring/host?comp=lease
x-ms-lease-action:renew
x-ms-lease-id:aa0b511e-7a56-1cdd-e9d7-33f1b19d7952
x-ms-version:2024-11-04
Accept:application/xml
x-ms-client-request-id:bf005a44-3636-446f-a83e-d89b17bff400
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.22.1 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Response [bf005a44-3636-446f-a83e-d89b17bff400] 200 OK (00.0s)
ETag:"0x8DECE2D7D1660EE"
x-ms-request-id:665a03c2-c01e-00d6-1852-026556000000
x-ms-client-request-id:bf005a44-3636-446f-a83e-d89b17bff400
x-ms-version:2024-11-04
x-ms-lease-id:aa0b511e-7a56-1cdd-e9d7-33f1b19d7952
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Length:0
Last-Modified:Fri, 19 Jun 2026 18:06:30 GMT

2026-06-22T14:21:18   [Information]   Response [09fb454c-115d-41f8-993d-ee1e978d76f3] 206 Partial Content (00.1s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23c8cf-f01e-0015-1852-0211a4000000
x-ms-client-request-id:09fb454c-115d-41f8-993d-ee1e978d76f3
x-ms-version:2026-02-06
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-blob-content-md5:FDGtsdzxt+wnqxE3hlFsqg==
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Length:4194304
Content-Type:video/mp4
Content-Range:bytes 4194304-8388607/41837686
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:18   [Information]   Request [0d91727b-dbb7-41b3-82de-497af72cfbf4] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-range:bytes=8388608-12582911
If-Match:"0x8DED069863F6A51"
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:0d91727b-dbb7-41b3-82de-497af72cfbf4
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Request [e94a400b-068a-4bcf-aeba-0840a0cdb424] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/azure-webjobs-blobtrigger-funccallmonitoring/messages?numofmessages=9&visibilitytimeout=600
x-ms-version:2025-11-05
Accept:application/xml
x-ms-client-request-id:e94a400b-068a-4bcf-aeba-0840a0cdb424
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:18   [Information]   Response [e94a400b-068a-4bcf-aeba-0840a0cdb424] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c2f0-a003-00d0-4f52-0256e9000000
x-ms-client-request-id:e94a400b-068a-4bcf-aeba-0840a0cdb424
x-ms-version:2025-11-05
Date:Mon, 22 Jun 2026 14:21:17 GMT
Content-Type:application/xml

2026-06-22T14:21:18   [Verbose]   Poll for function 'blob_trigger_starter' on queue 'azure-webjobs-blobtrigger-funccallmonitoring' with ClientRequestId 'e94a400b-068a-4bcf-aeba-0840a0cdb424' found 0 messages in 4 ms.
2026-06-22T14:21:18   [Verbose]   Function 'blob_trigger_starter' will wait 280.1255 ms before polling queue 'azure-webjobs-blobtrigger-funccallmonitoring'.
2026-06-22T14:21:18   [Information]   Response [0d91727b-dbb7-41b3-82de-497af72cfbf4] 206 Partial Content (00.1s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23c8e9-f01e-0015-3052-0211a4000000
x-ms-client-request-id:0d91727b-dbb7-41b3-82de-497af72cfbf4
x-ms-version:2026-02-06
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-blob-content-md5:FDGtsdzxt+wnqxE3hlFsqg==
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:21:18 GMT
Content-Length:4194304
Content-Type:video/mp4
Content-Range:bytes 8388608-12582911/41837686
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:18   [Information]   Request [191e91fc-0492-4585-a17c-dcf2e33b1530] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-range:bytes=12582912-16777215
If-Match:"0x8DED069863F6A51"
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:191e91fc-0492-4585-a17c-dcf2e33b1530
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Response [191e91fc-0492-4585-a17c-dcf2e33b1530] 206 Partial Content (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23c908-f01e-0015-4e52-0211a4000000
x-ms-client-request-id:191e91fc-0492-4585-a17c-dcf2e33b1530
x-ms-version:2026-02-06
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-blob-content-md5:FDGtsdzxt+wnqxE3hlFsqg==
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:21:18 GMT
Content-Length:4194304
Content-Type:video/mp4
Content-Range:bytes 12582912-16777215/41837686
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:18   [Information]   Request [f8faac64-5d70-43fb-b1db-0fe349589db8] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-range:bytes=16777216-20971519
If-Match:"0x8DED069863F6A51"
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:f8faac64-5d70-43fb-b1db-0fe349589db8
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Response [f8faac64-5d70-43fb-b1db-0fe349589db8] 206 Partial Content (00.1s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23c927-f01e-0015-6c52-0211a4000000
x-ms-client-request-id:f8faac64-5d70-43fb-b1db-0fe349589db8
x-ms-version:2026-02-06
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-blob-content-md5:FDGtsdzxt+wnqxE3hlFsqg==
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:21:18 GMT
Content-Length:4194304
Content-Type:video/mp4
Content-Range:bytes 16777216-20971519/41837686
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:18   [Information]   Request [5f26978d-0e1f-43ab-bfb6-c37c23dc47d3] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/azure-webjobs-blobtrigger-funccallmonitoring/messages?numofmessages=9&visibilitytimeout=600
x-ms-version:2025-11-05
Accept:application/xml
x-ms-client-request-id:5f26978d-0e1f-43ab-bfb6-c37c23dc47d3
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:18   [Information]   Request [dee3624c-5732-4ce3-b1d7-254ac2f71290] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-range:bytes=20971520-25165823
If-Match:"0x8DED069863F6A51"
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:dee3624c-5732-4ce3-b1d7-254ac2f71290
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:18   [Information]   Response [5f26978d-0e1f-43ab-bfb6-c37c23dc47d3] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c33a-a003-00d0-1252-0256e9000000
x-ms-client-request-id:5f26978d-0e1f-43ab-bfb6-c37c23dc47d3
x-ms-version:2025-11-05
Date:Mon, 22 Jun 2026 14:21:18 GMT
Content-Type:application/xml

2026-06-22T14:21:18   [Verbose]   Poll for function 'blob_trigger_starter' on queue 'azure-webjobs-blobtrigger-funccallmonitoring' with ClientRequestId '5f26978d-0e1f-43ab-bfb6-c37c23dc47d3' found 0 messages in 10 ms.
2026-06-22T14:21:18   [Verbose]   Function 'blob_trigger_starter' will wait 438.4822 ms before polling queue 'azure-webjobs-blobtrigger-funccallmonitoring'.
2026-06-22T14:21:18   [Information]   Response [dee3624c-5732-4ce3-b1d7-254ac2f71290] 206 Partial Content (00.1s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23c94f-f01e-0015-1152-0211a4000000
x-ms-client-request-id:dee3624c-5732-4ce3-b1d7-254ac2f71290
x-ms-version:2026-02-06
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-blob-content-md5:FDGtsdzxt+wnqxE3hlFsqg==
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:21:18 GMT
Content-Length:4194304
Content-Type:video/mp4
Content-Range:bytes 20971520-25165823/41837686
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:19   [Information]   Request [0a9b5d8e-a14c-46dd-8b02-d63b8d0de435] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-range:bytes=25165824-29360127
If-Match:"0x8DED069863F6A51"
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:0a9b5d8e-a14c-46dd-8b02-d63b8d0de435
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:19   [Information]   Response [0a9b5d8e-a14c-46dd-8b02-d63b8d0de435] 206 Partial Content (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23c976-f01e-0015-3052-0211a4000000
x-ms-client-request-id:0a9b5d8e-a14c-46dd-8b02-d63b8d0de435
x-ms-version:2026-02-06
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-blob-content-md5:FDGtsdzxt+wnqxE3hlFsqg==
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:21:18 GMT
Content-Length:4194304
Content-Type:video/mp4
Content-Range:bytes 25165824-29360127/41837686
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:19   [Information]   Request [6d966ade-77cc-4d93-bd50-e64ec7c5dd93] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-range:bytes=29360128-33554431
If-Match:"0x8DED069863F6A51"
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:6d966ade-77cc-4d93-bd50-e64ec7c5dd93
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:19   [Information]   Response [6d966ade-77cc-4d93-bd50-e64ec7c5dd93] 206 Partial Content (00.1s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23c981-f01e-0015-3b52-0211a4000000
x-ms-client-request-id:6d966ade-77cc-4d93-bd50-e64ec7c5dd93
x-ms-version:2026-02-06
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-blob-content-md5:FDGtsdzxt+wnqxE3hlFsqg==
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:21:18 GMT
Content-Length:4194304
Content-Type:video/mp4
Content-Range:bytes 29360128-33554431/41837686
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:19   [Information]   Request [872e7939-81a1-42c4-ba52-7978d6ed5d61] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-range:bytes=33554432-37748735
If-Match:"0x8DED069863F6A51"
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:872e7939-81a1-42c4-ba52-7978d6ed5d61
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:19   [Information]   Response [872e7939-81a1-42c4-ba52-7978d6ed5d61] 206 Partial Content (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23c9b3-f01e-0015-6952-0211a4000000
x-ms-client-request-id:872e7939-81a1-42c4-ba52-7978d6ed5d61
x-ms-version:2026-02-06
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-blob-content-md5:FDGtsdzxt+wnqxE3hlFsqg==
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:21:18 GMT
Content-Length:4194304
Content-Type:video/mp4
Content-Range:bytes 33554432-37748735/41837686
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:19   [Information]   Request [adc3f227-cb73-4a80-bf49-8cf81fb3c0d7] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-range:bytes=37748736-41943039
If-Match:"0x8DED069863F6A51"
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:adc3f227-cb73-4a80-bf49-8cf81fb3c0d7
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:19   [Information]   Response [adc3f227-cb73-4a80-bf49-8cf81fb3c0d7] 206 Partial Content (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23c9c9-f01e-0015-7c52-0211a4000000
x-ms-client-request-id:adc3f227-cb73-4a80-bf49-8cf81fb3c0d7
x-ms-version:2026-02-06
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-blob-content-md5:FDGtsdzxt+wnqxE3hlFsqg==
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:21:18 GMT
Content-Length:4088950
Content-Type:video/mp4
Content-Range:bytes 37748736-41837685/41837686
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:19   [Verbose]   funccallmonitoring-applease: Starting app lease renewal with token 3320c211-0000-0000-0000-000000000000
2026-06-22T14:21:19   [Information]   Request [1e4af88e-0f73-45f9-afaf-0ea72a566562] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/funccallmonitoring-applease?comp=lease&restype=container
x-ms-lease-action:renew
x-ms-lease-id:3320c211-0000-0000-0000-000000000000
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:1e4af88e-0f73-45f9-afaf-0ea72a566562
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:19   [Information]   Response [1e4af88e-0f73-45f9-afaf-0ea72a566562] 200 OK (00.0s)
ETag:"0x8DECE10DD3DE605"
x-ms-request-id:b3475d57-301e-0036-4352-02e6cf000000
x-ms-client-request-id:1e4af88e-0f73-45f9-afaf-0ea72a566562
x-ms-version:2026-02-06
x-ms-lease-id:3320c211-0000-0000-0000-000000000000
Date:Mon, 22 Jun 2026 14:21:18 GMT
Content-Length:0
Last-Modified:Fri, 19 Jun 2026 14:41:35 GMT

2026-06-22T14:21:19   [Verbose]   funccallmonitoring-applease: app lease renewal with token 3320c211-0000-0000-0000-000000000000 succeeded
2026-06-22T14:21:19   [Information]   Request [a9ce13cc-8abe-4882-b389-7f0be431b081] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/azure-webjobs-blobtrigger-funccallmonitoring/messages?numofmessages=9&visibilitytimeout=600
x-ms-version:2025-11-05
Accept:application/xml
x-ms-client-request-id:a9ce13cc-8abe-4882-b389-7f0be431b081
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:19   [Information]   Response [a9ce13cc-8abe-4882-b389-7f0be431b081] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c39c-a003-00d0-6d52-0256e9000000
x-ms-client-request-id:a9ce13cc-8abe-4882-b389-7f0be431b081
x-ms-version:2025-11-05
Date:Mon, 22 Jun 2026 14:21:18 GMT
Content-Type:application/xml

2026-06-22T14:21:19   [Verbose]   Poll for function 'blob_trigger_starter' on queue 'azure-webjobs-blobtrigger-funccallmonitoring' with ClientRequestId 'a9ce13cc-8abe-4882-b389-7f0be431b081' found 0 messages in 4 ms.
2026-06-22T14:21:19   [Verbose]   Function 'blob_trigger_starter' will wait 1014.8909 ms before polling queue 'azure-webjobs-blobtrigger-funccallmonitoring'.
2026-06-22T14:21:19   [Information]   Executing 'Functions.blob_trigger_starter' (Reason='New blob detected(LogsAndContainerScan): labhrdocs/bb12.mp4', Id=7ff72bb9-c35e-4240-888c-65b4cefd6817)
2026-06-22T14:21:19   [Information]   Trigger Details: MessageId: 80a5d654-5a2c-4875-9a56-f55e8344c71a, DequeueCount: 1, InsertedOn: 2026-06-22T14:21:17.000+00:00, BlobCreated: 2026-06-22T14:21:17.000+00:00, BlobLastModified: 2026-06-22T14:21:17.000+00:00
2026-06-22T14:21:19   [Verbose]   Sending invocation id: '7ff72bb9-c35e-4240-888c-65b4cefd6817
2026-06-22T14:21:19   [Verbose]   Posting invocation id:7ff72bb9-c35e-4240-888c-65b4cefd6817 on workerId:788f0a3b-fad5-4de0-b3dd-9699fa2a79e5
2026-06-22T14:21:19   [Information]   Request [0cfd0a28-c629-4eeb-8f58-187eef973201] GET https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions()?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
Accept:application/json;odata=minimalmetadata
x-ms-client-request-id:0cfd0a28-c629-4eeb-8f58-187eef973201
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:19   [Information]   Response [0cfd0a28-c629-4eeb-8f58-187eef973201] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:16a685a0-0002-00bb-1f52-02d11d000000
x-ms-client-request-id:0cfd0a28-c629-4eeb-8f58-187eef973201
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/json;odata=minimalmetadata;streaming=true;charset=utf-8

2026-06-22T14:21:19   [Information]   Request [9a3dd408-0332-4a8a-b80d-4c104f7dfd36] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-00')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A09.2653382Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:9a3dd408-0332-4a8a-b80d-4c104f7dfd36
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:19   [Information]   Response [9a3dd408-0332-4a8a-b80d-4c104f7dfd36] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A19.3092449Z'"
x-ms-request-id:16a685a1-0002-00bb-2052-02d11d000000
x-ms-client-request-id:9a3dd408-0332-4a8a-b80d-4c104f7dfd36
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Length:0

2026-06-22T14:21:19   [Verbose]   funccallmonitoring-control-00:  lease renewal with token  succeeded
2026-06-22T14:21:19   [Information]   Request [dee3f45c-15c7-4fe8-a8d6-1cc97ef6c651] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-01')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A09.2733256Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:dee3f45c-15c7-4fe8-a8d6-1cc97ef6c651
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:19   [Information]   Response [dee3f45c-15c7-4fe8-a8d6-1cc97ef6c651] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A19.3162337Z'"
x-ms-request-id:16a685a2-0002-00bb-2152-02d11d000000
x-ms-client-request-id:dee3f45c-15c7-4fe8-a8d6-1cc97ef6c651
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Length:0

2026-06-22T14:21:19   [Verbose]   funccallmonitoring-control-01:  lease renewal with token  succeeded
2026-06-22T14:21:19   [Information]   Request [93f8537d-ce9f-45bc-9c43-9a4909aa295e] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-02')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A09.281313Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:93f8537d-ce9f-45bc-9c43-9a4909aa295e
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:19   [Information]   Response [93f8537d-ce9f-45bc-9c43-9a4909aa295e] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A19.3222244Z'"
x-ms-request-id:16a685a3-0002-00bb-2252-02d11d000000
x-ms-client-request-id:93f8537d-ce9f-45bc-9c43-9a4909aa295e
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Length:0

2026-06-22T14:21:19   [Verbose]   funccallmonitoring-control-02:  lease renewal with token  succeeded
2026-06-22T14:21:19   [Information]   Request [a652bb42-4fbe-4303-a850-ccb859ae88e2] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-03')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A09.2883012Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:a652bb42-4fbe-4303-a850-ccb859ae88e2
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:19   [Information]   Response [a652bb42-4fbe-4303-a850-ccb859ae88e2] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A19.328215Z'"
x-ms-request-id:16a685a4-0002-00bb-2352-02d11d000000
x-ms-client-request-id:a652bb42-4fbe-4303-a850-ccb859ae88e2
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Length:0

2026-06-22T14:21:19   [Verbose]   funccallmonitoring-control-03:  lease renewal with token  succeeded
2026-06-22T14:21:20   [Warning]   🚨 1. TRIGGER FIRED! Azure detected a file: labhrdocs/bb12.mp4
2026-06-22T14:21:20   [Warning]   🚨 3. FILE ACCEPTED: bb12.mp4. Attempting to start Orchestrator...
2026-06-22T14:21:20   [Information]   Request [586978b4-c4c7-4cd3-b4ae-bb3bdb6c51c4] GET https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringInstances()?$format=REDACTED&$top=REDACTED&$select=REDACTED&$filter=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
Accept:application/json;odata=minimalmetadata
x-ms-client-request-id:586978b4-c4c7-4cd3-b4ae-bb3bdb6c51c4
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:20   [Information]   Response [586978b4-c4c7-4cd3-b4ae-bb3bdb6c51c4] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:16a685ab-0002-00bb-2752-02d11d000000
x-ms-client-request-id:586978b4-c4c7-4cd3-b4ae-bb3bdb6c51c4
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/json;odata=minimalmetadata;streaming=true;charset=utf-8

2026-06-22T14:21:20   [Information]   Fetched instance status for 8b392e4fc0a5491482f3f3b72693b801
2026-06-22T14:21:20   [Information]   Sending [ExecutionStarted] message to funccallmonitoring-control-03 for instance '8b392e4fc0a5491482f3f3b72693b801'
2026-06-22T14:21:20   [Information]   Request [a43b9348-3e0e-45af-9188-ba82264bb7f1] POST https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?messagettl=-1
x-ms-version:2025-05-05
Accept:application/xml
Content-Type:application/xml
x-ms-client-request-id:a43b9348-3e0e-45af-9188-ba82264bb7f1
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:19 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:20   [Information]   Response [a43b9348-3e0e-45af-9188-ba82264bb7f1] 201 Created (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:97a8c43d-a003-00d0-0352-0256e9000000
x-ms-client-request-id:a43b9348-3e0e-45af-9188-ba82264bb7f1
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/xml

2026-06-22T14:21:20   [Information]   Request [7c2d5c94-bf05-4df9-a4e1-b361654854c9] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:7c2d5c94-bf05-4df9-a4e1-b361654854c9
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:19 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:20   [Information]   Request [20b55167-eaae-4d44-ac43-78b1f8b13100] POST https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringInstances?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
Prefer:REDACTED
Accept:application/json;odata=minimalmetadata
Content-Type:application/json;odata=nometadata
x-ms-client-request-id:20b55167-eaae-4d44-ac43-78b1f8b13100
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:20   [Information]   Response [7c2d5c94-bf05-4df9-a4e1-b361654854c9] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c43e-a003-00d0-0452-0256e9000000
x-ms-client-request-id:7c2d5c94-bf05-4df9-a4e1-b361654854c9
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/xml

2026-06-22T14:21:20   [Information]   Response [20b55167-eaae-4d44-ac43-78b1f8b13100] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A19.736435Z'"
Location:REDACTED
x-ms-request-id:16a685ad-0002-00bb-2852-02d11d000000
x-ms-client-request-id:20b55167-eaae-4d44-ac43-78b1f8b13100
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Preference-Applied:REDACTED
DataServiceId:REDACTED
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Length:0

2026-06-22T14:21:20   [Information]   8b392e4fc0a5491482f3f3b72693b801: Updated Instances table and set the runtime status to 'Pending'
2026-06-22T14:21:20   [Warning]   🚨 4. ORCHESTRATION SUCCESSFULLY STARTED! Instance ID: 8b392e4fc0a5491482f3f3b72693b801
2026-06-22T14:21:20   [Information]   Executed 'Functions.blob_trigger_starter' (Succeeded, Id=7ff72bb9-c35e-4240-888c-65b4cefd6817, Duration=1915ms)
2026-06-22T14:21:20   [Information]   8b392e4fc0a5491482f3f3b72693b801: Fetched [ExecutionStarted] message from funccallmonitoring-control-03 (delay = 761ms)
2026-06-22T14:21:20   [Information]   Request [74731401-9da5-43ae-b98a-228fad8751a4] DELETE https://rgd1tsandboxaiapp01846c.queue.core.windows.net/azure-webjobs-blobtrigger-funccallmonitoring/messages/80a5d654-5a2c-4875-9a56-f55e8344c71a?popreceipt=AgAAAAMAAAAAAAAA2aaRyVMC3QE%3D
x-ms-version:2025-11-05
Accept:application/xml
x-ms-client-request-id:74731401-9da5-43ae-b98a-228fad8751a4
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:19 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:20   [Information]   Request [08d83d87-6daf-468c-88f4-5f7c06c82b49] GET https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringInstances()?$format=REDACTED&$top=REDACTED&$select=REDACTED&$filter=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
Accept:application/json;odata=minimalmetadata
x-ms-client-request-id:08d83d87-6daf-468c-88f4-5f7c06c82b49
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:20   [Information]   Response [74731401-9da5-43ae-b98a-228fad8751a4] 204 No Content (00.0s)
x-ms-request-id:97a8c445-a003-00d0-0b52-0256e9000000
x-ms-client-request-id:74731401-9da5-43ae-b98a-228fad8751a4
x-ms-version:2025-11-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Length:0

2026-06-22T14:21:20   [Information]   Response [08d83d87-6daf-468c-88f4-5f7c06c82b49] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:16a685ae-0002-00bb-2952-02d11d000000
x-ms-client-request-id:08d83d87-6daf-468c-88f4-5f7c06c82b49
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/json;odata=minimalmetadata;streaming=true;charset=utf-8

2026-06-22T14:21:20   [Information]   Fetched instance status for 8b392e4fc0a5491482f3f3b72693b801
2026-06-22T14:21:20   [Information]   Request [1d472fac-a543-4e60-92fc-aec064a99fac] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:1d472fac-a543-4e60-92fc-aec064a99fac
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:19 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:20   [Information]   Request [20f06217-150d-446e-a1a4-974a992f6717] GET https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringHistory()?$format=REDACTED&$filter=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
Accept:application/json;odata=minimalmetadata
x-ms-client-request-id:20f06217-150d-446e-a1a4-974a992f6717
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:20   [Information]   Response [1d472fac-a543-4e60-92fc-aec064a99fac] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c449-a003-00d0-0f52-0256e9000000
x-ms-client-request-id:1d472fac-a543-4e60-92fc-aec064a99fac
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/xml

2026-06-22T14:21:20   [Information]   funccallmonitoring-control-03: No new messages were found - backing off
2026-06-22T14:21:20   [Information]   Request [2a51461c-549c-4568-910d-4a20ef3a74ee] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:2a51461c-549c-4568-910d-4a20ef3a74ee
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:19 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:20   [Information]   Response [2a51461c-549c-4568-910d-4a20ef3a74ee] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c44a-a003-00d0-1052-0256e9000000
x-ms-client-request-id:2a51461c-549c-4568-910d-4a20ef3a74ee
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/xml

2026-06-22T14:21:20   [Information]   Response [20f06217-150d-446e-a1a4-974a992f6717] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:16a685af-0002-00bb-2a52-02d11d000000
x-ms-client-request-id:20f06217-150d-446e-a1a4-974a992f6717
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/json;odata=minimalmetadata;streaming=true;charset=utf-8

2026-06-22T14:21:20   [Information]   8b392e4fc0a5491482f3f3b72693b801: No history events were found
2026-06-22T14:21:20   [Information]   8b392e4fc0a5491482f3f3b72693b801: Processing [ExecutionStarted] (total delay = 779ms)
2026-06-22T14:21:20   [Verbose]   TaskOrchestrationDispatcher-6569a3b66664455a990b7ecb7508b417-0: Fetched next work item '8b392e4fc0a5491482f3f3b72693b801' after 244749833ms. Current active work-item count: 0. Maximum active work-item count: 20
2026-06-22T14:21:20   [Verbose]   TaskOrchestrationDispatcher-6569a3b66664455a990b7ecb7508b417-0: Fetching next work item. Current active work-item count: 1. Maximum active work-item count: 20. Timeout: 30s
2026-06-22T14:21:20   [Verbose]   TaskOrchestrationDispatcher-6569a3b66664455a990b7ecb7508b417-0: Processing work-item '8b392e4fc0a5491482f3f3b72693b801'
2026-06-22T14:21:20   [Verbose]   8b392e4fc0a5491482f3f3b72693b801: Preparing to process a [ExecutionStarted] message
2026-06-22T14:21:20   [Information]   8b392e4fc0a5491482f3f3b72693b801: Executing 'video_orchestrator' orchestration logic
2026-06-22T14:21:20   [Information]   Executing 'Functions.video_orchestrator' (Reason='(null)', Id=9c6168bc-ba2f-42b4-93bd-fc1042b9b542)
2026-06-22T14:21:20   [Information]   8b392e4fc0a5491482f3f3b72693b801: Function 'video_orchestrator (Orchestrator)' started. IsReplay: False. Input: (Redacted 122 characters). State: Started. RuntimeStatus: Running. HubName: funccallmonitoring. AppName: funccallmonitoring. SlotName: Production. ExtensionVersion: 3.12.3. SequenceNumber: 15. TaskEventId: -1
2026-06-22T14:21:20   [Verbose]   Sending invocation id: '9c6168bc-ba2f-42b4-93bd-fc1042b9b542
2026-06-22T14:21:20   [Verbose]   Posting invocation id:9c6168bc-ba2f-42b4-93bd-fc1042b9b542 on workerId:788f0a3b-fad5-4de0-b3dd-9699fa2a79e5
2026-06-22T14:21:20   [Information]   8b392e4fc0a5491482f3f3b72693b801: Function 'process_video_activity (Activity)' scheduled. Reason: video_orchestrator. IsReplay: False. State: Scheduled. RuntimeStatus: Pending. HubName: funccallmonitoring. AppName: funccallmonitoring. SlotName: Production. ExtensionVersion: 3.12.3. SequenceNumber: 16.
2026-06-22T14:21:20   [Information]   Executed 'Functions.video_orchestrator' (Succeeded, Id=9c6168bc-ba2f-42b4-93bd-fc1042b9b542, Duration=26ms)
2026-06-22T14:21:20   [Information]   8b392e4fc0a5491482f3f3b72693b801: Function 'video_orchestrator (Orchestrator)' awaited. IsReplay: False. State: Awaited. HubName: funccallmonitoring. AppName: funccallmonitoring. SlotName: Production. ExtensionVersion: 3.12.3. SequenceNumber: 17.
2026-06-22T14:21:20   [Information]   8b392e4fc0a5491482f3f3b72693b801: Orchestration 'video_orchestrator' awaited and scheduled 1 durable operation(s).
2026-06-22T14:21:20   [Information]   8b392e4fc0a5491482f3f3b72693b801: Scheduling activity [process_video_activity#0] with 0 bytes of input
2026-06-22T14:21:20   [Information]   8b392e4fc0a5491482f3f3b72693b801: Sending [TaskScheduled#0] message to funccallmonitoring-workitems for instance '8b392e4fc0a5491482f3f3b72693b801'
2026-06-22T14:21:20   [Information]   Request [a796683d-b1ca-4f9c-8c89-3964feac7d38] POST https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-workitems/messages?messagettl=-1
x-ms-version:2025-05-05
Accept:application/xml
Content-Type:application/xml
x-ms-client-request-id:a796683d-b1ca-4f9c-8c89-3964feac7d38
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:19 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:20   [Information]   Response [a796683d-b1ca-4f9c-8c89-3964feac7d38] 201 Created (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:97a8c44f-a003-00d0-1552-0256e9000000
x-ms-client-request-id:a796683d-b1ca-4f9c-8c89-3964feac7d38
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/xml

2026-06-22T14:21:20   [Information]   Request [3b6629c1-097c-4ba9-a942-809c5dc0d710] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-workitems/messages?numofmessages=1&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:3b6629c1-097c-4ba9-a942-809c5dc0d710
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:19 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:20   [Information]   Request [e84e98e9-1815-4350-873c-4c8a1078d420] POST https://rgd1tsandboxaiapp01846c.table.core.windows.net/$batch
x-ms-version:REDACTED
DataServiceVersion:REDACTED
Accept:application/json
Content-Type:multipart/mixed; boundary=batch_ceb126f7-ad1c-45fd-8321-90c798c4e7d3
x-ms-client-request-id:e84e98e9-1815-4350-873c-4c8a1078d420
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:20   [Information]   Response [3b6629c1-097c-4ba9-a942-809c5dc0d710] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c451-a003-00d0-1652-0256e9000000
x-ms-client-request-id:3b6629c1-097c-4ba9-a942-809c5dc0d710
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/xml

2026-06-22T14:21:20   [Information]   8b392e4fc0a5491482f3f3b72693b801: Fetched [TaskScheduled#0] message from funccallmonitoring-workitems (delay = 826ms)
2026-06-22T14:21:20   [Information]   8b392e4fc0a5491482f3f3b72693b801: Processing [TaskScheduled#0] (total delay = 826ms)
2026-06-22T14:21:20   [Verbose]   TaskActivityDispatcher-cb0d53800a414d848db1d856ae30b14d-0: Fetched next work item 'b25e58fb-47c8-44c2-a64f-cf5e3b14dd5f' after 244750135ms. Current active work-item count: 0. Maximum active work-item count: 20
2026-06-22T14:21:20   [Verbose]   TaskActivityDispatcher-cb0d53800a414d848db1d856ae30b14d-0: Fetching next work item. Current active work-item count: 1. Maximum active work-item count: 20. Timeout: 30s
2026-06-22T14:21:20   [Information]   Request [ab80bf34-cf28-40ee-a7b5-a396f2abd995] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-workitems/messages?numofmessages=1&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:ab80bf34-cf28-40ee-a7b5-a396f2abd995
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:19 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:20   [Verbose]   TaskActivityDispatcher-cb0d53800a414d848db1d856ae30b14d-0: Processing work-item 'b25e58fb-47c8-44c2-a64f-cf5e3b14dd5f'
2026-06-22T14:21:20   [Information]   8b392e4fc0a5491482f3f3b72693b801: Starting task activity [process_video_activity#0]
2026-06-22T14:21:20   [Information]   8b392e4fc0a5491482f3f3b72693b801: Function 'process_video_activity (Activity)' started. IsReplay: False. Input: (Redacted 124 characters). State: Started. RuntimeStatus: Running. HubName: funccallmonitoring. AppName: funccallmonitoring. SlotName: Production. ExtensionVersion: 3.12.3. SequenceNumber: 18. TaskEventId: 0
2026-06-22T14:21:20   [Information]   Executing 'Functions.process_video_activity' (Reason='(null)', Id=31040398-1bdf-4181-89f9-152889c90e2f)
2026-06-22T14:21:20   [Information]   Request [884c8f23-3a9d-4c17-b8eb-462f00e3df02] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:884c8f23-3a9d-4c17-b8eb-462f00e3df02
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:19 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:20   [Verbose]   Sending invocation id: '31040398-1bdf-4181-89f9-152889c90e2f
2026-06-22T14:21:20   [Verbose]   Posting invocation id:31040398-1bdf-4181-89f9-152889c90e2f on workerId:788f0a3b-fad5-4de0-b3dd-9699fa2a79e5
2026-06-22T14:21:20   [Information]   Response [ab80bf34-cf28-40ee-a7b5-a396f2abd995] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c453-a003-00d0-1852-0256e9000000
x-ms-client-request-id:ab80bf34-cf28-40ee-a7b5-a396f2abd995
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/xml

2026-06-22T14:21:20   [Information]   Request [3fccb7b7-ee25-4b97-b123-c07bce96e10a] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-workitems/messages?numofmessages=1&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:3fccb7b7-ee25-4b97-b123-c07bce96e10a
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:19 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:20   [Information]   Response [e84e98e9-1815-4350-873c-4c8a1078d420] 202 Accepted (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:16a685b1-0002-00bb-2b52-02d11d000000
x-ms-client-request-id:e84e98e9-1815-4350-873c-4c8a1078d420
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:multipart/mixed; boundary=batchresponse_b58374d0-b92b-4900-b854-ebdac5b4ac23

2026-06-22T14:21:20   [Information]   Response [884c8f23-3a9d-4c17-b8eb-462f00e3df02] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:c40d9b89-3003-008f-4152-02e2d5000000
x-ms-client-request-id:884c8f23-3a9d-4c17-b8eb-462f00e3df02
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/xml

2026-06-22T14:21:20   [Information]   8b392e4fc0a5491482f3f3b72693b801: Appended 4 new events to the history table in 0ms
2026-06-22T14:21:20   [Information]   Request [06a80f94-0235-4cbb-9f52-5d18b12c80f5] PATCH https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringInstances(PartitionKey='8b392e4fc0a5491482f3f3b72693b801',RowKey='')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:06a80f94-0235-4cbb-9f52-5d18b12c80f5
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:20   [Warning]   🚨 5. ACTIVITY STARTED! Now processing video: bb12.mp4
2026-06-22T14:21:20   [Information]   No environment configuration found.
2026-06-22T14:21:20   [Information]   Response [3fccb7b7-ee25-4b97-b123-c07bce96e10a] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c457-a003-00d0-1c52-0256e9000000
x-ms-client-request-id:3fccb7b7-ee25-4b97-b123-c07bce96e10a
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/xml

2026-06-22T14:21:20   [Information]   ManagedIdentityCredential will use App Service managed identity
2026-06-22T14:21:20   [Information]   Response [06a80f94-0235-4cbb-9f52-5d18b12c80f5] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A19.8423939Z'"
x-ms-request-id:16a685b2-0002-00bb-2c52-02d11d000000
x-ms-client-request-id:06a80f94-0235-4cbb-9f52-5d18b12c80f5
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Length:0

2026-06-22T14:21:20   [Information]   8b392e4fc0a5491482f3f3b72693b801: Updated Instances table and set the runtime status to 'Running'
2026-06-22T14:21:20   [Information]   8b392e4fc0a5491482f3f3b72693b801: Deleting [ExecutionStarted] message from funccallmonitoring-control-03
2026-06-22T14:21:20   [Information]   Request [a796683d-b1ca-4f9c-8c89-3964feac7d38] DELETE https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages/b612d464-d322-4075-ba0d-813c8e9f9169?popreceipt=AgAAAAMAAAAAAAAA70LkF1MC3QE%3D
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:a796683d-b1ca-4f9c-8c89-3964feac7d38
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:19 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:20   [Information]   Response [a796683d-b1ca-4f9c-8c89-3964feac7d38] 204 No Content (00.0s)
x-ms-request-id:97a8c459-a003-00d0-1d52-0256e9000000
x-ms-client-request-id:a796683d-b1ca-4f9c-8c89-3964feac7d38
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Length:0

2026-06-22T14:21:20   [Verbose]   TaskOrchestrationDispatcher-6569a3b66664455a990b7ecb7508b417-0: Finished processing work-item '8b392e4fc0a5491482f3f3b72693b801'
2026-06-22T14:21:20   [Information]   Request URL: 'http://169.254.129.8:8081/msi/token?api-version=2019-08-01&resource=REDACTED'
Request method: 'GET'
Request headers:
    'X-IDENTITY-HEADER': 'REDACTED'
    'Metadata': 'REDACTED'
    'User-Agent': 'azsdk-python-identity/1.25.3 Python/3.11.13 (Linux-6.6.138.1-1.azl3-x86_64-with-glibc2.31)'
No body was attached to the request
2026-06-22T14:21:20   [Information]   Request [93dfdf30-0d1d-4d21-abdb-da09544b81ec] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/azure-webjobs-blobtrigger-funccallmonitoring/messages?numofmessages=9&visibilitytimeout=600
x-ms-version:2025-11-05
Accept:application/xml
x-ms-client-request-id:93dfdf30-0d1d-4d21-abdb-da09544b81ec
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:19 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:20   [Information]   Response [93dfdf30-0d1d-4d21-abdb-da09544b81ec] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c45f-a003-00d0-2352-0256e9000000
x-ms-client-request-id:93dfdf30-0d1d-4d21-abdb-da09544b81ec
x-ms-version:2025-11-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/xml

2026-06-22T14:21:20   [Verbose]   Poll for function 'blob_trigger_starter' on queue 'azure-webjobs-blobtrigger-funccallmonitoring' with ClientRequestId '93dfdf30-0d1d-4d21-abdb-da09544b81ec' found 0 messages in 4 ms.
2026-06-22T14:21:20   [Verbose]   Function 'blob_trigger_starter' will wait 1511.4266 ms before polling queue 'azure-webjobs-blobtrigger-funccallmonitoring'.
2026-06-22T14:21:20   [Information]   Request [803c7d3c-e66f-42d3-a066-bca1df514e9d] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-workitems/messages?numofmessages=1&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:803c7d3c-e66f-42d3-a066-bca1df514e9d
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:19 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:20   [Information]   Response [803c7d3c-e66f-42d3-a066-bca1df514e9d] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c461-a003-00d0-2552-0256e9000000
x-ms-client-request-id:803c7d3c-e66f-42d3-a066-bca1df514e9d
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/xml

2026-06-22T14:21:20   [Information]   Request [5140d865-40ef-4843-9763-64dd009993ee] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:5140d865-40ef-4843-9763-64dd009993ee
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:19 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:20   [Information]   Response [5140d865-40ef-4843-9763-64dd009993ee] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c46b-a003-00d0-2d52-0256e9000000
x-ms-client-request-id:5140d865-40ef-4843-9763-64dd009993ee
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/xml

2026-06-22T14:21:20   [Information]   Request [0bb9cc39-afd3-4b08-a171-1a193769ed3f] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-workitems/messages?numofmessages=1&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:0bb9cc39-afd3-4b08-a171-1a193769ed3f
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:20 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:20   [Information]   Response [0bb9cc39-afd3-4b08-a171-1a193769ed3f] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c480-a003-00d0-4152-0256e9000000
x-ms-client-request-id:0bb9cc39-afd3-4b08-a171-1a193769ed3f
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/xml

2026-06-22T14:21:20   [Information]   Request [8ecda57f-1052-459f-b2a4-fe4698848cd0] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:8ecda57f-1052-459f-b2a4-fe4698848cd0
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:20 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:20   [Information]   Response [8ecda57f-1052-459f-b2a4-fe4698848cd0] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c490-a003-00d0-5152-0256e9000000
x-ms-client-request-id:8ecda57f-1052-459f-b2a4-fe4698848cd0
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/xml

2026-06-22T14:21:20   [Information]   Request [ed47b896-b739-484b-a4da-782b6cc0f546] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-workitems/messages?numofmessages=1&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:ed47b896-b739-484b-a4da-782b6cc0f546
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:20 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:20   [Information]   Response [ed47b896-b739-484b-a4da-782b6cc0f546] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c4a5-a003-00d0-6352-0256e9000000
x-ms-client-request-id:ed47b896-b739-484b-a4da-782b6cc0f546
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/xml

2026-06-22T14:21:20   [Information]   Request [22abc34a-aec6-4f08-8eaa-18c930004cca] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:22abc34a-aec6-4f08-8eaa-18c930004cca
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:20 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:20   [Information]   Response [22abc34a-aec6-4f08-8eaa-18c930004cca] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c4be-a003-00d0-7a52-0256e9000000
x-ms-client-request-id:22abc34a-aec6-4f08-8eaa-18c930004cca
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/xml

2026-06-22T14:21:20   [Information]   Response status: 200
Response headers:
    'Content-Type': 'application/json; charset=utf-8'
    'Date': 'Mon, 22 Jun 2026 14:21:19 GMT'
    'Server': 'Kestrel'
    'Transfer-Encoding': 'chunked'
    'X-CORRELATION-ID': 'REDACTED'
2026-06-22T14:21:20   [Information]   DefaultAzureCredential acquired a token from ManagedIdentityCredential
2026-06-22T14:21:20   [Information]   Request URL: 'https://aiinnovationstoragedev.blob.core.windows.net/?restype=REDACTED&comp=REDACTED'
Request method: 'POST'
Request headers:
    'Content-Length': '130'
    'x-ms-version': 'REDACTED'
    'Content-Type': 'application/xml'
    'Accept': 'application/xml'
    'User-Agent': 'azsdk-python-storage-blob/12.30.0 Python/3.11.13 (Linux-6.6.138.1-1.azl3-x86_64-with-glibc2.31)'
    'x-ms-date': 'REDACTED'
    'x-ms-client-request-id': 'a36cb412-6e45-11f1-9c53-36556c6652a7'
    'Authorization': 'REDACTED'
A body is sent with the request
2026-06-22T14:21:20   [Information]   Request [2c3b9414-1c34-420b-91e2-502475969c38] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-workitems/messages?numofmessages=1&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:2c3b9414-1c34-420b-91e2-502475969c38
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:20 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:20   [Information]   Response [2c3b9414-1c34-420b-91e2-502475969c38] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c4e8-a003-00d0-2352-0256e9000000
x-ms-client-request-id:2c3b9414-1c34-420b-91e2-502475969c38
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:20 GMT
Content-Type:application/xml

2026-06-22T14:21:20   [Information]   Response status: 200
Response headers:
    'Transfer-Encoding': 'chunked'
    'Content-Type': 'application/xml'
    'Server': 'Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0'
    'x-ms-request-id': '2b2ad269-001e-00f5-2852-02923d000000'
    'x-ms-client-request-id': 'a36cb412-6e45-11f1-9c53-36556c6652a7'
    'x-ms-version': 'REDACTED'
    'Date': 'Mon, 22 Jun 2026 14:21:20 GMT'
2026-06-22T14:21:20   [Information]   SAS URL generated.
2026-06-22T14:21:20   [Information]   Request URL: 'https://aifoundrylab-01.services.ai.azure.com//contentunderstanding/analyzers/CallQuality1:analyze?stringEncoding=REDACTED&api-version=2024-12-01-preview'
Request method: 'POST'
Request headers:
    'Content-Type': 'application/json'
    'Content-Length': '392'
    'Accept': 'application/json'
    'x-ms-client-request-id': 'a3c16534-6e45-11f1-9c53-36556c6652a7'
    'User-Agent': 'azsdk-python-ai-contentunderstanding/1.1.0 Python/3.11.13 (Linux-6.6.138.1-1.azl3-x86_64-with-glibc2.31)'
    'Ocp-Apim-Subscription-Key': 'REDACTED'
A body is sent with the request
2026-06-22T14:21:20   [Information]   Response status: 404
Response headers:
    'Content-Length': '81'
    'Content-Type': 'application/json'
    'Date': 'Mon, 22 Jun 2026 14:21:19 GMT'
2026-06-22T14:21:20   [Error]   Error processing bb12.mp4: (404) Preview API is not supported in this region.
Code: 404
Message: Preview API is not supported in this region.
Traceback (most recent call last):
  File "/home/site/wwwroot/function_app.py", line 132, in process_video_activity
    poller = cu_client.begin_analyze(
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/site/wwwroot/.python_packages/lib/site-packages/azure/core/tracing/decorator.py", line 119, in wrapper_use_tracer
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/site/wwwroot/.python_packages/lib/site-packages/azure/ai/contentunderstanding/_patch.py", line 221, in begin_analyze
    poller = super().begin_analyze(  # pyright: ignore[reportCallIssue]
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/site/wwwroot/.python_packages/lib/site-packages/azure/core/tracing/decorator.py", line 119, in wrapper_use_tracer
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/site/wwwroot/.python_packages/lib/site-packages/azure/ai/contentunderstanding/_operations/_operations.py", line 807, in begin_analyze
    raw_result = self._analyze_initial(
                 ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/site/wwwroot/.python_packages/lib/site-packages/azure/ai/contentunderstanding/_operations/_operations.py", line 632, in _analyze_initial
    map_error(
  File "/home/site/wwwroot/.python_packages/lib/site-packages/azure/core/exceptions.py", line 163, in map_error
    raise error
azure.core.exceptions.ResourceNotFoundError: (404) Preview API is not supported in this region.
Code: 404
Message: Preview API is not supported in this region.
2026-06-22T14:21:21   [Error]   Executed 'Functions.process_video_activity' (Failed, Id=31040398-1bdf-4181-89f9-152889c90e2f, Duration=688ms)
2026-06-22T14:21:21   [Error]   8b392e4fc0a5491482f3f3b72693b801: Function 'process_video_activity (Activity)' failed with an error. Reason: System.Exception
. IsReplay: False. State: Failed. RuntimeStatus: Failed. HubName: funccallmonitoring. AppName: funccallmonitoring. SlotName: Production. ExtensionVersion: 3.12.3. SequenceNumber: 19. TaskEventId: 0
2026-06-22T14:21:21   [Information]   8b392e4fc0a5491482f3f3b72693b801: Task activity [process_video_activity] failed: FailureSource: 
Details: {"$type":"System.Exception, System.Private.CoreLib","ClassName":"System.Exception","Message":" ResourceNotFoundError: (404) Preview API is not supported in this region.\nCode: 404\nMessage: Preview API is not supported in this region.","Data":null,"InnerException":{"$type":"Microsoft.Azure.WebJobs.Script.Workers.Rpc.RpcException, Microsoft.Azure.WebJobs.Script","IsUserException":false,"RemoteStackTrace":"Traceback (most recent call last):\n  File \"/azure-functions-host/workers/python/3.11/LINUX/X64/azure_functions_worker/dispatcher.py\", line 685, in _handle__invocation_request\n    call_result = await self._loop.run_in_executor(\n                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/local/lib/python3.11/concurrent/futures/thread.py\", line 58, in run\n    result = self.fn(*self.args, **self.kwargs)\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/azure-functions-host/workers/python/3.11/LINUX/X64/azure_functions_worker/dispatcher.py\", line 1019, in _run_sync_func\n    return ExtensionManager.get_sync_invocation_wrapper(context,\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/azure-functions-host/workers/python/3.11/LINUX/X64/azure_functions_worker/extension.py\", line 211, in _raw_invocation_wrapper\n    result = function(**args)\n             ^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/function_app.py\", line 182, in process_video_activity\n    raise e\n  File \"/home/site/wwwroot/function_app.py\", line 132, in process_video_activity\n    poller = cu_client.begin_analyze(\n             ^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/core/tracing/decorator.py\", line 119, in wrapper_use_tracer\n    return func(*args, **kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/ai/contentunderstanding/_patch.py\", line 221, in begin_analyze\n    poller = super().begin_analyze(  # pyright: ignore[reportCallIssue]\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/core/tracing/decorator.py\", line 119, in wrapper_use_tracer\n    return func(*args, **kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/ai/contentunderstanding/_operations/_operations.py\", line 807, in begin_analyze\n    raw_result = self._analyze_initial(\n                 ^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/ai/contentunderstanding/_operations/_operations.py\", line 632, in _analyze_initial\n    map_error(\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/core/exceptions.py\", line 163, in map_error\n    raise error\nazure.core.exceptions.ResourceNotFoundError: (404) Preview API is not supported in this region.\nCode: 404\nMessage: Preview API is not supported in this region.\n","RemoteMessage":"ResourceNotFoundError: (404) Preview API is not supported in this region.\nCode: 404\nMessage: Preview API is not supported in this region.","RemoteTypeName":null,"Message":"Result: Failure\nType: \nException: ResourceNotFoundError: (404) Preview API is not supported in this region.\nCode: 404\nMessage: Preview API is not supported in this region.\nStack: Traceback (most recent call last):\n  File \"/azure-functions-host/workers/python/3.11/LINUX/X64/azure_functions_worker/dispatcher.py\", line 685, in _handle__invocation_request\n    call_result = await self._loop.run_in_executor(\n                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/local/lib/python3.11/concurrent/futures/thread.py\", line 58, in run\n    result = self.fn(*self.args, **self.kwargs)\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/azure-functions-host/workers/python/3.11/LINUX/X64/azure_functions_worker/dispatcher.py\", line 1019, in _run_sync_func\n    return ExtensionManager.get_sync_invocation_wrapper(context,\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/azure-functions-host/workers/python/3.11/LINUX/X64/azure_functions_worker/extension.py\", line 211, in _raw_invocation_wrapper\n    result = function(**args)\n             ^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/function_app.py\", line 182, in process_video_activity\n    raise e\n  File \"/home/site/wwwroot/function_app.py\", line 132, in process_video_activity\n    poller = cu_client.begin_analyze(\n             ^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/core/tracing/decorator.py\", line 119, in wrapper_use_tracer\n    return func(*args, **kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/ai/contentunderstanding/_patch.py\", line 221, in begin_analyze\n    poller = super().begin_analyze(  # pyright: ignore[reportCallIssue]\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/core/tracing/decorator.py\", line 119, in wrapper_use_tracer\n    return func(*args, **kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/ai/contentunderstanding/_operations/_operations.py\", line 807, in begin_analyze\n    raw_result = self._analyze_initial(\n                 ^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/ai/contentunderstanding/_operations/_operations.py\", line 632, in _analyze_initial\n    map_error(\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/core/exceptions.py\", line 163, in map_error\n    raise error\nazure.core.exceptions.ResourceNotFoundError: (404) Preview API is not supported in this region.\nCode: 404\nMessage: Preview API is not supported in this region.\n","Data":{"$type":"System.Collections.ListDictionaryInternal, System.Private.CoreLib"},"InnerException":null,"HelpLink":null,"Source":"System.Private.CoreLib","HResult":-2146233088,"StackTrace":"   at Microsoft.Azure.WebJobs.Script.Description.WorkerFunctionInvoker.InvokeCore(Object[] parameters, FunctionInvocationContext context) in /_/src/WebJobs.Script.Grpc/WorkerFunctionInvoker.cs:line 103\n   at Microsoft.Azure.WebJobs.Script.Description.FunctionInvokerBase.Invoke(Object[] parameters) in /_/src/WebJobs.Script/Description/FunctionInvokerBase.cs:line 82\n   at Microsoft.Azure.WebJobs.Script.Description.FunctionGenerator.Coerce[T](Task`1 src) in /_/src/WebJobs.Script/Description/FunctionGenerator.cs:line 225\n   at Microsoft.Azure.WebJobs.Host.Executors.FunctionInvoker`2.InvokeAsync(Object instance, Object[] arguments) in /_/src/Microsoft.Azure.WebJobs.Host/Executors/FunctionInvoker.cs:line 53\n   at Microsoft.Azure.WebJobs.Host.Executors.FunctionExecutor.InvokeWithTimeoutAsync(IFunctionInvoker invoker, ParameterHelper parameterHelper, CancellationTokenSource timeoutTokenSource, CancellationTokenSource functionCancellationTokenSource, Boolean throwOnTimeout, TimeSpan timerInterval, IFunctionInstance instance) in /_/src/Microsoft.Azure.WebJobs.Host/Executors/FunctionExecutor.cs:line 590\n   at Microsoft.Azure.WebJobs.Host.Executors.FunctionExecutor.ExecuteWithWatchersAsync(IFunctionInstanceEx instance, ParameterHelper parameterHelper, ILogger logger, CancellationTokenSource functionCancellationTokenSource) in /_/src/Microsoft.Azure.WebJobs.Host/Executors/FunctionExecutor.cs:line 536\n   at Microsoft.Azure.WebJobs.Host.Executors.FunctionExecutor.ExecuteWithLoggingAsync(IFunctionInstanceEx instance, FunctionStartedMessage message, FunctionInstanceLogEntry instanceLogEntry, ParameterHelper parameterHelper, ILogger logger, CancellationToken cancellationToken) in /_/src/Microsoft.Azure.WebJobs.Host/Executors/FunctionExecutor.cs:line 315"},"HelpURL":null,"StackTraceString":null,"RemoteStackTraceString":null,"RemoteStackIndex":0,"ExceptionMethod":null,"HResult":-2146233088,"Source":null,"WatsonBuckets":null}
Message: Activity function 'process_video_activity' failed:  ResourceNotFoundError: (404) Preview API is not supported in this region.
Code: 404
Message: Preview API is not supported in this region.
Exception: DurableTask.Core.Exceptions.TaskFailureException: Activity function 'process_video_activity' failed:  ResourceNotFoundError: (404) Preview API is not supported in this region.
Code: 404
Message: Preview API is not supported in this region.
   at Microsoft.Azure.WebJobs.Extensions.DurableTask.TaskActivityShim.RunAsync(TaskContext context, String rawInput) in /_/src/WebJobs.Extensions.DurableTask/Listener/TaskActivityShim.cs:line 122
   at DurableTask.Core.TaskActivityDispatcher.<>c__DisplayClass15_1.<<OnProcessWorkItemAsync>b__2>d.MoveNext() in /_/src/DurableTask.Core/TaskActivityDispatcher.cs:line 211
--- End of stack trace from previous location ---
   at DurableTask.Core.TaskActivityDispatcher.OnProcessWorkItemAsync(TaskActivityWorkItem workItem) in /_/src/DurableTask.Core/TaskActivityDispatcher.cs:line 188
2026-06-22T14:21:21   [Information]   8b392e4fc0a5491482f3f3b72693b801: Sending [TaskFailed#0] message to funccallmonitoring-control-03 for instance '8b392e4fc0a5491482f3f3b72693b801'
2026-06-22T14:21:21   [Information]   Request [3b012308-0c1d-4c18-9586-3c597b200d07] POST https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?messagettl=-1
x-ms-version:2025-05-05
Accept:application/xml
Content-Type:application/xml
x-ms-client-request-id:3b012308-0c1d-4c18-9586-3c597b200d07
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:20 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:21   [Information]   Response [3b012308-0c1d-4c18-9586-3c597b200d07] 201 Created (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:97a8c509-a003-00d0-4452-0256e9000000
x-ms-client-request-id:3b012308-0c1d-4c18-9586-3c597b200d07
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:20 GMT
Content-Type:application/xml

2026-06-22T14:21:21   [Information]   8b392e4fc0a5491482f3f3b72693b801: Deleting [TaskScheduled#0] message from funccallmonitoring-workitems
2026-06-22T14:21:21   [Information]   Request [c6f1809f-f99d-48a6-8d7d-0cce2f148f64] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:c6f1809f-f99d-48a6-8d7d-0cce2f148f64
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:20 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:21   [Information]   Request [3b012308-0c1d-4c18-9586-3c597b200d07] DELETE https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-workitems/messages/b25e58fb-47c8-44c2-a64f-cf5e3b14dd5f?popreceipt=AgAAAAMAAAAAAAAA7qrxF1MC3QE%3D
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:3b012308-0c1d-4c18-9586-3c597b200d07
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:20 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:21   [Information]   Response [3b012308-0c1d-4c18-9586-3c597b200d07] 204 No Content (00.0s)
x-ms-request-id:c40d9c88-3003-008f-3452-02e2d5000000
x-ms-client-request-id:3b012308-0c1d-4c18-9586-3c597b200d07
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Length:0

2026-06-22T14:21:21   [Information]   Response [c6f1809f-f99d-48a6-8d7d-0cce2f148f64] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c50d-a003-00d0-4852-0256e9000000
x-ms-client-request-id:c6f1809f-f99d-48a6-8d7d-0cce2f148f64
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:20 GMT
Content-Type:application/xml

2026-06-22T14:21:21   [Verbose]   TaskActivityDispatcher-cb0d53800a414d848db1d856ae30b14d-0: Finished processing work-item 'b25e58fb-47c8-44c2-a64f-cf5e3b14dd5f'
2026-06-22T14:21:21   [Information]   8b392e4fc0a5491482f3f3b72693b801: Fetched [TaskFailed#0] message from funccallmonitoring-control-03 (delay = 546ms)
2026-06-22T14:21:21   [Information]   Request [abbb2fa5-8876-4b0d-8d82-096c2ffcd3b9] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:abbb2fa5-8876-4b0d-8d82-096c2ffcd3b9
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:20 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:21   [Information]   Request [90603be7-4556-4bda-b38b-df6ff32d7116] GET https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringHistory()?$format=REDACTED&$filter=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
Accept:application/json;odata=minimalmetadata
x-ms-client-request-id:90603be7-4556-4bda-b38b-df6ff32d7116
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:21   [Information]   Response [abbb2fa5-8876-4b0d-8d82-096c2ffcd3b9] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c50e-a003-00d0-4952-0256e9000000
x-ms-client-request-id:abbb2fa5-8876-4b0d-8d82-096c2ffcd3b9
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:20 GMT
Content-Type:application/xml

2026-06-22T14:21:21   [Information]   funccallmonitoring-control-03: No new messages were found - backing off
2026-06-22T14:21:21   [Information]   Request [cbcea109-7483-4b40-9d77-e167ba7c75b3] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:cbcea109-7483-4b40-9d77-e167ba7c75b3
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:20 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:21   [Information]   Response [90603be7-4556-4bda-b38b-df6ff32d7116] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:16a685bf-0002-00bb-3752-02d11d000000
x-ms-client-request-id:90603be7-4556-4bda-b38b-df6ff32d7116
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:20 GMT
Content-Type:application/json;odata=minimalmetadata;streaming=true;charset=utf-8

2026-06-22T14:21:21   [Information]   Response [cbcea109-7483-4b40-9d77-e167ba7c75b3] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c510-a003-00d0-4b52-0256e9000000
x-ms-client-request-id:cbcea109-7483-4b40-9d77-e167ba7c75b3
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:20 GMT
Content-Type:application/xml

2026-06-22T14:21:21   [Information]   8b392e4fc0a5491482f3f3b72693b801: Fetched 4 history events from the history table in 7ms
2026-06-22T14:21:21   [Information]   8b392e4fc0a5491482f3f3b72693b801: Processing [TaskFailed#0] (total delay = 555ms)
2026-06-22T14:21:21   [Verbose]   TaskOrchestrationDispatcher-6569a3b66664455a990b7ecb7508b417-0: Fetched next work item '8b392e4fc0a5491482f3f3b72693b801' after 773ms. Current active work-item count: 0. Maximum active work-item count: 20
2026-06-22T14:21:21   [Verbose]   TaskOrchestrationDispatcher-6569a3b66664455a990b7ecb7508b417-0: Fetching next work item. Current active work-item count: 1. Maximum active work-item count: 20. Timeout: 30s
2026-06-22T14:21:21   [Verbose]   TaskOrchestrationDispatcher-6569a3b66664455a990b7ecb7508b417-0: Processing work-item '8b392e4fc0a5491482f3f3b72693b801'
2026-06-22T14:21:21   [Verbose]   8b392e4fc0a5491482f3f3b72693b801: Preparing to process a [TaskFailed#0] message
2026-06-22T14:21:21   [Information]   8b392e4fc0a5491482f3f3b72693b801: Executing 'video_orchestrator' orchestration logic
2026-06-22T14:21:21   [Information]   Executing 'Functions.video_orchestrator' (Reason='(null)', Id=7e832a03-1d24-443c-a8ef-6949c2107822)
2026-06-22T14:21:21   [Verbose]   Sending invocation id: '7e832a03-1d24-443c-a8ef-6949c2107822
2026-06-22T14:21:21   [Verbose]   Posting invocation id:7e832a03-1d24-443c-a8ef-6949c2107822 on workerId:788f0a3b-fad5-4de0-b3dd-9699fa2a79e5
2026-06-22T14:21:21   [Error]   8b392e4fc0a5491482f3f3b72693b801: Function 'video_orchestrator (Orchestrator)' failed with an error. Reason: DurableTask.Core.Exceptions.OrchestrationFailureException
   at Microsoft.Azure.WebJobs.Extensions.DurableTask.OutOfProcOrchestrationShim.ScheduleDurableTaskEvents(OrchestrationInvocationResult result) in /_/src/WebJobs.Extensions.DurableTask/Listener/OutOfProcOrchestrationShim.cs:line 88
   at Microsoft.Azure.WebJobs.Extensions.DurableTask.OutOfProcOrchestrationShim.HandleDurableTaskReplay(OrchestrationInvocationResult executionJson) in /_/src/WebJobs.Extensions.DurableTask/Listener/OutOfProcOrchestrationShim.cs:line 65
   at Microsoft.Azure.WebJobs.Extensions.DurableTask.TaskOrchestrationShim.TraceAndReplay(Object result, Exception ex) in /_/src/WebJobs.Extensions.DurableTask/Listener/TaskOrchestrationShim.cs:line 242
   at Microsoft.Azure.WebJobs.Extensions.DurableTask.TaskOrchestrationShim.InvokeUserCodeAndHandleResults(RegisteredFunctionInfo orchestratorInfo, OrchestrationContext innerContext) in /_/src/WebJobs.Extensions.DurableTask/Listener/TaskOrchestrationShim.cs:line 181. IsReplay: False. State: Failed. RuntimeStatus: Failed. HubName: funccallmonitoring. AppName: funccallmonitoring. SlotName: Production. ExtensionVersion: 3.12.3. SequenceNumber: 20. TaskEventId: -1
2026-06-22T14:21:21   [Error]   Executed 'Functions.video_orchestrator' (Failed, Id=7e832a03-1d24-443c-a8ef-6949c2107822, Duration=26ms)
2026-06-22T14:21:21   [Information]   8b392e4fc0a5491482f3f3b72693b801: Orchestration 'video_orchestrator' awaited and scheduled 1 durable operation(s).
2026-06-22T14:21:21   [Information]   8b392e4fc0a5491482f3f3b72693b801: Orchestration completed with a 'Failed' status and 8297 bytes of output. Details: Message: Activity function 'process_video_activity' failed:  ResourceNotFoundError: (404) Preview API is not supported in this region.
Code: 404
Message: Preview API is not supported in this region. 
 {"$type":"System.Exception, System.Private.CoreLib","ClassName":"System.Exception","Message":" ResourceNotFoundError: (404) Preview API is not supported in this region.\nCode: 404\nMessage: Preview API is not supported in this region.","Data":null,"InnerException":{"$type":"Microsoft.Azure.WebJobs.Script.Workers.Rpc.RpcException, Microsoft.Azure.WebJobs.Script","IsUserException":false,"RemoteStackTrace":"Traceback (most recent call last):\n  File \"/azure-functions-host/workers/python/3.11/LINUX/X64/azure_functions_worker/dispatcher.py\", line 685, in _handle__invocation_request\n    call_result = await self._loop.run_in_executor(\n                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/local/lib/python3.11/concurrent/futures/thread.py\", line 58, in run\n    result = self.fn(*self.args, **self.kwargs)\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/azure-functions-host/workers/python/3.11/LINUX/X64/azure_functions_worker/dispatcher.py\", line 1019, in _run_sync_func\n    return ExtensionManager.get_sync_invocation_wrapper(context,\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/azure-functions-host/workers/python/3.11/LINUX/X64/azure_functions_worker/extension.py\", line 211, in _raw_invocation_wrapper\n    result = function(**args)\n             ^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/function_app.py\", line 182, in process_video_activity\n    raise e\n  File \"/home/site/wwwroot/function_app.py\", line 132, in process_video_activity\n    poller = cu_client.begin_analyze(\n             ^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/core/tracing/decorator.py\", line 119, in wrapper_use_tracer\n    return func(*args, **kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/ai/contentunderstanding/_patch.py\", line 221, in begin_analyze\n    poller = super().begin_analyze(  # pyright: ignore[reportCallIssue]\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/core/tracing/decorator.py\", line 119, in wrapper_use_tracer\n    return func(*args, **kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/ai/contentunderstanding/_operations/_operations.py\", line 807, in begin_analyze\n    raw_result = self._analyze_initial(\n                 ^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/ai/contentunderstanding/_operations/_operations.py\", line 632, in _analyze_initial\n    map_error(\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/core/exceptions.py\", line 163, in map_error\n    raise error\nazure.core.exceptions.ResourceNotFoundError: (404) Preview API is not supported in this region.\nCode: 404\nMessage: Preview API is not supported in this region.\n","RemoteMessage":"ResourceNotFoundError: (404) Preview API is not supported in this region.\nCode: 404\nMessage: Preview API is not supported in this region.","RemoteTypeName":null,"Message":"Result: Failure\nType: \nException: ResourceNotFoundError: (404) Preview API is not supported in this region.\nCode: 404\nMessage: Preview API is not supported in this region.\nStack: Traceback (most recent call last):\n  File \"/azure-functions-host/workers/python/3.11/LINUX/X64/azure_functions_worker/dispatcher.py\", line 685, in _handle__invocation_request\n    call_result = await self._loop.run_in_executor(\n                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/local/lib/python3.11/concurrent/futures/thread.py\", line 58, in run\n    result = self.fn(*self.args, **self.kwargs)\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/azure-functions-host/workers/python/3.11/LINUX/X64/azure_functions_worker/dispatcher.py\", line 1019, in _run_sync_func\n    return ExtensionManager.get_sync_invocation_wrapper(context,\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/azure-functions-host/workers/python/3.11/LINUX/X64/azure_functions_worker/extension.py\", line 211, in _raw_invocation_wrapper\n    result = function(**args)\n             ^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/function_app.py\", line 182, in process_video_activity\n    raise e\n  File \"/home/site/wwwroot/function_app.py\", line 132, in process_video_activity\n    poller = cu_client.begin_analyze(\n             ^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/core/tracing/decorator.py\", line 119, in wrapper_use_tracer\n    return func(*args, **kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/ai/contentunderstanding/_patch.py\", line 221, in begin_analyze\n    poller = super().begin_analyze(  # pyright: ignore[reportCallIssue]\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/core/tracing/decorator.py\", line 119, in wrapper_use_tracer\n    return func(*args, **kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/ai/contentunderstanding/_operations/_operations.py\", line 807, in begin_analyze\n    raw_result = self._analyze_initial(\n                 ^^^^^^^^^^^^^^^^^^^^^^\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/ai/contentunderstanding/_operations/_operations.py\", line 632, in _analyze_initial\n    map_error(\n  File \"/home/site/wwwroot/.python_packages/lib/site-packages/azure/core/exceptions.py\", line 163, in map_error\n    raise error\nazure.core.exceptions.ResourceNotFoundError: (404) Preview API is not supported in this region.\nCode: 404\nMessage: Preview API is not supported in this region.\n","Data":{"$type":"System.Collections.ListDictionaryInternal, System.Private.CoreLib"},"InnerException":null,"HelpLink":null,"Source":"System.Private.CoreLib","HResult":-2146233088,"StackTrace":"   at Microsoft.Azure.WebJobs.Script.Description.WorkerFunctionInvoker.InvokeCore(Object[] parameters, FunctionInvocationContext context) in /_/src/WebJobs.Script.Grpc/WorkerFunctionInvoker.cs:line 103\n   at Microsoft.Azure.WebJobs.Script.Description.FunctionInvokerBase.Invoke(Object[] parameters) in /_/src/WebJobs.Script/Description/FunctionInvokerBase.cs:line 82\n   at Microsoft.Azure.WebJobs.Script.Description.FunctionGenerator.Coerce[T](Task`1 src) in /_/src/WebJobs.Script/Description/FunctionGenerator.cs:line 225\n   at Microsoft.Azure.WebJobs.Host.Executors.FunctionInvoker`2.InvokeAsync(Object instance, Object[] arguments) in /_/src/Microsoft.Azure.WebJobs.Host/Executors/FunctionInvoker.cs:line 53\n   at Microsoft.Azure.WebJobs.Host.Executors.FunctionExecutor.InvokeWithTimeoutAsync(IFunctionInvoker invoker, ParameterHelper parameterHelper, CancellationTokenSource timeoutTokenSource, CancellationTokenSource functionCancellationTokenSource, Boolean throwOnTimeout, TimeSpan timerInterval, IFunctionInstance instance) in /_/src/Microsoft.Azure.WebJobs.Host/Executors/FunctionExecutor.cs:line 590\n   at Microsoft.Azure.WebJobs.Host.Executors.FunctionExecutor.ExecuteWithWatchersAsync(IFunctionInstanceEx instance, ParameterHelper parameterHelper, ILogger logger, CancellationTokenSource functionCancellationTokenSource) in /_/src/Microsoft.Azure.WebJobs.Host/Executors/FunctionExecutor.cs:line 536\n   at Microsoft.Azure.WebJobs.Host.Executors.FunctionExecutor.ExecuteWithLoggingAsync(IFunctionInstanceEx instance, FunctionStartedMessage message, FunctionInstanceLogEntry instanceLogEntry, ParameterHelper parameterHelper, ILogger logger, CancellationToken cancellationToken) in /_/src/Microsoft.Azure.WebJobs.Host/Executors/FunctionExecutor.cs:line 315"},"HelpURL":null,"StackTraceString":null,"RemoteStackTraceString":null,"RemoteStackIndex":0,"ExceptionMethod":null,"HResult":-2146233088,"Source":null,"WatsonBuckets":null}, StackTrace:    at System.Threading.Tasks.Task`1.GetResultCore(Boolean waitCompletionNotification)
   at Microsoft.Azure.WebJobs.Extensions.DurableTask.TaskOrchestrationShim.InvokeUserCodeAndHandleResults(RegisteredFunctionInfo orchestratorInfo, OrchestrationContext innerContext) in /_/src/WebJobs.Extensions.DurableTask/Listener/TaskOrchestrationShim.cs:line 148
2026-06-22T14:21:21   [Information]   Request [9a05c584-035b-499b-b67d-9b4c1fd9ecd4] POST https://rgd1tsandboxaiapp01846c.table.core.windows.net/$batch
x-ms-version:REDACTED
DataServiceVersion:REDACTED
Accept:application/json
Content-Type:multipart/mixed; boundary=batch_36bf58e5-c71c-4bfb-898d-1069c9aa4c9e
x-ms-client-request-id:9a05c584-035b-499b-b67d-9b4c1fd9ecd4
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:21   [Information]   Response [9a05c584-035b-499b-b67d-9b4c1fd9ecd4] 202 Accepted (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:16a685c0-0002-00bb-3852-02d11d000000
x-ms-client-request-id:9a05c584-035b-499b-b67d-9b4c1fd9ecd4
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:20 GMT
Content-Type:multipart/mixed; boundary=batchresponse_99ffa4c5-28ee-420e-975e-b1c33a77cb14

2026-06-22T14:21:21   [Information]   8b392e4fc0a5491482f3f3b72693b801: Appended 4 new events to the history table in 0ms
2026-06-22T14:21:21   [Information]   Request [966a6864-caf9-4550-8ee5-a061d0835534] PATCH https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringInstances(PartitionKey='8b392e4fc0a5491482f3f3b72693b801',RowKey='')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:966a6864-caf9-4550-8ee5-a061d0835534
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:21   [Information]   Response [966a6864-caf9-4550-8ee5-a061d0835534] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A20.6021774Z'"
x-ms-request-id:16a685c5-0002-00bb-3b52-02d11d000000
x-ms-client-request-id:966a6864-caf9-4550-8ee5-a061d0835534
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:20 GMT
Content-Length:0

2026-06-22T14:21:21   [Information]   8b392e4fc0a5491482f3f3b72693b801: Updated Instances table and set the runtime status to 'Failed'
2026-06-22T14:21:21   [Information]   8b392e4fc0a5491482f3f3b72693b801: Deleting [TaskFailed#0] message from funccallmonitoring-control-03
2026-06-22T14:21:21   [Information]   Request [c17c5a36-98ac-4a5f-aad9-1811c9d5b4e5] DELETE https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages/50d91994-d8fc-4353-91b9-0a2372cdb4ae?popreceipt=AgAAAAMAAAAAAAAA9IFfGFMC3QE%3D
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:c17c5a36-98ac-4a5f-aad9-1811c9d5b4e5
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:20 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:21   [Information]   Request [af3903d0-a65c-401a-9a2f-9c583496cea4] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:af3903d0-a65c-401a-9a2f-9c583496cea4
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:20 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:21   [Information]   Response [c17c5a36-98ac-4a5f-aad9-1811c9d5b4e5] 204 No Content (00.0s)
x-ms-request-id:97a8c51e-a003-00d0-5752-0256e9000000
x-ms-client-request-id:c17c5a36-98ac-4a5f-aad9-1811c9d5b4e5
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:20 GMT
Content-Length:0

2026-06-22T14:21:21   [Verbose]   TaskOrchestrationDispatcher-6569a3b66664455a990b7ecb7508b417-0: Finished processing work-item '8b392e4fc0a5491482f3f3b72693b801'
2026-06-22T14:21:21   [Information]   Response [af3903d0-a65c-401a-9a2f-9c583496cea4] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:c40d9ca1-3003-008f-4c52-02e2d5000000
x-ms-client-request-id:af3903d0-a65c-401a-9a2f-9c583496cea4
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/xml

2026-06-22T14:21:21   [Information]   Request [96e53293-abb2-4cfc-880d-aacfb731d78d] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:96e53293-abb2-4cfc-880d-aacfb731d78d
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:20 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:21   [Information]   Response [96e53293-abb2-4cfc-880d-aacfb731d78d] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:c40d9ccc-3003-008f-7352-02e2d5000000
x-ms-client-request-id:96e53293-abb2-4cfc-880d-aacfb731d78d
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:19 GMT
Content-Type:application/xml

2026-06-22T14:21:21   [Information]   Request [31f3e4df-669b-4bd7-b456-abfed141294a] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-workitems/messages?numofmessages=1&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:31f3e4df-669b-4bd7-b456-abfed141294a
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:20 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:21   [Information]   Response [31f3e4df-669b-4bd7-b456-abfed141294a] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:c40d9ce8-3003-008f-0d52-02e2d5000000
x-ms-client-request-id:31f3e4df-669b-4bd7-b456-abfed141294a
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:20 GMT
Content-Type:application/xml

2026-06-22T14:21:21   [Information]   Request [5df9a11e-056f-407d-ac46-54fddb018c2e] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:5df9a11e-056f-407d-ac46-54fddb018c2e
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:20 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:21   [Information]   Response [5df9a11e-056f-407d-ac46-54fddb018c2e] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:c40d9d0a-3003-008f-2c52-02e2d5000000
x-ms-client-request-id:5df9a11e-056f-407d-ac46-54fddb018c2e
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:20 GMT
Content-Type:application/xml

2026-06-22T14:21:21   [Information]   Request [532ef471-c8d0-4deb-8251-06ed112d8914] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:532ef471-c8d0-4deb-8251-06ed112d8914
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:21 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:21   [Information]   Response [532ef471-c8d0-4deb-8251-06ed112d8914] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:c40d9d5b-3003-008f-7d52-02e2d5000000
x-ms-client-request-id:532ef471-c8d0-4deb-8251-06ed112d8914
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:20 GMT
Content-Type:application/xml

2026-06-22T14:21:21   [Information]   Request [56a59858-4338-4c19-a602-60fca7089d49] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/azure-webjobs-blobtrigger-funccallmonitoring/messages?numofmessages=9&visibilitytimeout=600
x-ms-version:2025-11-05
Accept:application/xml
x-ms-client-request-id:56a59858-4338-4c19-a602-60fca7089d49
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:21 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:21   [Information]   Response [56a59858-4338-4c19-a602-60fca7089d49] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:c40d9dbb-3003-008f-5c52-02e2d5000000
x-ms-client-request-id:56a59858-4338-4c19-a602-60fca7089d49
x-ms-version:2025-11-05
Date:Mon, 22 Jun 2026 14:21:20 GMT
Content-Type:application/xml

2026-06-22T14:21:21   [Verbose]   Poll for function 'blob_trigger_starter' on queue 'azure-webjobs-blobtrigger-funccallmonitoring' with ClientRequestId '56a59858-4338-4c19-a602-60fca7089d49' found 0 messages in 4 ms.
2026-06-22T14:21:21   [Verbose]   Function 'blob_trigger_starter' will wait 3334.4802 ms before polling queue 'azure-webjobs-blobtrigger-funccallmonitoring'.
2026-06-22T14:21:22   [Information]   Request [5b7acfee-e74d-423d-8cd6-7eec3aed12e3] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-workitems/messages?numofmessages=1&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:5b7acfee-e74d-423d-8cd6-7eec3aed12e3
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:21 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:22   [Information]   Request [7b29115e-a801-4427-a284-515104158bfe] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:7b29115e-a801-4427-a284-515104158bfe
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:21 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:22   [Information]   Response [5b7acfee-e74d-423d-8cd6-7eec3aed12e3] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:c40d9e1d-3003-008f-3952-02e2d5000000
x-ms-client-request-id:5b7acfee-e74d-423d-8cd6-7eec3aed12e3
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:20 GMT
Content-Type:application/xml

2026-06-22T14:21:22   [Information]   Response [7b29115e-a801-4427-a284-515104158bfe] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c5d9-a003-00d0-0852-0256e9000000
x-ms-client-request-id:7b29115e-a801-4427-a284-515104158bfe
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:21 GMT
Content-Type:application/xml

2026-06-22T14:21:22   [Information]   Request [dd661f5f-3df0-4fe9-a521-bcc44d454d5c] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:dd661f5f-3df0-4fe9-a521-bcc44d454d5c
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:22 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:22   [Information]   Response [dd661f5f-3df0-4fe9-a521-bcc44d454d5c] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c678-a003-00d0-1c52-0256e9000000
x-ms-client-request-id:dd661f5f-3df0-4fe9-a521-bcc44d454d5c
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:22 GMT
Content-Type:application/xml

2026-06-22T14:21:23   [Verbose]   [HostMonitor] Checking worker statuses (Count=1)
2026-06-22T14:21:23   [Verbose]   [HostMonitor] Worker status: ID=788f0a3b-fad5-4de0-b3dd-9699fa2a79e5, Latency=1ms
2026-06-22T14:21:23   [Verbose]   [HostMonitor] Host process CPU stats (PID 52): History=(0,2,16,3,0), AvgCpuLoad=4.2, MaxCpuLoad=16
2026-06-22T14:21:23   [Verbose]   [HostMonitor] Host process CPU stats (PID 27): History=(10,31,6,5,2), AvgCpuLoad=11, MaxCpuLoad=31
2026-06-22T14:21:23   [Verbose]   [HostMonitor] Host aggregate CPU load 15
2026-06-22T14:21:23   [Information]   Executing StatusCodeResult, setting HTTP status code 200
2026-06-22T14:21:23   [Information]   Request [2a0cc658-b53e-47e2-bc29-3bc928b7af4a] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-workitems/messages?numofmessages=1&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:2a0cc658-b53e-47e2-bc29-3bc928b7af4a
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:23 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:23   [Information]   Response [2a0cc658-b53e-47e2-bc29-3bc928b7af4a] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c759-a003-00d0-6352-0256e9000000
x-ms-client-request-id:2a0cc658-b53e-47e2-bc29-3bc928b7af4a
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:23 GMT
Content-Type:application/xml

2026-06-22T14:21:24   [Information]   Request [d339fefe-59fb-4899-b8cb-ec4c722d965e] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:d339fefe-59fb-4899-b8cb-ec4c722d965e
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:23 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:24   [Information]   Response [d339fefe-59fb-4899-b8cb-ec4c722d965e] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c7c5-a003-00d0-4252-0256e9000000
x-ms-client-request-id:d339fefe-59fb-4899-b8cb-ec4c722d965e
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:23 GMT
Content-Type:application/xml

2026-06-22T14:21:25   [Information]   Request [a90679bb-e3ca-4e2b-9792-0e216231656e] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/azure-webjobs-blobtrigger-funccallmonitoring/messages?numofmessages=9&visibilitytimeout=600
x-ms-version:2025-11-05
Accept:application/xml
x-ms-client-request-id:a90679bb-e3ca-4e2b-9792-0e216231656e
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:24 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:25   [Information]   Response [a90679bb-e3ca-4e2b-9792-0e216231656e] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8c8e0-a003-00d0-4c52-0256e9000000
x-ms-client-request-id:a90679bb-e3ca-4e2b-9792-0e216231656e
x-ms-version:2025-11-05
Date:Mon, 22 Jun 2026 14:21:24 GMT
Content-Type:application/xml

2026-06-22T14:21:25   [Verbose]   Poll for function 'blob_trigger_starter' on queue 'azure-webjobs-blobtrigger-funccallmonitoring' with ClientRequestId 'a90679bb-e3ca-4e2b-9792-0e216231656e' found 0 messages in 4 ms.
2026-06-22T14:21:25   [Verbose]   Function 'blob_trigger_starter' will wait 5468.6206 ms before polling queue 'azure-webjobs-blobtrigger-funccallmonitoring'.
2026-06-22T14:21:26   [Information]   Request [e0ac676f-42f3-4457-b1ea-2634188c6d82] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/locks/funccallmonitoring/WebJobs.Internal.Blobs.Listener?comp=lease
x-ms-lease-action:renew
x-ms-lease-id:a91e3446-f57f-4eda-b6bf-2d5455b5d031
x-ms-version:2024-11-04
Accept:application/xml
x-ms-client-request-id:e0ac676f-42f3-4457-b1ea-2634188c6d82
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.22.1 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:26 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:26   [Information]   Request [6b3c38ee-fa04-4042-a319-736b3b3eaa66] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/?comp=list&maxresults=1
x-ms-version:2024-11-04
Accept:application/xml
x-ms-client-request-id:6b3c38ee-fa04-4042-a319-736b3b3eaa66
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.22.1 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:26 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:26   [Information]   Response [e0ac676f-42f3-4457-b1ea-2634188c6d82] 200 OK (00.0s)
ETag:"0x8DECE1769D6FB81"
x-ms-request-id:665a14f3-c01e-00d6-6b52-026556000000
x-ms-client-request-id:e0ac676f-42f3-4457-b1ea-2634188c6d82
x-ms-version:2024-11-04
x-ms-lease-id:a91e3446-f57f-4eda-b6bf-2d5455b5d031
Date:Mon, 22 Jun 2026 14:21:25 GMT
Content-Length:0
Last-Modified:Fri, 19 Jun 2026 15:28:28 GMT

2026-06-22T14:21:26   [Information]   Response [6b3c38ee-fa04-4042-a319-736b3b3eaa66] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:4d2554c7-601e-0004-1b52-02e6b8000000
x-ms-client-request-id:6b3c38ee-fa04-4042-a319-736b3b3eaa66
x-ms-version:2024-11-04
Date:Mon, 22 Jun 2026 14:21:25 GMT
Content-Type:application/xml

2026-06-22T14:21:27   [Information]   Request [f41b3b65-1bb0-4cd5-ae2f-6c282286866c] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:f41b3b65-1bb0-4cd5-ae2f-6c282286866c
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:26 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:27   [Information]   Response [f41b3b65-1bb0-4cd5-ae2f-6c282286866c] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8cac8-a003-00d0-0752-0256e9000000
x-ms-client-request-id:f41b3b65-1bb0-4cd5-ae2f-6c282286866c
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:26 GMT
Content-Type:application/xml

2026-06-22T14:21:27   [Information]   Request [06f2e9fa-95d5-4433-9f8e-3d64e135e407] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-workitems/messages?numofmessages=1&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:06f2e9fa-95d5-4433-9f8e-3d64e135e407
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:27 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:27   [Information]   Response [06f2e9fa-95d5-4433-9f8e-3d64e135e407] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8cb48-a003-00d0-8052-0256e9000000
x-ms-client-request-id:06f2e9fa-95d5-4433-9f8e-3d64e135e407
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:26 GMT
Content-Type:application/xml

2026-06-22T14:21:28   [Information]   Request [4f2c0527-72e4-498c-83cd-2a3c132d1cf9] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1400&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:4f2c0527-72e4-498c-83cd-2a3c132d1cf9
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:27 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:28   [Information]   Request [022d12cb-a6a0-4753-87d6-b02b5f15e088] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs?restype=container&comp=list&marker=&maxresults=10000
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:022d12cb-a6a0-4753-87d6-b02b5f15e088
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:27 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:28   [Information]   Response [022d12cb-a6a0-4753-87d6-b02b5f15e088] 200 OK (00.0s)
Transfer-Encoding:chunked
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23d417-f01e-0015-0652-0211a4000000
x-ms-client-request-id:022d12cb-a6a0-4753-87d6-b02b5f15e088
x-ms-version:2026-02-06
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:21:27 GMT
Content-Type:application/xml

2026-06-22T14:21:28   [Verbose]   Poll for blobs newer than '2026-06-22T14:21:17.000Z' in container 'labhrdocs' with ClientRequestId '6afae1b6-457c-4095-ac36-3f43b10e3cbf' found 1 blobs in 4 ms. ContinuationToken: False.
2026-06-22T14:21:28   [Information]   Request [e9f91678-0108-45b9-b7e4-ca3505a3d939] HEAD https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:e9f91678-0108-45b9-b7e4-ca3505a3d939
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:27 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:28   [Information]   Response [4f2c0527-72e4-498c-83cd-2a3c132d1cf9] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:b3477671-301e-0036-2152-02e6cf000000
x-ms-client-request-id:4f2c0527-72e4-498c-83cd-2a3c132d1cf9
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:21:27 GMT
Content-Type:application/xml

2026-06-22T14:21:28   [Information]   Request [3cdc18bb-99e4-40cc-a5f6-2b386c735e06] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1300&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:3cdc18bb-99e4-40cc-a5f6-2b386c735e06
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:27 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:28   [Information]   Response [e9f91678-0108-45b9-b7e4-ca3505a3d939] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Vary:Origin
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23d41b-f01e-0015-0852-0211a4000000
x-ms-client-request-id:e9f91678-0108-45b9-b7e4-ca3505a3d939
x-ms-version:2026-02-06
x-ms-tag-count:2
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:21:27 GMT
Content-Length:41837686
Content-Type:video/mp4
Content-MD5:FDGtsdzxt+wnqxE3hlFsqg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:28   [Information]   Request [16a42b78-7d01-442c-bd61-c312fdc0212c] HEAD https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/blobreceipts/funccallmonitoring/Host.Functions.blob_trigger_starter/%220x8DED069863F6A51%22/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:16a42b78-7d01-442c-bd61-c312fdc0212c
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:27 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:28   [Information]   Response [3cdc18bb-99e4-40cc-a5f6-2b386c735e06] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:b3477679-301e-0036-2752-02e6cf000000
x-ms-client-request-id:3cdc18bb-99e4-40cc-a5f6-2b386c735e06
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:21:27 GMT
Content-Type:application/xml

2026-06-22T14:21:28   [Information]   Response [16a42b78-7d01-442c-bd61-c312fdc0212c] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED06986690316"
x-ms-request-id:5a23bca1-901e-0000-3852-026bbf000000
x-ms-client-request-id:16a42b78-7d01-442c-bd61-c312fdc0212c
x-ms-version:2026-02-06
x-ms-tag-count:2
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:21:27 GMT
Content-Length:0
Content-Type:application/octet-stream
Content-MD5:1B2M2Y8AsgTpgAmY7PhCfg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:28   [Verbose]   Blob 'bb12.mp4' will be skipped for function 'blob_trigger_starter' because this blob with ETag '"0x8DED069863F6A51"' has already been processed. PollId: '6afae1b6-457c-4095-ac36-3f43b10e3cbf'. Source: 'ContainerScan'.
2026-06-22T14:21:28   [Information]   Request [2f36e09d-5661-421b-98f4-96216d608ffe] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-02/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:2f36e09d-5661-421b-98f4-96216d608ffe
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:28 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:28   [Information]   Response [2f36e09d-5661-421b-98f4-96216d608ffe] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8cc55-a003-00d0-7e52-0256e9000000
x-ms-client-request-id:2f36e09d-5661-421b-98f4-96216d608ffe
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:28 GMT
Content-Type:application/xml

2026-06-22T14:21:29   [Information]   Request [14590cd4-0817-4fb2-96f4-a928db80e6fe] GET https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions()?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
Accept:application/json;odata=minimalmetadata
x-ms-client-request-id:14590cd4-0817-4fb2-96f4-a928db80e6fe
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:29   [Information]   Response [14590cd4-0817-4fb2-96f4-a928db80e6fe] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:16a686cd-0002-00bb-7552-02d11d000000
x-ms-client-request-id:14590cd4-0817-4fb2-96f4-a928db80e6fe
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:29 GMT
Content-Type:application/json;odata=minimalmetadata;streaming=true;charset=utf-8

2026-06-22T14:21:29   [Information]   Request [328f6ecf-bfa4-4376-8ce2-8b833666a547] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-00')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A19.3092449Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:328f6ecf-bfa4-4376-8ce2-8b833666a547
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:29   [Information]   Response [328f6ecf-bfa4-4376-8ce2-8b833666a547] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A29.343172Z'"
x-ms-request-id:16a686d0-0002-00bb-7652-02d11d000000
x-ms-client-request-id:328f6ecf-bfa4-4376-8ce2-8b833666a547
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:29 GMT
Content-Length:0

2026-06-22T14:21:29   [Verbose]   funccallmonitoring-control-00:  lease renewal with token  succeeded
2026-06-22T14:21:29   [Information]   Request [9d9b08a7-a24f-42d2-9735-0108720f682e] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-01')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A19.3162337Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:9d9b08a7-a24f-42d2-9735-0108720f682e
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:29   [Information]   Response [9d9b08a7-a24f-42d2-9735-0108720f682e] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A29.3491619Z'"
x-ms-request-id:16a686d1-0002-00bb-7752-02d11d000000
x-ms-client-request-id:9d9b08a7-a24f-42d2-9735-0108720f682e
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:29 GMT
Content-Length:0

2026-06-22T14:21:29   [Verbose]   funccallmonitoring-control-01:  lease renewal with token  succeeded
2026-06-22T14:21:29   [Information]   Request [0618ee13-dfaa-444e-b498-2633d44f575f] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-02')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A19.3222244Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:0618ee13-dfaa-444e-b498-2633d44f575f
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:29   [Information]   Response [0618ee13-dfaa-444e-b498-2633d44f575f] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A29.3561507Z'"
x-ms-request-id:16a686d2-0002-00bb-7852-02d11d000000
x-ms-client-request-id:0618ee13-dfaa-444e-b498-2633d44f575f
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:29 GMT
Content-Length:0

2026-06-22T14:21:29   [Verbose]   funccallmonitoring-control-02:  lease renewal with token  succeeded
2026-06-22T14:21:29   [Information]   Request [18b85f4b-21a8-45ce-a10b-6654c68c0d4b] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-03')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A19.328215Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:18b85f4b-21a8-45ce-a10b-6654c68c0d4b
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:29   [Information]   Response [18b85f4b-21a8-45ce-a10b-6654c68c0d4b] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A29.3621431Z'"
x-ms-request-id:16a686d3-0002-00bb-7952-02d11d000000
x-ms-client-request-id:18b85f4b-21a8-45ce-a10b-6654c68c0d4b
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:29 GMT
Content-Length:0

2026-06-22T14:21:29   [Verbose]   funccallmonitoring-control-03:  lease renewal with token  succeeded
2026-06-22T14:21:30   [Information]   Request [827966a0-f329-43d2-8251-0b33137c960b] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/locks/funccallmonitoring/host?comp=lease
x-ms-lease-action:renew
x-ms-lease-id:aa0b511e-7a56-1cdd-e9d7-33f1b19d7952
x-ms-version:2024-11-04
Accept:application/xml
x-ms-client-request-id:827966a0-f329-43d2-8251-0b33137c960b
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.22.1 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:30 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:30   [Information]   Response [827966a0-f329-43d2-8251-0b33137c960b] 200 OK (00.0s)
ETag:"0x8DECE2D7D1660EE"
x-ms-request-id:4d255cca-601e-0004-4952-02e6b8000000
x-ms-client-request-id:827966a0-f329-43d2-8251-0b33137c960b
x-ms-version:2024-11-04
x-ms-lease-id:aa0b511e-7a56-1cdd-e9d7-33f1b19d7952
Date:Mon, 22 Jun 2026 14:21:29 GMT
Content-Length:0
Last-Modified:Fri, 19 Jun 2026 18:06:30 GMT

2026-06-22T14:21:30   [Information]   Request [51eeb372-dac3-478e-b613-4ffe4b454b54] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/azure-webjobs-blobtrigger-funccallmonitoring/messages?numofmessages=9&visibilitytimeout=600
x-ms-version:2025-11-05
Accept:application/xml
x-ms-client-request-id:51eeb372-dac3-478e-b613-4ffe4b454b54
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:30 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:30   [Information]   Response [51eeb372-dac3-478e-b613-4ffe4b454b54] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8cdcb-a003-00d0-4f52-0256e9000000
x-ms-client-request-id:51eeb372-dac3-478e-b613-4ffe4b454b54
x-ms-version:2025-11-05
Date:Mon, 22 Jun 2026 14:21:29 GMT
Content-Type:application/xml

2026-06-22T14:21:30   [Verbose]   Poll for function 'blob_trigger_starter' on queue 'azure-webjobs-blobtrigger-funccallmonitoring' with ClientRequestId '51eeb372-dac3-478e-b613-4ffe4b454b54' found 0 messages in 4 ms.
2026-06-22T14:21:30   [Verbose]   Function 'blob_trigger_starter' will wait 10421.6675 ms before polling queue 'azure-webjobs-blobtrigger-funccallmonitoring'.
2026-06-22T14:21:33   [Verbose]   [HostMonitor] Checking worker statuses (Count=1)
2026-06-22T14:21:33   [Verbose]   [HostMonitor] Worker status: ID=788f0a3b-fad5-4de0-b3dd-9699fa2a79e5, Latency=1ms
2026-06-22T14:21:33   [Verbose]   [HostMonitor] Host process CPU stats (PID 52): History=(0,0,0,0,0), AvgCpuLoad=0, MaxCpuLoad=0
2026-06-22T14:21:33   [Verbose]   [HostMonitor] Host process CPU stats (PID 27): History=(2,1,3,2,1), AvgCpuLoad=2, MaxCpuLoad=3
2026-06-22T14:21:33   [Verbose]   [HostMonitor] Host aggregate CPU load 2
2026-06-22T14:21:33   [Information]   Executing StatusCodeResult, setting HTTP status code 200
2026-06-22T14:21:33   [Information]   Request [2b22992b-d011-4a61-be53-095f4dd75091] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:2b22992b-d011-4a61-be53-095f4dd75091
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:33 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:33   [Information]   Response [2b22992b-d011-4a61-be53-095f4dd75091] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8d02f-a003-00d0-7b52-0256e9000000
x-ms-client-request-id:2b22992b-d011-4a61-be53-095f4dd75091
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:32 GMT
Content-Type:application/xml

2026-06-22T14:21:34   [Information]   Request [cad15757-c2ab-4028-9465-0fb56e9bfa0a] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-workitems/messages?numofmessages=1&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:cad15757-c2ab-4028-9465-0fb56e9bfa0a
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:34 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:34   [Information]   Response [cad15757-c2ab-4028-9465-0fb56e9bfa0a] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8d12a-a003-00d0-4952-0256e9000000
x-ms-client-request-id:cad15757-c2ab-4028-9465-0fb56e9bfa0a
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:33 GMT
Content-Type:application/xml

2026-06-22T14:21:38   [Information]   Request [98049f1a-13a0-4564-aa45-d6aab27ed581] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1400&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:98049f1a-13a0-4564-aa45-d6aab27ed581
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:37 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:38   [Information]   Request [53eb8c43-a198-43c7-a8a9-7ba6b1035aa2] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs?restype=container&comp=list&marker=&maxresults=10000
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:53eb8c43-a198-43c7-a8a9-7ba6b1035aa2
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:37 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:38   [Information]   Response [98049f1a-13a0-4564-aa45-d6aab27ed581] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:5a23dcd1-901e-0000-1352-026bbf000000
x-ms-client-request-id:98049f1a-13a0-4564-aa45-d6aab27ed581
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:21:37 GMT
Content-Type:application/xml

2026-06-22T14:21:38   [Information]   Request [38a7de73-ef09-43fe-9cd3-09b655922505] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1300&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:38a7de73-ef09-43fe-9cd3-09b655922505
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:37 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:38   [Information]   Response [53eb8c43-a198-43c7-a8a9-7ba6b1035aa2] 200 OK (00.0s)
Transfer-Encoding:chunked
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23dfc7-f01e-0015-4352-0211a4000000
x-ms-client-request-id:53eb8c43-a198-43c7-a8a9-7ba6b1035aa2
x-ms-version:2026-02-06
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:21:37 GMT
Content-Type:application/xml

2026-06-22T14:21:38   [Verbose]   Poll for blobs newer than '2026-06-22T14:21:17.000Z' in container 'labhrdocs' with ClientRequestId '1f1ee97c-b2d8-4289-8b71-cc084e5ba881' found 1 blobs in 6 ms. ContinuationToken: False.
2026-06-22T14:21:38   [Information]   Request [b090efbd-e21f-457c-ad18-a732c98efd56] HEAD https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:b090efbd-e21f-457c-ad18-a732c98efd56
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:37 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:38   [Information]   Response [b090efbd-e21f-457c-ad18-a732c98efd56] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Vary:Origin
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23dfcf-f01e-0015-4952-0211a4000000
x-ms-client-request-id:b090efbd-e21f-457c-ad18-a732c98efd56
x-ms-version:2026-02-06
x-ms-tag-count:2
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:21:37 GMT
Content-Length:41837686
Content-Type:video/mp4
Content-MD5:FDGtsdzxt+wnqxE3hlFsqg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:38   [Information]   Request [a2f0224c-5c70-4df0-92e1-b97b67b17265] HEAD https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/blobreceipts/funccallmonitoring/Host.Functions.blob_trigger_starter/%220x8DED069863F6A51%22/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:a2f0224c-5c70-4df0-92e1-b97b67b17265
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:37 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:38   [Information]   Response [a2f0224c-5c70-4df0-92e1-b97b67b17265] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED06986690316"
x-ms-request-id:b3479a5f-301e-0036-0952-02e6cf000000
x-ms-client-request-id:a2f0224c-5c70-4df0-92e1-b97b67b17265
x-ms-version:2026-02-06
x-ms-tag-count:2
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:21:37 GMT
Content-Length:0
Content-Type:application/octet-stream
Content-MD5:1B2M2Y8AsgTpgAmY7PhCfg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:38   [Verbose]   Blob 'bb12.mp4' will be skipped for function 'blob_trigger_starter' because this blob with ETag '"0x8DED069863F6A51"' has already been processed. PollId: '1f1ee97c-b2d8-4289-8b71-cc084e5ba881'. Source: 'ContainerScan'.
2026-06-22T14:21:38   [Information]   Response [38a7de73-ef09-43fe-9cd3-09b655922505] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:5a23dcd5-901e-0000-1652-026bbf000000
x-ms-client-request-id:38a7de73-ef09-43fe-9cd3-09b655922505
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:21:37 GMT
Content-Type:application/xml

2026-06-22T14:21:38   [Information]   Request [47a6ff6b-c0b7-41ef-a979-e4ab5ce891c1] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-01/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:47a6ff6b-c0b7-41ef-a979-e4ab5ce891c1
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:38 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:38   [Information]   Response [47a6ff6b-c0b7-41ef-a979-e4ab5ce891c1] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8d64e-a003-00d0-0b52-0256e9000000
x-ms-client-request-id:47a6ff6b-c0b7-41ef-a979-e4ab5ce891c1
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:37 GMT
Content-Type:application/xml

2026-06-22T14:21:39   [Information]   Request [0b68a407-5f5d-4a0a-b80c-509631e25ae9] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-00/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:0b68a407-5f5d-4a0a-b80c-509631e25ae9
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:39 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:39   [Information]   Response [0b68a407-5f5d-4a0a-b80c-509631e25ae9] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8d6ee-a003-00d0-1f52-0256e9000000
x-ms-client-request-id:0b68a407-5f5d-4a0a-b80c-509631e25ae9
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:38 GMT
Content-Type:application/xml

2026-06-22T14:21:39   [Information]   Request [bf778124-a710-43e8-93a4-c22830a78a61] GET https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions()?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
Accept:application/json;odata=minimalmetadata
x-ms-client-request-id:bf778124-a710-43e8-93a4-c22830a78a61
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:39   [Information]   Response [bf778124-a710-43e8-93a4-c22830a78a61] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:16a68954-0002-00bb-6c52-02d11d000000
x-ms-client-request-id:bf778124-a710-43e8-93a4-c22830a78a61
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:39 GMT
Content-Type:application/json;odata=minimalmetadata;streaming=true;charset=utf-8

2026-06-22T14:21:39   [Information]   Request [6426406d-2529-483a-9f9a-bb9776f5b9a0] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-00')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A29.343172Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:6426406d-2529-483a-9f9a-bb9776f5b9a0
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:39   [Information]   Response [6426406d-2529-483a-9f9a-bb9776f5b9a0] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A39.3780972Z'"
x-ms-request-id:16a68955-0002-00bb-6d52-02d11d000000
x-ms-client-request-id:6426406d-2529-483a-9f9a-bb9776f5b9a0
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:39 GMT
Content-Length:0

2026-06-22T14:21:39   [Verbose]   funccallmonitoring-control-00:  lease renewal with token  succeeded
2026-06-22T14:21:39   [Information]   Request [19e25c13-f226-476e-b467-fb7791fa4ee0] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-01')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A29.3491619Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:19e25c13-f226-476e-b467-fb7791fa4ee0
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:39   [Information]   Response [19e25c13-f226-476e-b467-fb7791fa4ee0] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A39.3840879Z'"
x-ms-request-id:16a68956-0002-00bb-6e52-02d11d000000
x-ms-client-request-id:19e25c13-f226-476e-b467-fb7791fa4ee0
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:39 GMT
Content-Length:0

2026-06-22T14:21:39   [Verbose]   funccallmonitoring-control-01:  lease renewal with token  succeeded
2026-06-22T14:21:39   [Information]   Request [1b61a7fc-7b7b-48bd-86f9-db79a490d9b3] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-02')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A29.3561507Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:1b61a7fc-7b7b-48bd-86f9-db79a490d9b3
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:39   [Information]   Response [1b61a7fc-7b7b-48bd-86f9-db79a490d9b3] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A39.3900786Z'"
x-ms-request-id:16a68957-0002-00bb-6f52-02d11d000000
x-ms-client-request-id:1b61a7fc-7b7b-48bd-86f9-db79a490d9b3
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:39 GMT
Content-Length:0

2026-06-22T14:21:39   [Verbose]   funccallmonitoring-control-02:  lease renewal with token  succeeded
2026-06-22T14:21:39   [Information]   Request [37592f08-d80a-4cef-bce6-2a66ae45a161] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-03')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A29.3621431Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:37592f08-d80a-4cef-bce6-2a66ae45a161
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:39   [Information]   Response [37592f08-d80a-4cef-bce6-2a66ae45a161] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A39.3970667Z'"
x-ms-request-id:16a68958-0002-00bb-7052-02d11d000000
x-ms-client-request-id:37592f08-d80a-4cef-bce6-2a66ae45a161
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:39 GMT
Content-Length:0

2026-06-22T14:21:39   [Verbose]   funccallmonitoring-control-03:  lease renewal with token  succeeded
2026-06-22T14:21:41   [Information]   Request [1d3c9774-f658-48a9-8ede-7818b096c00f] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/azure-webjobs-blobtrigger-funccallmonitoring/messages?numofmessages=9&visibilitytimeout=600
x-ms-version:2025-11-05
Accept:application/xml
x-ms-client-request-id:1d3c9774-f658-48a9-8ede-7818b096c00f
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:40 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:41   [Information]   Response [1d3c9774-f658-48a9-8ede-7818b096c00f] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8d82f-a003-00d0-4852-0256e9000000
x-ms-client-request-id:1d3c9774-f658-48a9-8ede-7818b096c00f
x-ms-version:2025-11-05
Date:Mon, 22 Jun 2026 14:21:40 GMT
Content-Type:application/xml

2026-06-22T14:21:41   [Verbose]   Poll for function 'blob_trigger_starter' on queue 'azure-webjobs-blobtrigger-funccallmonitoring' with ClientRequestId '1d3c9774-f658-48a9-8ede-7818b096c00f' found 0 messages in 4 ms.
2026-06-22T14:21:41   [Verbose]   Function 'blob_trigger_starter' will wait 30150.8284 ms before polling queue 'azure-webjobs-blobtrigger-funccallmonitoring'.
2026-06-22T14:21:42   [Information]   Request [534632d0-4ca9-4332-acd7-507720bcf125] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/locks/funccallmonitoring/host?comp=lease
x-ms-lease-action:renew
x-ms-lease-id:aa0b511e-7a56-1cdd-e9d7-33f1b19d7952
x-ms-version:2024-11-04
Accept:application/xml
x-ms-client-request-id:534632d0-4ca9-4332-acd7-507720bcf125
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.22.1 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:42 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:42   [Information]   Response [534632d0-4ca9-4332-acd7-507720bcf125] 200 OK (00.0s)
ETag:"0x8DECE2D7D1660EE"
x-ms-request-id:4d257bfd-601e-0004-3052-02e6b8000000
x-ms-client-request-id:534632d0-4ca9-4332-acd7-507720bcf125
x-ms-version:2024-11-04
x-ms-lease-id:aa0b511e-7a56-1cdd-e9d7-33f1b19d7952
Date:Mon, 22 Jun 2026 14:21:41 GMT
Content-Length:0
Last-Modified:Fri, 19 Jun 2026 18:06:30 GMT

2026-06-22T14:21:43   [Verbose]   [HostMonitor] Checking worker statuses (Count=1)
2026-06-22T14:21:43   [Verbose]   [HostMonitor] Worker status: ID=788f0a3b-fad5-4de0-b3dd-9699fa2a79e5, Latency=1ms
2026-06-22T14:21:43   [Verbose]   [HostMonitor] Host process CPU stats (PID 52): History=(0,0,0,0,0), AvgCpuLoad=0, MaxCpuLoad=0
2026-06-22T14:21:43   [Verbose]   [HostMonitor] Host process CPU stats (PID 27): History=(2,1,2,2,1), AvgCpuLoad=2, MaxCpuLoad=2
2026-06-22T14:21:43   [Verbose]   [HostMonitor] Host aggregate CPU load 2
2026-06-22T14:21:43   [Information]   Executing StatusCodeResult, setting HTTP status code 200
2026-06-22T14:21:44   [Verbose]   funccallmonitoring-applease: Starting app lease renewal with token 3320c211-0000-0000-0000-000000000000
2026-06-22T14:21:44   [Information]   Request [f00e83cf-2483-428c-97c0-371d5b144a9e] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/funccallmonitoring-applease?comp=lease&restype=container
x-ms-lease-action:renew
x-ms-lease-id:3320c211-0000-0000-0000-000000000000
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:f00e83cf-2483-428c-97c0-371d5b144a9e
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:43 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:44   [Information]   Response [f00e83cf-2483-428c-97c0-371d5b144a9e] 200 OK (00.0s)
ETag:"0x8DECE10DD3DE605"
x-ms-request-id:5a23ef7f-901e-0000-7752-026bbf000000
x-ms-client-request-id:f00e83cf-2483-428c-97c0-371d5b144a9e
x-ms-version:2026-02-06
x-ms-lease-id:3320c211-0000-0000-0000-000000000000
Date:Mon, 22 Jun 2026 14:21:43 GMT
Content-Length:0
Last-Modified:Fri, 19 Jun 2026 14:41:35 GMT

2026-06-22T14:21:44   [Verbose]   funccallmonitoring-applease: app lease renewal with token 3320c211-0000-0000-0000-000000000000 succeeded
2026-06-22T14:21:45   [Information]   Request [02e8b444-3dfd-45f5-9227-92085389b887] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:02e8b444-3dfd-45f5-9227-92085389b887
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:45 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:45   [Information]   Response [02e8b444-3dfd-45f5-9227-92085389b887] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8dde2-a003-00d0-0a52-0256e9000000
x-ms-client-request-id:02e8b444-3dfd-45f5-9227-92085389b887
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:44 GMT
Content-Type:application/xml

2026-06-22T14:21:46   [Information]   Request [b34a5fdf-3168-4b80-acf9-c103a3d1803a] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-workitems/messages?numofmessages=1&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:b34a5fdf-3168-4b80-acf9-c103a3d1803a
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:46 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:46   [Information]   Response [b34a5fdf-3168-4b80-acf9-c103a3d1803a] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8def1-a003-00d0-0152-0256e9000000
x-ms-client-request-id:b34a5fdf-3168-4b80-acf9-c103a3d1803a
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:45 GMT
Content-Type:application/xml

2026-06-22T14:21:48   [Information]   Request [b09f9970-b509-4057-a045-c81f72cdfa9c] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1400&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:b09f9970-b509-4057-a045-c81f72cdfa9c
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:47 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:48   [Information]   Request [dccde1e2-9815-4af4-b970-f6ea16d67157] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs?restype=container&comp=list&marker=&maxresults=10000
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:dccde1e2-9815-4af4-b970-f6ea16d67157
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:47 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:48   [Information]   Response [b09f9970-b509-4057-a045-c81f72cdfa9c] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:5a23fa18-901e-0000-1a52-026bbf000000
x-ms-client-request-id:b09f9970-b509-4057-a045-c81f72cdfa9c
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:21:47 GMT
Content-Type:application/xml

2026-06-22T14:21:48   [Information]   Response [dccde1e2-9815-4af4-b970-f6ea16d67157] 200 OK (00.0s)
Transfer-Encoding:chunked
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23ea6e-f01e-0015-2352-0211a4000000
x-ms-client-request-id:dccde1e2-9815-4af4-b970-f6ea16d67157
x-ms-version:2026-02-06
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:21:47 GMT
Content-Type:application/xml

2026-06-22T14:21:48   [Verbose]   Poll for blobs newer than '2026-06-22T14:21:17.000Z' in container 'labhrdocs' with ClientRequestId '0d4f4f6d-f841-48c9-9753-f324c5799ee2' found 1 blobs in 4 ms. ContinuationToken: False.
2026-06-22T14:21:48   [Information]   Request [b7345e86-edb5-48e1-8c7b-274e14367220] HEAD https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:b7345e86-edb5-48e1-8c7b-274e14367220
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:47 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:48   [Information]   Request [48f2f153-c1ea-4c1c-894e-6ca757a743c3] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1300&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:48f2f153-c1ea-4c1c-894e-6ca757a743c3
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:47 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:48   [Information]   Response [b7345e86-edb5-48e1-8c7b-274e14367220] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Vary:Origin
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23ea72-f01e-0015-2552-0211a4000000
x-ms-client-request-id:b7345e86-edb5-48e1-8c7b-274e14367220
x-ms-version:2026-02-06
x-ms-tag-count:2
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:21:47 GMT
Content-Length:41837686
Content-Type:video/mp4
Content-MD5:FDGtsdzxt+wnqxE3hlFsqg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:48   [Information]   Request [a03fa48d-72d6-4c42-b6e1-b226fab76b98] HEAD https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/blobreceipts/funccallmonitoring/Host.Functions.blob_trigger_starter/%220x8DED069863F6A51%22/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:a03fa48d-72d6-4c42-b6e1-b226fab76b98
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:47 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:48   [Information]   Response [a03fa48d-72d6-4c42-b6e1-b226fab76b98] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED06986690316"
x-ms-request-id:b347b8d1-301e-0036-1952-02e6cf000000
x-ms-client-request-id:a03fa48d-72d6-4c42-b6e1-b226fab76b98
x-ms-version:2026-02-06
x-ms-tag-count:2
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:21:47 GMT
Content-Length:0
Content-Type:application/octet-stream
Content-MD5:1B2M2Y8AsgTpgAmY7PhCfg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:48   [Verbose]   Blob 'bb12.mp4' will be skipped for function 'blob_trigger_starter' because this blob with ETag '"0x8DED069863F6A51"' has already been processed. PollId: '0d4f4f6d-f841-48c9-9753-f324c5799ee2'. Source: 'ContainerScan'.
2026-06-22T14:21:48   [Information]   Response [48f2f153-c1ea-4c1c-894e-6ca757a743c3] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:5a23fa1f-901e-0000-1e52-026bbf000000
x-ms-client-request-id:48f2f153-c1ea-4c1c-894e-6ca757a743c3
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:21:47 GMT
Content-Type:application/xml

2026-06-22T14:21:49   [Information]   Request [963f0db6-0e0e-4bbc-9fba-ddafcaafb149] GET https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions()?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
Accept:application/json;odata=minimalmetadata
x-ms-client-request-id:963f0db6-0e0e-4bbc-9fba-ddafcaafb149
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:49   [Information]   Response [963f0db6-0e0e-4bbc-9fba-ddafcaafb149] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:16a68b01-0002-00bb-4052-02d11d000000
x-ms-client-request-id:963f0db6-0e0e-4bbc-9fba-ddafcaafb149
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:49 GMT
Content-Type:application/json;odata=minimalmetadata;streaming=true;charset=utf-8

2026-06-22T14:21:49   [Information]   Request [7a330db8-8c59-4e8d-b885-e14f61d5fd42] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-00')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A39.3780972Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:7a330db8-8c59-4e8d-b885-e14f61d5fd42
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:49   [Information]   Response [7a330db8-8c59-4e8d-b885-e14f61d5fd42] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A49.4070267Z'"
x-ms-request-id:16a68b04-0002-00bb-4152-02d11d000000
x-ms-client-request-id:7a330db8-8c59-4e8d-b885-e14f61d5fd42
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:49 GMT
Content-Length:0

2026-06-22T14:21:49   [Verbose]   funccallmonitoring-control-00:  lease renewal with token  succeeded
2026-06-22T14:21:49   [Information]   Request [c5478210-362f-488a-b896-3333d8a45ffc] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-01')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A39.3840879Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:c5478210-362f-488a-b896-3333d8a45ffc
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:49   [Information]   Response [c5478210-362f-488a-b896-3333d8a45ffc] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A49.4130172Z'"
x-ms-request-id:16a68b05-0002-00bb-4252-02d11d000000
x-ms-client-request-id:c5478210-362f-488a-b896-3333d8a45ffc
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:49 GMT
Content-Length:0

2026-06-22T14:21:49   [Verbose]   funccallmonitoring-control-01:  lease renewal with token  succeeded
2026-06-22T14:21:49   [Information]   Request [a9b05e81-606e-4a04-95bd-7dc572e213ef] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-02')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A39.3900786Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:a9b05e81-606e-4a04-95bd-7dc572e213ef
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:49   [Information]   Response [a9b05e81-606e-4a04-95bd-7dc572e213ef] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A49.4210042Z'"
x-ms-request-id:16a68b07-0002-00bb-4452-02d11d000000
x-ms-client-request-id:a9b05e81-606e-4a04-95bd-7dc572e213ef
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:49 GMT
Content-Length:0

2026-06-22T14:21:49   [Verbose]   funccallmonitoring-control-02:  lease renewal with token  succeeded
2026-06-22T14:21:49   [Information]   Request [dc9d2c25-8698-460d-b0f5-fab2ab54b224] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-03')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A39.3970667Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:dc9d2c25-8698-460d-b0f5-fab2ab54b224
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:49   [Information]   Response [dc9d2c25-8698-460d-b0f5-fab2ab54b224] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A49.4259963Z'"
x-ms-request-id:16a68b09-0002-00bb-4552-02d11d000000
x-ms-client-request-id:dc9d2c25-8698-460d-b0f5-fab2ab54b224
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:49 GMT
Content-Length:0

2026-06-22T14:21:49   [Verbose]   funccallmonitoring-control-03:  lease renewal with token  succeeded
2026-06-22T14:21:53   [Verbose]   [HostMonitor] Checking worker statuses (Count=1)
2026-06-22T14:21:53   [Verbose]   [HostMonitor] Worker status: ID=788f0a3b-fad5-4de0-b3dd-9699fa2a79e5, Latency=1ms
2026-06-22T14:21:53   [Verbose]   [HostMonitor] Host process CPU stats (PID 52): History=(0,1,0,1,0), AvgCpuLoad=0.4, MaxCpuLoad=1
2026-06-22T14:21:53   [Verbose]   [HostMonitor] Host process CPU stats (PID 27): History=(1,2,1,1,1), AvgCpuLoad=1, MaxCpuLoad=2
2026-06-22T14:21:53   [Verbose]   [HostMonitor] Host aggregate CPU load 2
2026-06-22T14:21:53   [Information]   Executing StatusCodeResult, setting HTTP status code 200
2026-06-22T14:21:54   [Information]   Request [98f16330-356d-49b4-8507-38df505bac07] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/locks/funccallmonitoring/host?comp=lease
x-ms-lease-action:renew
x-ms-lease-id:aa0b511e-7a56-1cdd-e9d7-33f1b19d7952
x-ms-version:2024-11-04
Accept:application/xml
x-ms-client-request-id:98f16330-356d-49b4-8507-38df505bac07
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.22.1 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:54 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:54   [Information]   Response [98f16330-356d-49b4-8507-38df505bac07] 200 OK (00.0s)
ETag:"0x8DECE2D7D1660EE"
x-ms-request-id:4d25964f-601e-0004-4352-02e6b8000000
x-ms-client-request-id:98f16330-356d-49b4-8507-38df505bac07
x-ms-version:2024-11-04
x-ms-lease-id:aa0b511e-7a56-1cdd-e9d7-33f1b19d7952
Date:Mon, 22 Jun 2026 14:21:53 GMT
Content-Length:0
Last-Modified:Fri, 19 Jun 2026 18:06:30 GMT

2026-06-22T14:21:54   [Verbose]   There are currently 0 orchestration(s) and 0 activities loaded into memory on this worker
2026-06-22T14:21:56   [Information]   Request [f0c0c60a-2208-4f7d-933f-b3267ccdc7cc] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/locks/funccallmonitoring/WebJobs.Internal.Blobs.Listener?comp=lease
x-ms-lease-action:renew
x-ms-lease-id:a91e3446-f57f-4eda-b6bf-2d5455b5d031
x-ms-version:2024-11-04
Accept:application/xml
x-ms-client-request-id:f0c0c60a-2208-4f7d-933f-b3267ccdc7cc
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.22.1 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:56 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:56   [Information]   Request [fe5f76c6-0c64-4ae6-b04d-ae765b3b4cda] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/?comp=list&maxresults=1
x-ms-version:2024-11-04
Accept:application/xml
x-ms-client-request-id:fe5f76c6-0c64-4ae6-b04d-ae765b3b4cda
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.22.1 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:56 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:56   [Information]   Response [f0c0c60a-2208-4f7d-933f-b3267ccdc7cc] 200 OK (00.0s)
ETag:"0x8DECE1769D6FB81"
x-ms-request-id:4d259a5d-601e-0004-0952-02e6b8000000
x-ms-client-request-id:f0c0c60a-2208-4f7d-933f-b3267ccdc7cc
x-ms-version:2024-11-04
x-ms-lease-id:a91e3446-f57f-4eda-b6bf-2d5455b5d031
Date:Mon, 22 Jun 2026 14:21:55 GMT
Content-Length:0
Last-Modified:Fri, 19 Jun 2026 15:28:28 GMT

2026-06-22T14:21:56   [Information]   Response [fe5f76c6-0c64-4ae6-b04d-ae765b3b4cda] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:665a5e0c-c01e-00d6-0752-026556000000
x-ms-client-request-id:fe5f76c6-0c64-4ae6-b04d-ae765b3b4cda
x-ms-version:2024-11-04
Date:Mon, 22 Jun 2026 14:21:55 GMT
Content-Type:application/xml

2026-06-22T14:21:58   [Information]   Request [132a6ae4-9d59-4c8c-83c9-8199b0ac9cb4] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1400&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:132a6ae4-9d59-4c8c-83c9-8199b0ac9cb4
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:57 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:58   [Information]   Request [e713f5c5-487d-498a-abaa-453af231bbd0] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs?restype=container&comp=list&marker=&maxresults=10000
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:e713f5c5-487d-498a-abaa-453af231bbd0
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:57 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:58   [Information]   Response [132a6ae4-9d59-4c8c-83c9-8199b0ac9cb4] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:5a2417d8-901e-0000-0f52-026bbf000000
x-ms-client-request-id:132a6ae4-9d59-4c8c-83c9-8199b0ac9cb4
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:21:57 GMT
Content-Type:application/xml

2026-06-22T14:21:58   [Information]   Response [e713f5c5-487d-498a-abaa-453af231bbd0] 200 OK (00.0s)
Transfer-Encoding:chunked
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23f48e-f01e-0015-6352-0211a4000000
x-ms-client-request-id:e713f5c5-487d-498a-abaa-453af231bbd0
x-ms-version:2026-02-06
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:21:57 GMT
Content-Type:application/xml

2026-06-22T14:21:58   [Verbose]   Poll for blobs newer than '2026-06-22T14:21:17.000Z' in container 'labhrdocs' with ClientRequestId '91cb7f78-54c8-4af1-bcf6-6ae2391fb075' found 1 blobs in 4 ms. ContinuationToken: False.
2026-06-22T14:21:58   [Information]   Request [aeb6ef50-8459-4e3f-8707-5f31528af39f] HEAD https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:aeb6ef50-8459-4e3f-8707-5f31528af39f
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:57 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:58   [Information]   Request [1bb927bf-fcb2-4427-9c08-c089804dbe99] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1300&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:1bb927bf-fcb2-4427-9c08-c089804dbe99
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:57 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:58   [Information]   Response [aeb6ef50-8459-4e3f-8707-5f31528af39f] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Vary:Origin
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c23f493-f01e-0015-6752-0211a4000000
x-ms-client-request-id:aeb6ef50-8459-4e3f-8707-5f31528af39f
x-ms-version:2026-02-06
x-ms-tag-count:2
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:21:57 GMT
Content-Length:41837686
Content-Type:video/mp4
Content-MD5:FDGtsdzxt+wnqxE3hlFsqg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:58   [Information]   Request [72f00222-c6fb-450e-89f2-f1eba388b5ee] HEAD https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/blobreceipts/funccallmonitoring/Host.Functions.blob_trigger_starter/%220x8DED069863F6A51%22/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:72f00222-c6fb-450e-89f2-f1eba388b5ee
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:57 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:21:58   [Information]   Response [72f00222-c6fb-450e-89f2-f1eba388b5ee] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED06986690316"
x-ms-request-id:b347d30f-301e-0036-1f52-02e6cf000000
x-ms-client-request-id:72f00222-c6fb-450e-89f2-f1eba388b5ee
x-ms-version:2026-02-06
x-ms-tag-count:2
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:21:57 GMT
Content-Length:0
Content-Type:application/octet-stream
Content-MD5:1B2M2Y8AsgTpgAmY7PhCfg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:21:58   [Verbose]   Blob 'bb12.mp4' will be skipped for function 'blob_trigger_starter' because this blob with ETag '"0x8DED069863F6A51"' has already been processed. PollId: '91cb7f78-54c8-4af1-bcf6-6ae2391fb075'. Source: 'ContainerScan'.
2026-06-22T14:21:58   [Information]   Response [1bb927bf-fcb2-4427-9c08-c089804dbe99] 200 OK (00.1s)
Transfer-Encoding:chunked
x-ms-request-id:5a2417de-901e-0000-1452-026bbf000000
x-ms-client-request-id:1bb927bf-fcb2-4427-9c08-c089804dbe99
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:21:57 GMT
Content-Type:application/xml

2026-06-22T14:21:58   [Information]   Request [05dbe066-b977-4388-9c01-937407d81ea2] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-02/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:05dbe066-b977-4388-9c01-937407d81ea2
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:21:58 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:21:58   [Information]   Response [05dbe066-b977-4388-9c01-937407d81ea2] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8e9cc-a003-00d0-0a52-0256e9000000
x-ms-client-request-id:05dbe066-b977-4388-9c01-937407d81ea2
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:21:58 GMT
Content-Type:application/xml

2026-06-22T14:21:59   [Information]   Request [71691bd1-aa58-422a-afac-b62781c8f872] GET https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions()?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
Accept:application/json;odata=minimalmetadata
x-ms-client-request-id:71691bd1-aa58-422a-afac-b62781c8f872
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:59   [Information]   Response [71691bd1-aa58-422a-afac-b62781c8f872] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:16a68c2c-0002-00bb-1752-02d11d000000
x-ms-client-request-id:71691bd1-aa58-422a-afac-b62781c8f872
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:59 GMT
Content-Type:application/json;odata=minimalmetadata;streaming=true;charset=utf-8

2026-06-22T14:21:59   [Information]   Request [db31e86c-fb89-46d0-af3e-9646c0292173] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-00')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A49.4070267Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:db31e86c-fb89-46d0-af3e-9646c0292173
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:59   [Information]   Response [db31e86c-fb89-46d0-af3e-9646c0292173] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A59.4449436Z'"
x-ms-request-id:16a68c2d-0002-00bb-1852-02d11d000000
x-ms-client-request-id:db31e86c-fb89-46d0-af3e-9646c0292173
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:59 GMT
Content-Length:0

2026-06-22T14:21:59   [Verbose]   funccallmonitoring-control-00:  lease renewal with token  succeeded
2026-06-22T14:21:59   [Information]   Request [b557ac3a-fb6e-45c6-a228-17e4bc25a1fc] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-01')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A49.4130172Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:b557ac3a-fb6e-45c6-a228-17e4bc25a1fc
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:59   [Information]   Response [b557ac3a-fb6e-45c6-a228-17e4bc25a1fc] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A59.4509345Z'"
x-ms-request-id:16a68c2e-0002-00bb-1952-02d11d000000
x-ms-client-request-id:b557ac3a-fb6e-45c6-a228-17e4bc25a1fc
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:59 GMT
Content-Length:0

2026-06-22T14:21:59   [Verbose]   funccallmonitoring-control-01:  lease renewal with token  succeeded
2026-06-22T14:21:59   [Information]   Request [cb008d3b-70bc-4044-bc6b-728a444d6896] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-02')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A49.4210042Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:cb008d3b-70bc-4044-bc6b-728a444d6896
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:59   [Information]   Response [cb008d3b-70bc-4044-bc6b-728a444d6896] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A59.4569249Z'"
x-ms-request-id:16a68c31-0002-00bb-1b52-02d11d000000
x-ms-client-request-id:cb008d3b-70bc-4044-bc6b-728a444d6896
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:59 GMT
Content-Length:0

2026-06-22T14:21:59   [Verbose]   funccallmonitoring-control-02:  lease renewal with token  succeeded
2026-06-22T14:21:59   [Information]   Request [01b2659b-b16f-47d6-a523-99eb48fd771b] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-03')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A49.4259963Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:01b2659b-b16f-47d6-a523-99eb48fd771b
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:21:59   [Information]   Response [01b2659b-b16f-47d6-a523-99eb48fd771b] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A21%3A59.4629155Z'"
x-ms-request-id:16a68c34-0002-00bb-1d52-02d11d000000
x-ms-client-request-id:01b2659b-b16f-47d6-a523-99eb48fd771b
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:21:59 GMT
Content-Length:0

2026-06-22T14:21:59   [Verbose]   funccallmonitoring-control-03:  lease renewal with token  succeeded
2026-06-22T14:22:04   [Verbose]   [HostMonitor] Checking worker statuses (Count=1)
2026-06-22T14:22:04   [Verbose]   [HostMonitor] Worker status: ID=788f0a3b-fad5-4de0-b3dd-9699fa2a79e5, Latency=1ms
2026-06-22T14:22:04   [Verbose]   [HostMonitor] Host process CPU stats (PID 52): History=(0,0,1,0,0), AvgCpuLoad=0.2, MaxCpuLoad=1
2026-06-22T14:22:04   [Verbose]   [HostMonitor] Host process CPU stats (PID 27): History=(2,1,2,1,1), AvgCpuLoad=1, MaxCpuLoad=2
2026-06-22T14:22:04   [Verbose]   [HostMonitor] Host aggregate CPU load 2
2026-06-22T14:22:04   [Information]   Executing StatusCodeResult, setting HTTP status code 200
2026-06-22T14:22:06   [Information]   Request [4ae01331-0a06-475a-8ba7-b9f836e4ce0a] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/locks/funccallmonitoring/host?comp=lease
x-ms-lease-action:renew
x-ms-lease-id:aa0b511e-7a56-1cdd-e9d7-33f1b19d7952
x-ms-version:2024-11-04
Accept:application/xml
x-ms-client-request-id:4ae01331-0a06-475a-8ba7-b9f836e4ce0a
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.22.1 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:06 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:06   [Information]   Response [4ae01331-0a06-475a-8ba7-b9f836e4ce0a] 200 OK (00.0s)
ETag:"0x8DECE2D7D1660EE"
x-ms-request-id:665a7004-c01e-00d6-5752-026556000000
x-ms-client-request-id:4ae01331-0a06-475a-8ba7-b9f836e4ce0a
x-ms-version:2024-11-04
x-ms-lease-id:aa0b511e-7a56-1cdd-e9d7-33f1b19d7952
Date:Mon, 22 Jun 2026 14:22:05 GMT
Content-Length:0
Last-Modified:Fri, 19 Jun 2026 18:06:30 GMT

2026-06-22T14:22:07   [Information]   Request [62bac175-810c-4ff2-b163-c516bfa2a247] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-workitems/messages?numofmessages=1&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:62bac175-810c-4ff2-b163-c516bfa2a247
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:06 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:22:07   [Information]   Response [62bac175-810c-4ff2-b163-c516bfa2a247] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8f286-a003-00d0-3952-0256e9000000
x-ms-client-request-id:62bac175-810c-4ff2-b163-c516bfa2a247
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:22:06 GMT
Content-Type:application/xml

2026-06-22T14:22:08   [Information]   Request [b6d14ca1-fe57-43a0-beb5-0e834c567843] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1400&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:b6d14ca1-fe57-43a0-beb5-0e834c567843
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:08 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:08   [Information]   Request [1f9ba084-6392-48d3-a069-33be18b3c3ec] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs?restype=container&comp=list&marker=&maxresults=10000
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:1f9ba084-6392-48d3-a069-33be18b3c3ec
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:08 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:08   [Information]   Response [b6d14ca1-fe57-43a0-beb5-0e834c567843] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:5a24329a-901e-0000-5252-026bbf000000
x-ms-client-request-id:b6d14ca1-fe57-43a0-beb5-0e834c567843
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:22:07 GMT
Content-Type:application/xml

2026-06-22T14:22:08   [Information]   Request [cd202d5a-d1ef-406d-b86d-1eab58fc7bc0] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1300&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:cd202d5a-d1ef-406d-b86d-1eab58fc7bc0
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:08 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:08   [Information]   Response [1f9ba084-6392-48d3-a069-33be18b3c3ec] 200 OK (00.0s)
Transfer-Encoding:chunked
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c240031-f01e-0015-0852-0211a4000000
x-ms-client-request-id:1f9ba084-6392-48d3-a069-33be18b3c3ec
x-ms-version:2026-02-06
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:22:07 GMT
Content-Type:application/xml

2026-06-22T14:22:08   [Verbose]   Poll for blobs newer than '2026-06-22T14:21:17.000Z' in container 'labhrdocs' with ClientRequestId 'c036f6bc-94fc-46f6-8eb1-29002c36a7fe' found 1 blobs in 10 ms. ContinuationToken: False.
2026-06-22T14:22:08   [Information]   Request [75bd5657-8250-4cf3-9a85-6d932b43085a] HEAD https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:75bd5657-8250-4cf3-9a85-6d932b43085a
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:08 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:08   [Information]   Response [75bd5657-8250-4cf3-9a85-6d932b43085a] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Vary:Origin
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c240038-f01e-0015-0d52-0211a4000000
x-ms-client-request-id:75bd5657-8250-4cf3-9a85-6d932b43085a
x-ms-version:2026-02-06
x-ms-tag-count:2
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:22:07 GMT
Content-Length:41837686
Content-Type:video/mp4
Content-MD5:FDGtsdzxt+wnqxE3hlFsqg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:22:08   [Information]   Request [55a41563-f34a-4b5a-acd2-a4028f4018f4] HEAD https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/blobreceipts/funccallmonitoring/Host.Functions.blob_trigger_starter/%220x8DED069863F6A51%22/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:55a41563-f34a-4b5a-acd2-a4028f4018f4
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:08 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:08   [Information]   Response [55a41563-f34a-4b5a-acd2-a4028f4018f4] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED06986690316"
x-ms-request-id:b347ec87-301e-0036-8052-02e6cf000000
x-ms-client-request-id:55a41563-f34a-4b5a-acd2-a4028f4018f4
x-ms-version:2026-02-06
x-ms-tag-count:2
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:22:07 GMT
Content-Length:0
Content-Type:application/octet-stream
Content-MD5:1B2M2Y8AsgTpgAmY7PhCfg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:22:08   [Verbose]   Blob 'bb12.mp4' will be skipped for function 'blob_trigger_starter' because this blob with ETag '"0x8DED069863F6A51"' has already been processed. PollId: 'c036f6bc-94fc-46f6-8eb1-29002c36a7fe'. Source: 'ContainerScan'.
2026-06-22T14:22:08   [Information]   Response [cd202d5a-d1ef-406d-b86d-1eab58fc7bc0] 200 OK (00.1s)
Transfer-Encoding:chunked
x-ms-request-id:5a2432a1-901e-0000-5652-026bbf000000
x-ms-client-request-id:cd202d5a-d1ef-406d-b86d-1eab58fc7bc0
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:22:07 GMT
Content-Type:application/xml

2026-06-22T14:22:08   [Information]   Request [622bd3a9-209a-4a80-99a1-7651acfe8acb] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-01/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:622bd3a9-209a-4a80-99a1-7651acfe8acb
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:08 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:22:08   [Information]   Response [622bd3a9-209a-4a80-99a1-7651acfe8acb] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8f40c-a003-00d0-2f52-0256e9000000
x-ms-client-request-id:622bd3a9-209a-4a80-99a1-7651acfe8acb
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:22:07 GMT
Content-Type:application/xml

2026-06-22T14:22:09   [Verbose]   funccallmonitoring-applease: Starting app lease renewal with token 3320c211-0000-0000-0000-000000000000
2026-06-22T14:22:09   [Information]   Request [f7fc818b-a6d8-48d0-89c7-de774bc3fd43] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/funccallmonitoring-applease?comp=lease&restype=container
x-ms-lease-action:renew
x-ms-lease-id:3320c211-0000-0000-0000-000000000000
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:f7fc818b-a6d8-48d0-89c7-de774bc3fd43
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:08 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:09   [Information]   Response [f7fc818b-a6d8-48d0-89c7-de774bc3fd43] 200 OK (00.0s)
ETag:"0x8DECE10DD3DE605"
x-ms-request-id:5a24348b-901e-0000-7252-026bbf000000
x-ms-client-request-id:f7fc818b-a6d8-48d0-89c7-de774bc3fd43
x-ms-version:2026-02-06
x-ms-lease-id:3320c211-0000-0000-0000-000000000000
Date:Mon, 22 Jun 2026 14:22:08 GMT
Content-Length:0
Last-Modified:Fri, 19 Jun 2026 14:41:35 GMT

2026-06-22T14:22:09   [Verbose]   funccallmonitoring-applease: app lease renewal with token 3320c211-0000-0000-0000-000000000000 succeeded
2026-06-22T14:22:09   [Information]   Request [d8ec3712-4544-4b55-9c87-2fed75758ab0] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-00/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:d8ec3712-4544-4b55-9c87-2fed75758ab0
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:09 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:22:09   [Information]   Response [d8ec3712-4544-4b55-9c87-2fed75758ab0] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8f4d2-a003-00d0-6a52-0256e9000000
x-ms-client-request-id:d8ec3712-4544-4b55-9c87-2fed75758ab0
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:22:08 GMT
Content-Type:application/xml

2026-06-22T14:22:09   [Information]   Request [ca73909a-43de-4c28-9e2d-d51c845e665c] GET https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions()?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
Accept:application/json;odata=minimalmetadata
x-ms-client-request-id:ca73909a-43de-4c28-9e2d-d51c845e665c
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:09   [Information]   Response [ca73909a-43de-4c28-9e2d-d51c845e665c] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:16a68da7-0002-00bb-3452-02d11d000000
x-ms-client-request-id:ca73909a-43de-4c28-9e2d-d51c845e665c
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:09 GMT
Content-Type:application/json;odata=minimalmetadata;streaming=true;charset=utf-8

2026-06-22T14:22:09   [Information]   Request [cccca6df-17ed-4c97-9b0b-69349bf061fa] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-00')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A59.4449436Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:cccca6df-17ed-4c97-9b0b-69349bf061fa
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:09   [Information]   Response [cccca6df-17ed-4c97-9b0b-69349bf061fa] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A22%3A09.4788696Z'"
x-ms-request-id:16a68daa-0002-00bb-3552-02d11d000000
x-ms-client-request-id:cccca6df-17ed-4c97-9b0b-69349bf061fa
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:09 GMT
Content-Length:0

2026-06-22T14:22:09   [Verbose]   funccallmonitoring-control-00:  lease renewal with token  succeeded
2026-06-22T14:22:09   [Information]   Request [9b352f4c-e46b-40c4-a40a-a51368ac31ac] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-01')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A59.4509345Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:9b352f4c-e46b-40c4-a40a-a51368ac31ac
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:09   [Information]   Response [9b352f4c-e46b-40c4-a40a-a51368ac31ac] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A22%3A09.4858585Z'"
x-ms-request-id:16a68dad-0002-00bb-3852-02d11d000000
x-ms-client-request-id:9b352f4c-e46b-40c4-a40a-a51368ac31ac
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:09 GMT
Content-Length:0

2026-06-22T14:22:09   [Verbose]   funccallmonitoring-control-01:  lease renewal with token  succeeded
2026-06-22T14:22:09   [Information]   Request [3c7cb92c-551f-44b1-bb21-be6ac0f3eb91] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-02')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A59.4569249Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:3c7cb92c-551f-44b1-bb21-be6ac0f3eb91
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:09   [Information]   Response [3c7cb92c-551f-44b1-bb21-be6ac0f3eb91] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A22%3A09.4918488Z'"
x-ms-request-id:16a68db0-0002-00bb-3a52-02d11d000000
x-ms-client-request-id:3c7cb92c-551f-44b1-bb21-be6ac0f3eb91
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:09 GMT
Content-Length:0

2026-06-22T14:22:09   [Verbose]   funccallmonitoring-control-02:  lease renewal with token  succeeded
2026-06-22T14:22:09   [Information]   Request [facae84e-1b07-4f28-bac4-5173f4ec5a7b] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-03')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A21%3A59.4629155Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:facae84e-1b07-4f28-bac4-5173f4ec5a7b
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:11   [Information]   Request [16fc2f3a-9510-4e0f-82e1-5f67bf889814] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/azure-webjobs-blobtrigger-funccallmonitoring/messages?numofmessages=9&visibilitytimeout=600
x-ms-version:2025-11-05
Accept:application/xml
x-ms-client-request-id:16fc2f3a-9510-4e0f-82e1-5f67bf889814
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:10 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:22:11   [Information]   Response [16fc2f3a-9510-4e0f-82e1-5f67bf889814] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8f69e-a003-00d0-1752-0256e9000000
x-ms-client-request-id:16fc2f3a-9510-4e0f-82e1-5f67bf889814
x-ms-version:2025-11-05
Date:Mon, 22 Jun 2026 14:22:10 GMT
Content-Type:application/xml

2026-06-22T14:22:11   [Verbose]   Poll for function 'blob_trigger_starter' on queue 'azure-webjobs-blobtrigger-funccallmonitoring' with ClientRequestId '16fc2f3a-9510-4e0f-82e1-5f67bf889814' found 0 messages in 5 ms.
2026-06-22T14:22:11   [Verbose]   Function 'blob_trigger_starter' will wait 49937.6094 ms before polling queue 'azure-webjobs-blobtrigger-funccallmonitoring'.
2026-06-22T14:22:13   [Information]   Request [c34476c2-3676-48cc-b5f8-5a675f8f1606] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:c34476c2-3676-48cc-b5f8-5a675f8f1606
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:13 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:22:13   [Information]   Response [c34476c2-3676-48cc-b5f8-5a675f8f1606] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a8f87e-a003-00d0-5152-0256e9000000
x-ms-client-request-id:c34476c2-3676-48cc-b5f8-5a675f8f1606
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:22:12 GMT
Content-Type:application/xml

2026-06-22T14:22:14   [Verbose]   [HostMonitor] Checking worker statuses (Count=1)
2026-06-22T14:22:14   [Verbose]   [HostMonitor] Worker status: ID=788f0a3b-fad5-4de0-b3dd-9699fa2a79e5, Latency=1ms
2026-06-22T14:22:14   [Verbose]   [HostMonitor] Host process CPU stats (PID 52): History=(0,0,0,0,1), AvgCpuLoad=0.2, MaxCpuLoad=1
2026-06-22T14:22:14   [Verbose]   [HostMonitor] Host process CPU stats (PID 27): History=(2,1,1,2,1), AvgCpuLoad=1, MaxCpuLoad=2
2026-06-22T14:22:14   [Verbose]   [HostMonitor] Host aggregate CPU load 2
2026-06-22T14:22:14   [Information]   Executing StatusCodeResult, setting HTTP status code 200
2026-06-22T14:22:18   [Information]   Request [fed91b41-c8d4-4875-b158-46fe084332f0] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/locks/funccallmonitoring/host?comp=lease
x-ms-lease-action:renew
x-ms-lease-id:aa0b511e-7a56-1cdd-e9d7-33f1b19d7952
x-ms-version:2024-11-04
Accept:application/xml
x-ms-client-request-id:fed91b41-c8d4-4875-b158-46fe084332f0
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.22.1 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:18   [Information]   Response [fed91b41-c8d4-4875-b158-46fe084332f0] 200 OK (00.0s)
ETag:"0x8DECE2D7D1660EE"
x-ms-request-id:665a89fa-c01e-00d6-1252-026556000000
x-ms-client-request-id:fed91b41-c8d4-4875-b158-46fe084332f0
x-ms-version:2024-11-04
x-ms-lease-id:aa0b511e-7a56-1cdd-e9d7-33f1b19d7952
Date:Mon, 22 Jun 2026 14:22:17 GMT
Content-Length:0
Last-Modified:Fri, 19 Jun 2026 18:06:30 GMT

2026-06-22T14:22:18   [Information]   Request [ee1c49bc-0f73-4d89-9d8f-8860f169c096] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1400&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:ee1c49bc-0f73-4d89-9d8f-8860f169c096
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:18   [Information]   Request [fa56be76-e0dc-4ece-87b6-d9804e30d7e7] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs?restype=container&comp=list&marker=&maxresults=10000
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:fa56be76-e0dc-4ece-87b6-d9804e30d7e7
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:18   [Information]   Response [fa56be76-e0dc-4ece-87b6-d9804e30d7e7] 200 OK (00.0s)
Transfer-Encoding:chunked
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c240a5f-f01e-0015-7e52-0211a4000000
x-ms-client-request-id:fa56be76-e0dc-4ece-87b6-d9804e30d7e7
x-ms-version:2026-02-06
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:22:17 GMT
Content-Type:application/xml

2026-06-22T14:22:18   [Verbose]   Poll for blobs newer than '2026-06-22T14:21:17.000Z' in container 'labhrdocs' with ClientRequestId 'b1846787-d31d-4abb-9d8d-6aa424fa566e' found 1 blobs in 4 ms. ContinuationToken: False.
2026-06-22T14:22:18   [Information]   Request [9155a117-dafc-43fb-b404-1159d8334a15] HEAD https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:9155a117-dafc-43fb-b404-1159d8334a15
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:18   [Information]   Response [ee1c49bc-0f73-4d89-9d8f-8860f169c096] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:5a244d3e-901e-0000-3852-026bbf000000
x-ms-client-request-id:ee1c49bc-0f73-4d89-9d8f-8860f169c096
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:22:17 GMT
Content-Type:application/xml

2026-06-22T14:22:18   [Information]   Request [d335a7e8-b10e-40bd-8743-4651c1ee113d] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1300&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:d335a7e8-b10e-40bd-8743-4651c1ee113d
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:18   [Information]   Response [9155a117-dafc-43fb-b404-1159d8334a15] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Vary:Origin
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c240a63-f01e-0015-0152-0211a4000000
x-ms-client-request-id:9155a117-dafc-43fb-b404-1159d8334a15
x-ms-version:2026-02-06
x-ms-tag-count:2
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:22:17 GMT
Content-Length:41837686
Content-Type:video/mp4
Content-MD5:FDGtsdzxt+wnqxE3hlFsqg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:22:18   [Information]   Request [e9a81cb6-e370-4b88-b4be-e6d82425b58c] HEAD https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/blobreceipts/funccallmonitoring/Host.Functions.blob_trigger_starter/%220x8DED069863F6A51%22/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:e9a81cb6-e370-4b88-b4be-e6d82425b58c
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:18 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:18   [Information]   Response [e9a81cb6-e370-4b88-b4be-e6d82425b58c] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED06986690316"
x-ms-request-id:b348061e-301e-0036-2252-02e6cf000000
x-ms-client-request-id:e9a81cb6-e370-4b88-b4be-e6d82425b58c
x-ms-version:2026-02-06
x-ms-tag-count:2
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:22:17 GMT
Content-Length:0
Content-Type:application/octet-stream
Content-MD5:1B2M2Y8AsgTpgAmY7PhCfg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:22:18   [Verbose]   Blob 'bb12.mp4' will be skipped for function 'blob_trigger_starter' because this blob with ETag '"0x8DED069863F6A51"' has already been processed. PollId: 'b1846787-d31d-4abb-9d8d-6aa424fa566e'. Source: 'ContainerScan'.
2026-06-22T14:22:18   [Information]   Response [d335a7e8-b10e-40bd-8743-4651c1ee113d] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:5a244d43-901e-0000-3c52-026bbf000000
x-ms-client-request-id:d335a7e8-b10e-40bd-8743-4651c1ee113d
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:22:17 GMT
Content-Type:application/xml

2026-06-22T14:22:20   [Information]   Request [2c43aaf4-24ee-4b21-96b0-73951decf7be] GET https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions()?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
Accept:application/json;odata=minimalmetadata
x-ms-client-request-id:2c43aaf4-24ee-4b21-96b0-73951decf7be
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:20   [Information]   Response [2c43aaf4-24ee-4b21-96b0-73951decf7be] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:16a69032-0002-00bb-4e52-02d11d000000
x-ms-client-request-id:2c43aaf4-24ee-4b21-96b0-73951decf7be
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:19 GMT
Content-Type:application/json;odata=minimalmetadata;streaming=true;charset=utf-8

2026-06-22T14:22:20   [Information]   Request [cb044098-a2d6-4892-bdaf-ce2343f58509] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-00')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A22%3A09.4788696Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:cb044098-a2d6-4892-bdaf-ce2343f58509
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:20   [Information]   Response [cb044098-a2d6-4892-bdaf-ce2343f58509] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A22%3A19.5117951Z'"
x-ms-request-id:16a69037-0002-00bb-5152-02d11d000000
x-ms-client-request-id:cb044098-a2d6-4892-bdaf-ce2343f58509
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:19 GMT
Content-Length:0

2026-06-22T14:22:20   [Verbose]   funccallmonitoring-control-00:  lease renewal with token  succeeded
2026-06-22T14:22:20   [Information]   Request [3771b59d-0f26-4404-804a-536df6ba38ed] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-01')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A22%3A09.4858585Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:3771b59d-0f26-4404-804a-536df6ba38ed
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:20   [Information]   Response [3771b59d-0f26-4404-804a-536df6ba38ed] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A22%3A19.516787Z'"
x-ms-request-id:16a69039-0002-00bb-5352-02d11d000000
x-ms-client-request-id:3771b59d-0f26-4404-804a-536df6ba38ed
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:19 GMT
Content-Length:0

2026-06-22T14:22:20   [Verbose]   funccallmonitoring-control-01:  lease renewal with token  succeeded
2026-06-22T14:22:20   [Information]   Request [9959da38-51b6-4d2a-8ab3-3433ff14755b] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-02')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A22%3A09.4918488Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:9959da38-51b6-4d2a-8ab3-3433ff14755b
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:20   [Information]   Response [9959da38-51b6-4d2a-8ab3-3433ff14755b] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A22%3A19.5237759Z'"
x-ms-request-id:16a6903a-0002-00bb-5452-02d11d000000
x-ms-client-request-id:9959da38-51b6-4d2a-8ab3-3433ff14755b
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:19 GMT
Content-Length:0

2026-06-22T14:22:20   [Verbose]   funccallmonitoring-control-02:  lease renewal with token  succeeded
2026-06-22T14:22:20   [Information]   Request [8db472ef-7929-44b7-a320-54a47e035cec] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-03')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A22%3A09.4978393Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:8db472ef-7929-44b7-a320-54a47e035cec
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:20   [Information]   Response [8db472ef-7929-44b7-a320-54a47e035cec] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A22%3A19.5287679Z'"
x-ms-request-id:16a6903b-0002-00bb-5552-02d11d000000
x-ms-client-request-id:8db472ef-7929-44b7-a320-54a47e035cec
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:19 GMT
Content-Length:0

2026-06-22T14:22:20   [Verbose]   funccallmonitoring-control-03:  lease renewal with token  succeeded
2026-06-22T14:22:24   [Verbose]   [HostMonitor] Checking worker statuses (Count=1)
2026-06-22T14:22:24   [Verbose]   [HostMonitor] Worker status: ID=788f0a3b-fad5-4de0-b3dd-9699fa2a79e5, Latency=1ms
2026-06-22T14:22:24   [Verbose]   [HostMonitor] Host process CPU stats (PID 52): History=(0,0,0,0,1), AvgCpuLoad=0.2, MaxCpuLoad=1
2026-06-22T14:22:24   [Verbose]   [HostMonitor] Host process CPU stats (PID 27): History=(1,2,1,1,2), AvgCpuLoad=1, MaxCpuLoad=2
2026-06-22T14:22:24   [Verbose]   [HostMonitor] Host aggregate CPU load 2
2026-06-22T14:22:24   [Information]   Executing StatusCodeResult, setting HTTP status code 200
2026-06-22T14:22:26   [Information]   Request [0b9ee946-0335-47c4-9174-4d883db16e01] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/locks/funccallmonitoring/WebJobs.Internal.Blobs.Listener?comp=lease
x-ms-lease-action:renew
x-ms-lease-id:a91e3446-f57f-4eda-b6bf-2d5455b5d031
x-ms-version:2024-11-04
Accept:application/xml
x-ms-client-request-id:0b9ee946-0335-47c4-9174-4d883db16e01
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.22.1 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:26 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:26   [Information]   Response [0b9ee946-0335-47c4-9174-4d883db16e01] 200 OK (00.0s)
ETag:"0x8DECE1769D6FB81"
x-ms-request-id:665a9b53-c01e-00d6-1052-026556000000
x-ms-client-request-id:0b9ee946-0335-47c4-9174-4d883db16e01
x-ms-version:2024-11-04
x-ms-lease-id:a91e3446-f57f-4eda-b6bf-2d5455b5d031
Date:Mon, 22 Jun 2026 14:22:25 GMT
Content-Length:0
Last-Modified:Fri, 19 Jun 2026 15:28:28 GMT

2026-06-22T14:22:26   [Information]   Request [8dfae906-e73d-4e7d-98c8-4b695e0fd501] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/?comp=list&maxresults=1
x-ms-version:2024-11-04
Accept:application/xml
x-ms-client-request-id:8dfae906-e73d-4e7d-98c8-4b695e0fd501
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.22.1 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:26 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:26   [Information]   Response [8dfae906-e73d-4e7d-98c8-4b695e0fd501] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:665a9b5a-c01e-00d6-1652-026556000000
x-ms-client-request-id:8dfae906-e73d-4e7d-98c8-4b695e0fd501
x-ms-version:2024-11-04
Date:Mon, 22 Jun 2026 14:22:25 GMT
Content-Type:application/xml

2026-06-22T14:22:28   [Information]   Request [453ddaa9-7dcd-4053-850a-69edb25afbc6] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1400&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:453ddaa9-7dcd-4053-850a-69edb25afbc6
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:28 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:28   [Information]   Request [0d3b34bf-6036-4444-8ff8-80d9a0bf7d15] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs?restype=container&comp=list&marker=&maxresults=10000
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:0d3b34bf-6036-4444-8ff8-80d9a0bf7d15
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:28 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:28   [Information]   Response [0d3b34bf-6036-4444-8ff8-80d9a0bf7d15] 200 OK (00.0s)
Transfer-Encoding:chunked
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c2413eb-f01e-0015-4352-0211a4000000
x-ms-client-request-id:0d3b34bf-6036-4444-8ff8-80d9a0bf7d15
x-ms-version:2026-02-06
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:22:27 GMT
Content-Type:application/xml

2026-06-22T14:22:28   [Verbose]   Poll for blobs newer than '2026-06-22T14:21:17.000Z' in container 'labhrdocs' with ClientRequestId 'f384cded-45ce-4f22-b55d-b9efe191728f' found 1 blobs in 5 ms. ContinuationToken: False.
2026-06-22T14:22:28   [Information]   Request [8608539f-4895-435f-aaf3-8160a0c8c3d4] HEAD https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:8608539f-4895-435f-aaf3-8160a0c8c3d4
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:28 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:28   [Information]   Response [453ddaa9-7dcd-4053-850a-69edb25afbc6] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:5a246a34-901e-0000-7552-026bbf000000
x-ms-client-request-id:453ddaa9-7dcd-4053-850a-69edb25afbc6
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:22:27 GMT
Content-Type:application/xml

2026-06-22T14:22:28   [Information]   Request [13fea910-81a3-4327-aedf-c11866b953ef] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1300&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:13fea910-81a3-4327-aedf-c11866b953ef
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:28 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:28   [Information]   Response [8608539f-4895-435f-aaf3-8160a0c8c3d4] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Vary:Origin
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c2413ef-f01e-0015-4552-0211a4000000
x-ms-client-request-id:8608539f-4895-435f-aaf3-8160a0c8c3d4
x-ms-version:2026-02-06
x-ms-tag-count:2
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:22:27 GMT
Content-Length:41837686
Content-Type:video/mp4
Content-MD5:FDGtsdzxt+wnqxE3hlFsqg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:22:28   [Information]   Request [4ef25c38-312b-4ffd-b606-a9300af4ce04] HEAD https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/blobreceipts/funccallmonitoring/Host.Functions.blob_trigger_starter/%220x8DED069863F6A51%22/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:4ef25c38-312b-4ffd-b606-a9300af4ce04
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:28 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:28   [Information]   Response [4ef25c38-312b-4ffd-b606-a9300af4ce04] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED06986690316"
x-ms-request-id:b348232c-301e-0036-6c52-02e6cf000000
x-ms-client-request-id:4ef25c38-312b-4ffd-b606-a9300af4ce04
x-ms-version:2026-02-06
x-ms-tag-count:2
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:22:27 GMT
Content-Length:0
Content-Type:application/octet-stream
Content-MD5:1B2M2Y8AsgTpgAmY7PhCfg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:22:28   [Verbose]   Blob 'bb12.mp4' will be skipped for function 'blob_trigger_starter' because this blob with ETag '"0x8DED069863F6A51"' has already been processed. PollId: 'f384cded-45ce-4f22-b55d-b9efe191728f'. Source: 'ContainerScan'.
2026-06-22T14:22:28   [Information]   Response [13fea910-81a3-4327-aedf-c11866b953ef] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:5a246a38-901e-0000-7752-026bbf000000
x-ms-client-request-id:13fea910-81a3-4327-aedf-c11866b953ef
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:22:27 GMT
Content-Type:application/xml

2026-06-22T14:22:28   [Information]   Request [0b733cf3-f22e-43df-914c-ed4081216f6a] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs/blob/2026/06/22/1400/000002.log
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:0b733cf3-f22e-43df-914c-ed4081216f6a
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:28 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:28   [Information]   Response [0b733cf3-f22e-43df-914c-ed4081216f6a] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED069ACCAC51A"
x-ms-request-id:5a246a58-901e-0000-1152-026bbf000000
x-ms-client-request-id:0b733cf3-f22e-43df-914c-ed4081216f6a
x-ms-version:2026-02-06
x-ms-meta-StartTime:REDACTED
x-ms-meta-EndTime:REDACTED
x-ms-meta-LogType:REDACTED
x-ms-meta-LogVersion:REDACTED
x-ms-meta-Opaque1:REDACTED
x-ms-creation-time:Mon, 22 Jun 2026 14:22:22 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:22:27 GMT
Content-Length:42365
Content-Type:application/octet-stream
Last-Modified:Mon, 22 Jun 2026 14:22:22 GMT

2026-06-22T14:22:28   [Information]   Request [6a257c08-91cc-45fd-86fd-bc0762f3fb54] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-02/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:6a257c08-91cc-45fd-86fd-bc0762f3fb54
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:28 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:22:28   [Information]   Response [6a257c08-91cc-45fd-86fd-bc0762f3fb54] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a9069c-a003-00d0-0852-0256e9000000
x-ms-client-request-id:6a257c08-91cc-45fd-86fd-bc0762f3fb54
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:22:27 GMT
Content-Type:application/xml

2026-06-22T14:22:30   [Information]   Request [73246198-49e2-4dd1-8bae-55c81b86f0ac] GET https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions()?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
Accept:application/json;odata=minimalmetadata
x-ms-client-request-id:73246198-49e2-4dd1-8bae-55c81b86f0ac
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:30   [Information]   Response [73246198-49e2-4dd1-8bae-55c81b86f0ac] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:16a6914c-0002-00bb-1552-02d11d000000
x-ms-client-request-id:73246198-49e2-4dd1-8bae-55c81b86f0ac
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:29 GMT
Content-Type:application/json;odata=minimalmetadata;streaming=true;charset=utf-8

2026-06-22T14:22:30   [Information]   Request [814d5480-4df5-4da0-9841-ebf4734a810f] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-00')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A22%3A19.5117951Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:814d5480-4df5-4da0-9841-ebf4734a810f
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:30   [Information]   Response [814d5480-4df5-4da0-9841-ebf4734a810f] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A22%3A29.5417268Z'"
x-ms-request-id:16a69150-0002-00bb-1752-02d11d000000
x-ms-client-request-id:814d5480-4df5-4da0-9841-ebf4734a810f
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:29 GMT
Content-Length:0

2026-06-22T14:22:30   [Verbose]   funccallmonitoring-control-00:  lease renewal with token  succeeded
2026-06-22T14:22:30   [Information]   Request [94322923-99a7-41ae-a335-b0386bb898ad] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-01')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A22%3A19.516787Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:94322923-99a7-41ae-a335-b0386bb898ad
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:30   [Information]   Response [94322923-99a7-41ae-a335-b0386bb898ad] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A22%3A29.5477171Z'"
x-ms-request-id:16a69152-0002-00bb-1852-02d11d000000
x-ms-client-request-id:94322923-99a7-41ae-a335-b0386bb898ad
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:29 GMT
Content-Length:0

2026-06-22T14:22:30   [Verbose]   funccallmonitoring-control-01:  lease renewal with token  succeeded
2026-06-22T14:22:30   [Information]   Request [11788709-5e85-464c-aa07-b550678bfb14] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-02')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A22%3A19.5237759Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:11788709-5e85-464c-aa07-b550678bfb14
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:30   [Information]   Response [11788709-5e85-464c-aa07-b550678bfb14] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A22%3A29.5547057Z'"
x-ms-request-id:16a69153-0002-00bb-1952-02d11d000000
x-ms-client-request-id:11788709-5e85-464c-aa07-b550678bfb14
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:29 GMT
Content-Length:0

2026-06-22T14:22:30   [Verbose]   funccallmonitoring-control-02:  lease renewal with token  succeeded
2026-06-22T14:22:30   [Information]   Request [43b56687-d866-4d9f-b1e3-f6c78740c0e9] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-03')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A22%3A19.5287679Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:43b56687-d866-4d9f-b1e3-f6c78740c0e9
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:30   [Information]   Response [43b56687-d866-4d9f-b1e3-f6c78740c0e9] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A22%3A29.5606967Z'"
x-ms-request-id:16a69154-0002-00bb-1a52-02d11d000000
x-ms-client-request-id:43b56687-d866-4d9f-b1e3-f6c78740c0e9
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:29 GMT
Content-Length:0

2026-06-22T14:22:30   [Verbose]   funccallmonitoring-control-03:  lease renewal with token  succeeded
2026-06-22T14:22:30   [Information]   Request [d68866e3-fe85-42cf-88df-3144177c696b] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/locks/funccallmonitoring/host?comp=lease
x-ms-lease-action:renew
x-ms-lease-id:aa0b511e-7a56-1cdd-e9d7-33f1b19d7952
x-ms-version:2024-11-04
Accept:application/xml
x-ms-client-request-id:d68866e3-fe85-42cf-88df-3144177c696b
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.22.1 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:30 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:30   [Information]   Response [d68866e3-fe85-42cf-88df-3144177c696b] 200 OK (00.0s)
ETag:"0x8DECE2D7D1660EE"
x-ms-request-id:665aa176-c01e-00d6-1952-026556000000
x-ms-client-request-id:d68866e3-fe85-42cf-88df-3144177c696b
x-ms-version:2024-11-04
x-ms-lease-id:aa0b511e-7a56-1cdd-e9d7-33f1b19d7952
Date:Mon, 22 Jun 2026 14:22:29 GMT
Content-Length:0
Last-Modified:Fri, 19 Jun 2026 18:06:30 GMT

2026-06-22T14:22:34   [Verbose]   [HostMonitor] Checking worker statuses (Count=1)
2026-06-22T14:22:34   [Verbose]   [HostMonitor] Worker status: ID=788f0a3b-fad5-4de0-b3dd-9699fa2a79e5, Latency=1ms
2026-06-22T14:22:34   [Verbose]   [HostMonitor] Host process CPU stats (PID 52): History=(0,0,0,0,0), AvgCpuLoad=0, MaxCpuLoad=0
2026-06-22T14:22:34   [Verbose]   [HostMonitor] Host process CPU stats (PID 27): History=(2,1,1,1,1), AvgCpuLoad=1, MaxCpuLoad=2
2026-06-22T14:22:34   [Verbose]   [HostMonitor] Host aggregate CPU load 1
2026-06-22T14:22:34   [Information]   Executing StatusCodeResult, setting HTTP status code 200
2026-06-22T14:22:34   [Verbose]   funccallmonitoring-applease: Starting app lease renewal with token 3320c211-0000-0000-0000-000000000000
2026-06-22T14:22:34   [Information]   Request [8f7ab592-588b-45c2-92db-e3266d260a38] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/funccallmonitoring-applease?comp=lease&restype=container
x-ms-lease-action:renew
x-ms-lease-id:3320c211-0000-0000-0000-000000000000
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:8f7ab592-588b-45c2-92db-e3266d260a38
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:33 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:34   [Information]   Response [8f7ab592-588b-45c2-92db-e3266d260a38] 200 OK (00.0s)
ETag:"0x8DECE10DD3DE605"
x-ms-request-id:5a2478d6-901e-0000-7752-026bbf000000
x-ms-client-request-id:8f7ab592-588b-45c2-92db-e3266d260a38
x-ms-version:2026-02-06
x-ms-lease-id:3320c211-0000-0000-0000-000000000000
Date:Mon, 22 Jun 2026 14:22:33 GMT
Content-Length:0
Last-Modified:Fri, 19 Jun 2026 14:41:35 GMT

2026-06-22T14:22:34   [Verbose]   funccallmonitoring-applease: app lease renewal with token 3320c211-0000-0000-0000-000000000000 succeeded
2026-06-22T14:22:37   [Information]   Request [0ec98d48-1c50-4cc2-b3cc-ea2772d94948] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-workitems/messages?numofmessages=1&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:0ec98d48-1c50-4cc2-b3cc-ea2772d94948
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:36 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:22:37   [Information]   Response [0ec98d48-1c50-4cc2-b3cc-ea2772d94948] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a91103-a003-00d0-1952-0256e9000000
x-ms-client-request-id:0ec98d48-1c50-4cc2-b3cc-ea2772d94948
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:22:36 GMT
Content-Type:application/xml

2026-06-22T14:22:38   [Information]   Request [0f18eead-c54b-4c93-bc86-3f842a32ad41] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-01/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:0f18eead-c54b-4c93-bc86-3f842a32ad41
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:38 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:22:38   [Information]   Response [0f18eead-c54b-4c93-bc86-3f842a32ad41] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a9125e-a003-00d0-6352-0256e9000000
x-ms-client-request-id:0f18eead-c54b-4c93-bc86-3f842a32ad41
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:22:37 GMT
Content-Type:application/xml

2026-06-22T14:22:38   [Information]   Request [56b7eb2f-049b-473c-ae98-9b9f09d91aa5] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1400&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:56b7eb2f-049b-473c-ae98-9b9f09d91aa5
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:38 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:38   [Information]   Request [635835e7-07db-4807-8c3c-47240915f13f] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs?restype=container&comp=list&marker=&maxresults=10000
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:635835e7-07db-4807-8c3c-47240915f13f
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:38 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:38   [Information]   Response [56b7eb2f-049b-473c-ae98-9b9f09d91aa5] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:5a24835b-901e-0000-0e52-026bbf000000
x-ms-client-request-id:56b7eb2f-049b-473c-ae98-9b9f09d91aa5
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:22:37 GMT
Content-Type:application/xml

2026-06-22T14:22:38   [Information]   Response [635835e7-07db-4807-8c3c-47240915f13f] 200 OK (00.0s)
Transfer-Encoding:chunked
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c241ef7-f01e-0015-4f52-0211a4000000
x-ms-client-request-id:635835e7-07db-4807-8c3c-47240915f13f
x-ms-version:2026-02-06
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:22:38 GMT
Content-Type:application/xml

2026-06-22T14:22:38   [Verbose]   Poll for blobs newer than '2026-06-22T14:21:17.000Z' in container 'labhrdocs' with ClientRequestId '6fca4e4b-a750-4e42-ab89-b47a6d91240e' found 1 blobs in 8 ms. ContinuationToken: False.
2026-06-22T14:22:38   [Information]   Request [0110647b-1d3a-4a4d-859a-e16e96e19971] HEAD https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:0110647b-1d3a-4a4d-859a-e16e96e19971
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:38 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:38   [Information]   Request [e85482d1-23da-4a60-aced-53328c9d2bff] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1300&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:e85482d1-23da-4a60-aced-53328c9d2bff
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:38 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:38   [Information]   Response [0110647b-1d3a-4a4d-859a-e16e96e19971] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Vary:Origin
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c241efb-f01e-0015-5252-0211a4000000
x-ms-client-request-id:0110647b-1d3a-4a4d-859a-e16e96e19971
x-ms-version:2026-02-06
x-ms-tag-count:2
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:22:38 GMT
Content-Length:41837686
Content-Type:video/mp4
Content-MD5:FDGtsdzxt+wnqxE3hlFsqg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:22:38   [Information]   Request [5458d4a7-3b38-4a76-a4b8-6199f57969be] HEAD https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/blobreceipts/funccallmonitoring/Host.Functions.blob_trigger_starter/%220x8DED069863F6A51%22/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:5458d4a7-3b38-4a76-a4b8-6199f57969be
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:38 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:38   [Information]   Response [5458d4a7-3b38-4a76-a4b8-6199f57969be] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED06986690316"
x-ms-request-id:b3483a02-301e-0036-2552-02e6cf000000
x-ms-client-request-id:5458d4a7-3b38-4a76-a4b8-6199f57969be
x-ms-version:2026-02-06
x-ms-tag-count:2
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:22:37 GMT
Content-Length:0
Content-Type:application/octet-stream
Content-MD5:1B2M2Y8AsgTpgAmY7PhCfg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:22:38   [Verbose]   Blob 'bb12.mp4' will be skipped for function 'blob_trigger_starter' because this blob with ETag '"0x8DED069863F6A51"' has already been processed. PollId: '6fca4e4b-a750-4e42-ab89-b47a6d91240e'. Source: 'ContainerScan'.
2026-06-22T14:22:38   [Information]   Response [e85482d1-23da-4a60-aced-53328c9d2bff] 200 OK (00.1s)
Transfer-Encoding:chunked
x-ms-request-id:5a248361-901e-0000-1352-026bbf000000
x-ms-client-request-id:e85482d1-23da-4a60-aced-53328c9d2bff
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:22:37 GMT
Content-Type:application/xml

2026-06-22T14:22:39   [Information]   Request [fc3ab092-93df-42df-bdb3-00d1fe1549be] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-00/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:fc3ab092-93df-42df-bdb3-00d1fe1549be
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:39 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:22:39   [Information]   Response [fc3ab092-93df-42df-bdb3-00d1fe1549be] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a9133a-a003-00d0-3552-0256e9000000
x-ms-client-request-id:fc3ab092-93df-42df-bdb3-00d1fe1549be
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:22:38 GMT
Content-Type:application/xml

2026-06-22T14:22:40   [Information]   Request [adca5e5f-2574-45f9-b6e1-7db102e696dd] GET https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions()?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
Accept:application/json;odata=minimalmetadata
x-ms-client-request-id:adca5e5f-2574-45f9-b6e1-7db102e696dd
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:40   [Information]   Response [adca5e5f-2574-45f9-b6e1-7db102e696dd] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:16a693e9-0002-00bb-2b52-02d11d000000
x-ms-client-request-id:adca5e5f-2574-45f9-b6e1-7db102e696dd
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:39 GMT
Content-Type:application/json;odata=minimalmetadata;streaming=true;charset=utf-8

2026-06-22T14:22:40   [Information]   Request [d35bff58-5501-49e0-ac71-42f6f02f0bf4] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-00')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A22%3A29.5417268Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:d35bff58-5501-49e0-ac71-42f6f02f0bf4
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:40   [Information]   Response [d35bff58-5501-49e0-ac71-42f6f02f0bf4] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A22%3A39.570656Z'"
x-ms-request-id:16a693eb-0002-00bb-2d52-02d11d000000
x-ms-client-request-id:d35bff58-5501-49e0-ac71-42f6f02f0bf4
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:39 GMT
Content-Length:0

2026-06-22T14:22:40   [Verbose]   funccallmonitoring-control-00:  lease renewal with token  succeeded
2026-06-22T14:22:40   [Information]   Request [cca67df0-fd00-4d8b-9684-1d5c7673c2e7] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-01')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A22%3A29.5477171Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:cca67df0-fd00-4d8b-9684-1d5c7673c2e7
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:40   [Information]   Response [cca67df0-fd00-4d8b-9684-1d5c7673c2e7] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A22%3A39.575648Z'"
x-ms-request-id:16a693ec-0002-00bb-2e52-02d11d000000
x-ms-client-request-id:cca67df0-fd00-4d8b-9684-1d5c7673c2e7
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:39 GMT
Content-Length:0

2026-06-22T14:22:40   [Verbose]   funccallmonitoring-control-01:  lease renewal with token  succeeded
2026-06-22T14:22:40   [Information]   Request [ab8c2559-3af3-40c5-99b1-d2bfbd363005] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-02')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A22%3A29.5547057Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:ab8c2559-3af3-40c5-99b1-d2bfbd363005
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:40   [Information]   Response [ab8c2559-3af3-40c5-99b1-d2bfbd363005] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A22%3A39.5816388Z'"
x-ms-request-id:16a693ed-0002-00bb-2f52-02d11d000000
x-ms-client-request-id:ab8c2559-3af3-40c5-99b1-d2bfbd363005
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:39 GMT
Content-Length:0

2026-06-22T14:22:40   [Verbose]   funccallmonitoring-control-02:  lease renewal with token  succeeded
2026-06-22T14:22:40   [Information]   Request [22b87e6d-8c29-4f40-bbac-4b722a15b799] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-03')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A22%3A29.5606967Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:22b87e6d-8c29-4f40-bbac-4b722a15b799
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:40   [Information]   Response [22b87e6d-8c29-4f40-bbac-4b722a15b799] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A22%3A39.5866304Z'"
x-ms-request-id:16a693ee-0002-00bb-3052-02d11d000000
x-ms-client-request-id:22b87e6d-8c29-4f40-bbac-4b722a15b799
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:39 GMT
Content-Length:0

2026-06-22T14:22:40   [Verbose]   funccallmonitoring-control-03:  lease renewal with token  succeeded
2026-06-22T14:22:42   [Information]   Request [2bd27a93-972e-4db5-bbdb-eda436df0040] PUT https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/locks/funccallmonitoring/host?comp=lease
x-ms-lease-action:renew
x-ms-lease-id:aa0b511e-7a56-1cdd-e9d7-33f1b19d7952
x-ms-version:2024-11-04
Accept:application/xml
x-ms-client-request-id:2bd27a93-972e-4db5-bbdb-eda436df0040
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.22.1 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:42 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:42   [Information]   Response [2bd27a93-972e-4db5-bbdb-eda436df0040] 200 OK (00.0s)
ETag:"0x8DECE2D7D1660EE"
x-ms-request-id:665ab710-c01e-00d6-7a52-026556000000
x-ms-client-request-id:2bd27a93-972e-4db5-bbdb-eda436df0040
x-ms-version:2024-11-04
x-ms-lease-id:aa0b511e-7a56-1cdd-e9d7-33f1b19d7952
Date:Mon, 22 Jun 2026 14:22:41 GMT
Content-Length:0
Last-Modified:Fri, 19 Jun 2026 18:06:30 GMT

2026-06-22T14:22:43   [Information]   Request [df3fdcf3-8521-408f-b08a-5f0794d279a9] GET https://rgd1tsandboxaiapp01846c.queue.core.windows.net/funccallmonitoring-control-03/messages?numofmessages=32&visibilitytimeout=300
x-ms-version:2025-05-05
Accept:application/xml
x-ms-client-request-id:df3fdcf3-8521-408f-b08a-5f0794d279a9
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Queues/12.24.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:43 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Queues
2026-06-22T14:22:43   [Information]   Response [df3fdcf3-8521-408f-b08a-5f0794d279a9] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:97a9175d-a003-00d0-1852-0256e9000000
x-ms-client-request-id:df3fdcf3-8521-408f-b08a-5f0794d279a9
x-ms-version:2025-05-05
Date:Mon, 22 Jun 2026 14:22:42 GMT
Content-Type:application/xml

2026-06-22T14:22:44   [Verbose]   [HostMonitor] Checking worker statuses (Count=1)
2026-06-22T14:22:44   [Verbose]   [HostMonitor] Worker status: ID=788f0a3b-fad5-4de0-b3dd-9699fa2a79e5, Latency=2ms
2026-06-22T14:22:44   [Verbose]   [HostMonitor] Host process CPU stats (PID 52): History=(0,0,0,0,0), AvgCpuLoad=0, MaxCpuLoad=0
2026-06-22T14:22:44   [Verbose]   [HostMonitor] Host process CPU stats (PID 27): History=(2,2,1,1,0), AvgCpuLoad=1, MaxCpuLoad=2
2026-06-22T14:22:44   [Verbose]   [HostMonitor] Host aggregate CPU load 1
2026-06-22T14:22:44   [Information]   Executing StatusCodeResult, setting HTTP status code 200
2026-06-22T14:22:48   [Information]   Request [5501f628-8eee-4f0d-bd8f-e3f65c6758a8] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1400&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:5501f628-8eee-4f0d-bd8f-e3f65c6758a8
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:48 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:48   [Information]   Request [6aeb84d0-9a67-4eb5-9952-86bd5091c8e1] GET https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs?restype=container&comp=list&marker=&maxresults=10000
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:6aeb84d0-9a67-4eb5-9952-86bd5091c8e1
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:48 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:48   [Information]   Response [6aeb84d0-9a67-4eb5-9952-86bd5091c8e1] 200 OK (00.0s)
Transfer-Encoding:chunked
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c242981-f01e-0015-2352-0211a4000000
x-ms-client-request-id:6aeb84d0-9a67-4eb5-9952-86bd5091c8e1
x-ms-version:2026-02-06
Access-Control-Expose-Headers:REDACTED
Access-Control-Allow-Origin:*
Date:Mon, 22 Jun 2026 14:22:48 GMT
Content-Type:application/xml

2026-06-22T14:22:48   [Verbose]   Poll for blobs newer than '2026-06-22T14:21:17.000Z' in container 'labhrdocs' with ClientRequestId 'd0717029-298c-4726-9fe6-427448ae0526' found 1 blobs in 4 ms. ContinuationToken: False.
2026-06-22T14:22:48   [Information]   Request [79a22bca-03e9-4a55-b659-2568c7c56bcf] HEAD https://aiinnovationstoragedev.blob.core.windows.net/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:79a22bca-03e9-4a55-b659-2568c7c56bcf
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:48 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:48   [Information]   Response [5501f628-8eee-4f0d-bd8f-e3f65c6758a8] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:5a2499cf-901e-0000-4552-026bbf000000
x-ms-client-request-id:5501f628-8eee-4f0d-bd8f-e3f65c6758a8
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:22:47 GMT
Content-Type:application/xml

2026-06-22T14:22:48   [Information]   Request [dee7bdcd-986d-427f-ab66-2441ddeb3082] GET https://rgd1tsandboxaiapp01846c.blob.core.windows.net/$logs?restype=container&comp=list&prefix=blob%2F2026%2F06%2F22%2F1300&include=Metadata
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:dee7bdcd-986d-427f-ab66-2441ddeb3082
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:48 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:48   [Information]   Response [79a22bca-03e9-4a55-b659-2568c7c56bcf] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED069863F6A51"
Vary:Origin
Server:Windows-Azure-Blob/1.0 Microsoft-HTTPAPI/2.0
x-ms-request-id:9c242986-f01e-0015-2652-0211a4000000
x-ms-client-request-id:79a22bca-03e9-4a55-b659-2568c7c56bcf
x-ms-version:2026-02-06
x-ms-tag-count:2
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:22:48 GMT
Content-Length:41837686
Content-Type:video/mp4
Content-MD5:FDGtsdzxt+wnqxE3hlFsqg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:22:48   [Information]   Request [483f47a2-8849-4275-b4c5-b4c8d8a14b16] HEAD https://rgd1tsandboxaiapp01846c.blob.core.windows.net/azure-webjobs-hosts/blobreceipts/funccallmonitoring/Host.Functions.blob_trigger_starter/%220x8DED069863F6A51%22/labhrdocs/bb12.mp4
x-ms-version:2026-02-06
Accept:application/xml
x-ms-client-request-id:483f47a2-8849-4275-b4c5-b4c8d8a14b16
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Storage.Blobs/12.27.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:Mon, 22 Jun 2026 14:22:48 GMT
Authorization:REDACTED
client assembly: Azure.Storage.Blobs
2026-06-22T14:22:48   [Information]   Response [483f47a2-8849-4275-b4c5-b4c8d8a14b16] 200 OK (00.0s)
Accept-Ranges:bytes
ETag:"0x8DED06986690316"
x-ms-request-id:b348510c-301e-0036-1152-02e6cf000000
x-ms-client-request-id:483f47a2-8849-4275-b4c5-b4c8d8a14b16
x-ms-version:2026-02-06
x-ms-tag-count:2
x-ms-creation-time:Mon, 22 Jun 2026 14:21:17 GMT
x-ms-lease-status:unlocked
x-ms-lease-state:available
x-ms-blob-type:BlockBlob
x-ms-server-encrypted:true
x-ms-access-tier:Hot
x-ms-access-tier-inferred:true
Date:Mon, 22 Jun 2026 14:22:47 GMT
Content-Length:0
Content-Type:application/octet-stream
Content-MD5:1B2M2Y8AsgTpgAmY7PhCfg==
Last-Modified:Mon, 22 Jun 2026 14:21:17 GMT

2026-06-22T14:22:48   [Verbose]   Blob 'bb12.mp4' will be skipped for function 'blob_trigger_starter' because this blob with ETag '"0x8DED069863F6A51"' has already been processed. PollId: 'd0717029-298c-4726-9fe6-427448ae0526'. Source: 'ContainerScan'.
2026-06-22T14:22:48   [Information]   Response [dee7bdcd-986d-427f-ab66-2441ddeb3082] 200 OK (00.0s)
Transfer-Encoding:chunked
x-ms-request-id:5a2499d7-901e-0000-4952-026bbf000000
x-ms-client-request-id:dee7bdcd-986d-427f-ab66-2441ddeb3082
x-ms-version:2026-02-06
Date:Mon, 22 Jun 2026 14:22:47 GMT
Content-Type:application/xml

2026-06-22T14:22:50   [Information]   Request [2de2732a-22dd-404a-bbda-6d8e49376ccb] GET https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions()?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
Accept:application/json;odata=minimalmetadata
x-ms-client-request-id:2de2732a-22dd-404a-bbda-6d8e49376ccb
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:50   [Information]   Response [2de2732a-22dd-404a-bbda-6d8e49376ccb] 200 OK (00.0s)
Cache-Control:no-cache
Transfer-Encoding:chunked
x-ms-request-id:16a6955b-0002-00bb-5552-02d11d000000
x-ms-client-request-id:2de2732a-22dd-404a-bbda-6d8e49376ccb
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:49 GMT
Content-Type:application/json;odata=minimalmetadata;streaming=true;charset=utf-8

2026-06-22T14:22:50   [Information]   Request [7f52b2d0-42f2-446a-9ea5-844efcfc3a2a] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-00')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A22%3A39.570656Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:7f52b2d0-42f2-446a-9ea5-844efcfc3a2a
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:50   [Information]   Response [7f52b2d0-42f2-446a-9ea5-844efcfc3a2a] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A22%3A49.6015883Z'"
x-ms-request-id:16a6955e-0002-00bb-5652-02d11d000000
x-ms-client-request-id:7f52b2d0-42f2-446a-9ea5-844efcfc3a2a
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:49 GMT
Content-Length:0

2026-06-22T14:22:50   [Verbose]   funccallmonitoring-control-00:  lease renewal with token  succeeded
2026-06-22T14:22:50   [Information]   Request [bf66392c-ddce-4f2e-b995-dd61752c325f] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-01')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A22%3A39.575648Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:bf66392c-ddce-4f2e-b995-dd61752c325f
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:50   [Information]   Response [bf66392c-ddce-4f2e-b995-dd61752c325f] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A22%3A49.6065804Z'"
x-ms-request-id:16a6955f-0002-00bb-5752-02d11d000000
x-ms-client-request-id:bf66392c-ddce-4f2e-b995-dd61752c325f
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:49 GMT
Content-Length:0

2026-06-22T14:22:50   [Verbose]   funccallmonitoring-control-01:  lease renewal with token  succeeded
2026-06-22T14:22:50   [Information]   Request [520442a7-03d5-4231-b9da-9b10e85f3911] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-02')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A22%3A39.5816388Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:520442a7-03d5-4231-b9da-9b10e85f3911
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:50   [Information]   Response [520442a7-03d5-4231-b9da-9b10e85f3911] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A22%3A49.6135697Z'"
x-ms-request-id:16a69560-0002-00bb-5852-02d11d000000
x-ms-client-request-id:520442a7-03d5-4231-b9da-9b10e85f3911
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:49 GMT
Content-Length:0

2026-06-22T14:22:50   [Verbose]   funccallmonitoring-control-02:  lease renewal with token  succeeded
2026-06-22T14:22:50   [Information]   Request [61f5874f-b23d-491f-88f7-13dab029bacb] PUT https://rgd1tsandboxaiapp01846c.table.core.windows.net/funccallmonitoringPartitions(PartitionKey='',RowKey='funccallmonitoring-control-03')?$format=REDACTED
x-ms-version:REDACTED
DataServiceVersion:REDACTED
If-Match:W/"datetime'2026-06-22T14%3A22%3A39.5866304Z'"
Accept:application/json
Content-Type:application/json
x-ms-client-request-id:61f5874f-b23d-491f-88f7-13dab029bacb
x-ms-return-client-request-id:true
User-Agent:azsdk-net-Data.Tables/12.11.0 (.NET 8.0.26; Debian GNU/Linux 11 (bullseye))
x-ms-date:REDACTED
Authorization:REDACTED
client assembly: Azure.Data.Tables
2026-06-22T14:22:50   [Information]   Response [61f5874f-b23d-491f-88f7-13dab029bacb] 204 No Content (00.0s)
Cache-Control:no-cache
ETag:W/"datetime'2026-06-22T14%3A22%3A49.6205584Z'"
x-ms-request-id:16a69561-0002-00bb-5952-02d11d000000
x-ms-client-request-id:61f5874f-b23d-491f-88f7-13dab029bacb
x-ms-version:REDACTED
X-Content-Type-Options:REDACTED
Date:Mon, 22 Jun 2026 14:22:49 GMT
Content-Length:0

2026-06-22T14:22:50   [Verbose]   funccallmonitoring-control-03:  lease renewal with token  succeeded
