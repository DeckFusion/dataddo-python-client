# HttpStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.http_storage_request import HttpStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HttpStorageRequest from a JSON string
http_storage_request_instance = HttpStorageRequest.from_json(json)
# print the JSON string representation of the object
print(HttpStorageRequest.to_json())

# convert the object into a dict
http_storage_request_dict = http_storage_request_instance.to_dict()
# create an instance of HttpStorageRequest from a dict
http_storage_request_from_dict = HttpStorageRequest.from_dict(http_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


