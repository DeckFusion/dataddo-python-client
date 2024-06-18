# PanoplyStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 
**project_id** | **str** |  | [optional] 
**dataset_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.panoply_storage_request import PanoplyStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PanoplyStorageRequest from a JSON string
panoply_storage_request_instance = PanoplyStorageRequest.from_json(json)
# print the JSON string representation of the object
print(PanoplyStorageRequest.to_json())

# convert the object into a dict
panoply_storage_request_dict = panoply_storage_request_instance.to_dict()
# create an instance of PanoplyStorageRequest from a dict
panoply_storage_request_from_dict = PanoplyStorageRequest.from_dict(panoply_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


