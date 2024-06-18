# CockroachDBStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.cockroach_db_storage_request import CockroachDBStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CockroachDBStorageRequest from a JSON string
cockroach_db_storage_request_instance = CockroachDBStorageRequest.from_json(json)
# print the JSON string representation of the object
print(CockroachDBStorageRequest.to_json())

# convert the object into a dict
cockroach_db_storage_request_dict = cockroach_db_storage_request_instance.to_dict()
# create an instance of CockroachDBStorageRequest from a dict
cockroach_db_storage_request_from_dict = CockroachDBStorageRequest.from_dict(cockroach_db_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


