# FireboltStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.firebolt_storage_request import FireboltStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FireboltStorageRequest from a JSON string
firebolt_storage_request_instance = FireboltStorageRequest.from_json(json)
# print the JSON string representation of the object
print(FireboltStorageRequest.to_json())

# convert the object into a dict
firebolt_storage_request_dict = firebolt_storage_request_instance.to_dict()
# create an instance of FireboltStorageRequest from a dict
firebolt_storage_request_from_dict = FireboltStorageRequest.from_dict(firebolt_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


