# An attempt to build a framework to help understand how ACL and RBAC influences interactions with ADLS Gen 2
using the Python SDK and some Azure CLI

## Things you need to make this work

An HNS enabled storage account.

Some service principals: 

    az ad sp create-for-rbac -n "spname" --scopes /subscriptions/your-sub/resourceGroups/your-rg
This will return some JSON, which you should save in an .id file. 

Included is an example of this with .id.json extension. The used id files with secrets are excluded via gitignore.

Start with running tests from test_aad_adls module

## Useful URLs

https://github.com/Azure/azure-sdk-for-python/blob/master/sdk/storage/azure-storage-file-datalake/samples/datalake_samples_file_system.py

https://docs.microsoft.com/en-us/azure/developer/python/azure-sdk-authenticate?tabs=cmd

https://github.com/hurtn/datalake-on-ADLS/blob/master/Understanding%20access%20control%20and%20data%20lake%20configurations%20in%20ADLS%20Gen2.md

https://github.com/Azure-Samples/ms-identity-python-daemon/blob/master/1-Call-MsGraph-WithSecret/AppCreationScripts/AppCreationScripts.md

https://docs.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-access-control#common-scenarios-related-to-permissions



## Requirement

requirement created with 
py -m pip freeze > requirements.txt


