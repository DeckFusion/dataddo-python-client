# PgSQLStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.pg_sql_storage_request import PgSQLStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PgSQLStorageRequest from a JSON string
pg_sql_storage_request_instance = PgSQLStorageRequest.from_json(json)
# print the JSON string representation of the object
print(PgSQLStorageRequest.to_json())

# convert the object into a dict
pg_sql_storage_request_dict = pg_sql_storage_request_instance.to_dict()
# create an instance of PgSQLStorageRequest from a dict
pg_sql_storage_request_from_dict = PgSQLStorageRequest.from_dict(pg_sql_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


