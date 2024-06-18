# KlaviyoStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 
**object** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.klaviyo_storage_request import KlaviyoStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KlaviyoStorageRequest from a JSON string
klaviyo_storage_request_instance = KlaviyoStorageRequest.from_json(json)
# print the JSON string representation of the object
print(KlaviyoStorageRequest.to_json())

# convert the object into a dict
klaviyo_storage_request_dict = klaviyo_storage_request_instance.to_dict()
# create an instance of KlaviyoStorageRequest from a dict
klaviyo_storage_request_from_dict = KlaviyoStorageRequest.from_dict(klaviyo_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


