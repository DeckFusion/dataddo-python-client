# MySQLStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.my_sql_storage_request import MySQLStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MySQLStorageRequest from a JSON string
my_sql_storage_request_instance = MySQLStorageRequest.from_json(json)
# print the JSON string representation of the object
print(MySQLStorageRequest.to_json())

# convert the object into a dict
my_sql_storage_request_dict = my_sql_storage_request_instance.to_dict()
# create an instance of MySQLStorageRequest from a dict
my_sql_storage_request_from_dict = MySQLStorageRequest.from_dict(my_sql_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


