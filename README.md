
PS F:\Workspace\CallMonitoring\Sandbox Python Pipeline> python VideoIDX-LoadCosmos.py
LOOKBACK_HOURS=24 
USE_SAS_FOR_ANALYSIS=True (SAS is NOT stored; only used for analyzer input if enabled)
Cosmos: testDB1/CallQuality PK=/originalFileName
AzureCliCredential.get_token_info failed: Failed to invoke the Azure CLI 
Traceback (most recent call last): 
  File "F:\Workspace\CallMonitoring\Sandbox Python Pipeline\VideoIDX-LoadCosmos.py", line 358, in <module>
    main()
    ~~~~^^
  File "F:\Workspace\CallMonitoring\Sandbox Python Pipeline\VideoIDX-LoadCosmos.py", line 304, in main
    videos = list_recent_mp4_blobs()
  File "F:\Workspace\CallMonitoring\Sandbox Python Pipeline\VideoIDX-LoadCosmos.py", line 137, in list_recent_mp4_blobs
    for blob in container.list_blobs():
                ~~~~~~~~~~~~~~~~~~~~^^
  File "C:\Program Files\Python314\Lib\site-packages\azure\core\paging.py", line 
136, in __next__
    return next(self._page_iterator)
  File "C:\Program Files\Python314\Lib\site-packages\azure\core\paging.py", line 
82, in __next__
    self._response = self._get_next(self.continuation_token)
                     ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Program Files\Python314\Lib\site-packages\azure\storage\blob\_list_blobs_helper.py", line 96, in _get_next_cb
    process_storage_error(error)
    ~~~~~~~~~~~~~~~~~~~~~^^^^^^^
  File "C:\Program Files\Python314\Lib\site-packages\azure\storage\blob\_shared\response_handlers.py", line 196, in process_storage_error
    raise error from None
azure.core.exceptions.HttpResponseError: This request is not authorized to perform this operation using this permission.
RequestId:260f5dee-401e-0029-45ff-f46283000000
Time:2026-06-05T15:26:00.7090370Z
ErrorCode:AuthorizationPermissionMismatch
Content: <?xml version="1.0" encoding="utf-8"?><Error><Code>AuthorizationPermissionMismatch</Code><Message>This request is not authorized to perform this operation using this permission.
RequestId:260f5dee-401e-0029-45ff-f46283000000
Time:2026-06-05T15:26:00.7090370Z</Message></Error>
PS F:\Workspace\CallMonitoring\Sandbox Python Pipeline> 

https://verbalabs.atlassian.net/wiki/spaces/v91/pages/9542087/Screen+capturing+features

PROJECT_ENDPOINT1="https://aifoundry-test-01.services.ai.azure.com/api/projects/Nitin-TestProject"
PROJECT_CONNECTION_STRING1="https://aifoundry-test-01.services.ai.azure.com/api/projects/Nitin-TestProject"

PROJECT_CONNECTION_STRING="https://aifoundrylab-01.services.ai.azure.com/api/projects/AIFoundryLab-01-Project"

MODEL_DEPLOYMENT_NAME="gpt-4.1"



AZURE_AI_ENDPOINT="https://aifoundrylab-01.services.ai.azure.com/"
# classic AZURE_AI_KEY="EyFqn4Qb5ZZ5o8NS9fnNI7LGRfjXqH6xvb1zCU0XQ0arQqcETxCKJQQJ99BLACYeBjFXJ3w3AAAAACOGHwu5"
AZURE_AI_KEY="EyFqn4Qb5ZZ5o8NS9fnNI7LGRfjXqH6xvb1zCU0XQ0arQqcETxCKJQQJ99BLACYeBjFXJ3w3AAAAACOGHwu5"

ANALYZER_ID= "CallQuality1"

 # "COO_Analysis1"
AZURE_STORAGE_CONNECTION_STRING = "https://aiinnovationstoragedev.blob.core.windows.net"
AZURE_STORAGE_ACCOUNT_NAME      =  "aiinnovationstoragedev"
AZURE_STORAGE_ACCOUNT_KEY       =  "" 
AZURE_BLOB_CONTAINER            = "labhrdocs"    
AZURE_STG_TABLE                 =    "cootable"


COSMOS_ENDPOINT = "https://cenlarcosmosdbpoc.documents.azure.com:443/"
COSMOS_KEY =  "KpiGvHNjh9eHWppmrDrBZTn3mb5cuWWbaDjjQHQ62Q5fi1zRqqOpazrpSuA2f3f1C3UqZrn8KEpJACDbgH74hQ=="


" 
# coo-documents   labhrdocs https://aifoundrylab-01.services.ai.azure.com/ https://aifoundrylab-01.openai.azure.com/openai/v1

