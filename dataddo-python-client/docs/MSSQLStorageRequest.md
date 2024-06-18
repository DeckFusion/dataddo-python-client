# MSSQLStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.mssql_storage_request import MSSQLStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MSSQLStorageRequest from a JSON string
mssql_storage_request_instance = MSSQLStorageRequest.from_json(json)
# print the JSON string representation of the object
print(MSSQLStorageRequest.to_json())

# convert the object into a dict
mssql_storage_request_dict = mssql_storage_request_instance.to_dict()
# create an instance of MSSQLStorageRequest from a dict
mssql_storage_request_from_dict = MSSQLStorageRequest.from_dict(mssql_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


