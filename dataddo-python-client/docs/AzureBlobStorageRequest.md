# AzureBlobStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_blob_storage_request import AzureBlobStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AzureBlobStorageRequest from a JSON string
azure_blob_storage_request_instance = AzureBlobStorageRequest.from_json(json)
# print the JSON string representation of the object
print(AzureBlobStorageRequest.to_json())

# convert the object into a dict
azure_blob_storage_request_dict = azure_blob_storage_request_instance.to_dict()
# create an instance of AzureBlobStorageRequest from a dict
azure_blob_storage_request_from_dict = AzureBlobStorageRequest.from_dict(azure_blob_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


