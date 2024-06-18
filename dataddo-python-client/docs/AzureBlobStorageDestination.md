# AzureBlobStorageDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**last_use** | **datetime** |  | [optional] 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**status_detail** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.azure_blob_storage_destination import AzureBlobStorageDestination

# TODO update the JSON string below
json = "{}"
# create an instance of AzureBlobStorageDestination from a JSON string
azure_blob_storage_destination_instance = AzureBlobStorageDestination.from_json(json)
# print the JSON string representation of the object
print(AzureBlobStorageDestination.to_json())

# convert the object into a dict
azure_blob_storage_destination_dict = azure_blob_storage_destination_instance.to_dict()
# create an instance of AzureBlobStorageDestination from a dict
azure_blob_storage_destination_from_dict = AzureBlobStorageDestination.from_dict(azure_blob_storage_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


