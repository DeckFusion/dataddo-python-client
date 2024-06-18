# OneDriveStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**drive_id** | **str** |  | [optional] 
**tenant** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.one_drive_storage_request import OneDriveStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OneDriveStorageRequest from a JSON string
one_drive_storage_request_instance = OneDriveStorageRequest.from_json(json)
# print the JSON string representation of the object
print(OneDriveStorageRequest.to_json())

# convert the object into a dict
one_drive_storage_request_dict = one_drive_storage_request_instance.to_dict()
# create an instance of OneDriveStorageRequest from a dict
one_drive_storage_request_from_dict = OneDriveStorageRequest.from_dict(one_drive_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


