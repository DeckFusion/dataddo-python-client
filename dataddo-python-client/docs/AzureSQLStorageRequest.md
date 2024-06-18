# AzureSQLStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.azure_sql_storage_request import AzureSQLStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSQLStorageRequest from a JSON string
azure_sql_storage_request_instance = AzureSQLStorageRequest.from_json(json)
# print the JSON string representation of the object
print(AzureSQLStorageRequest.to_json())

# convert the object into a dict
azure_sql_storage_request_dict = azure_sql_storage_request_instance.to_dict()
# create an instance of AzureSQLStorageRequest from a dict
azure_sql_storage_request_from_dict = AzureSQLStorageRequest.from_dict(azure_sql_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


