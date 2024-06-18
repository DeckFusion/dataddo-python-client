# PipedreamStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.pipedream_storage_request import PipedreamStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PipedreamStorageRequest from a JSON string
pipedream_storage_request_instance = PipedreamStorageRequest.from_json(json)
# print the JSON string representation of the object
print(PipedreamStorageRequest.to_json())

# convert the object into a dict
pipedream_storage_request_dict = pipedream_storage_request_instance.to_dict()
# create an instance of PipedreamStorageRequest from a dict
pipedream_storage_request_from_dict = PipedreamStorageRequest.from_dict(pipedream_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


