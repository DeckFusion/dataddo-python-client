# StorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.storage_request import StorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StorageRequest from a JSON string
storage_request_instance = StorageRequest.from_json(json)
# print the JSON string representation of the object
print(StorageRequest.to_json())

# convert the object into a dict
storage_request_dict = storage_request_instance.to_dict()
# create an instance of StorageRequest from a dict
storage_request_from_dict = StorageRequest.from_dict(storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


