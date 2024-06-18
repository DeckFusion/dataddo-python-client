# DataboxStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.databox_storage_request import DataboxStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataboxStorageRequest from a JSON string
databox_storage_request_instance = DataboxStorageRequest.from_json(json)
# print the JSON string representation of the object
print(DataboxStorageRequest.to_json())

# convert the object into a dict
databox_storage_request_dict = databox_storage_request_instance.to_dict()
# create an instance of DataboxStorageRequest from a dict
databox_storage_request_from_dict = DataboxStorageRequest.from_dict(databox_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


