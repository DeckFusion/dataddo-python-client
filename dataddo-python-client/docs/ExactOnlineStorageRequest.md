# ExactOnlineStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 
**endpoint** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.exact_online_storage_request import ExactOnlineStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ExactOnlineStorageRequest from a JSON string
exact_online_storage_request_instance = ExactOnlineStorageRequest.from_json(json)
# print the JSON string representation of the object
print(ExactOnlineStorageRequest.to_json())

# convert the object into a dict
exact_online_storage_request_dict = exact_online_storage_request_instance.to_dict()
# create an instance of ExactOnlineStorageRequest from a dict
exact_online_storage_request_from_dict = ExactOnlineStorageRequest.from_dict(exact_online_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


