# SnowflakeStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.snowflake_storage_request import SnowflakeStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeStorageRequest from a JSON string
snowflake_storage_request_instance = SnowflakeStorageRequest.from_json(json)
# print the JSON string representation of the object
print(SnowflakeStorageRequest.to_json())

# convert the object into a dict
snowflake_storage_request_dict = snowflake_storage_request_instance.to_dict()
# create an instance of SnowflakeStorageRequest from a dict
snowflake_storage_request_from_dict = SnowflakeStorageRequest.from_dict(snowflake_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


