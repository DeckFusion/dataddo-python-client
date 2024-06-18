# ClickhouseStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.clickhouse_storage_request import ClickhouseStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClickhouseStorageRequest from a JSON string
clickhouse_storage_request_instance = ClickhouseStorageRequest.from_json(json)
# print the JSON string representation of the object
print(ClickhouseStorageRequest.to_json())

# convert the object into a dict
clickhouse_storage_request_dict = clickhouse_storage_request_instance.to_dict()
# create an instance of ClickhouseStorageRequest from a dict
clickhouse_storage_request_from_dict = ClickhouseStorageRequest.from_dict(clickhouse_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


