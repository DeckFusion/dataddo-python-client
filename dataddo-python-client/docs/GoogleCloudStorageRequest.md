# GoogleCloudStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 
**bucket** | **str** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.google_cloud_storage_request import GoogleCloudStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudStorageRequest from a JSON string
google_cloud_storage_request_instance = GoogleCloudStorageRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudStorageRequest.to_json())

# convert the object into a dict
google_cloud_storage_request_dict = google_cloud_storage_request_instance.to_dict()
# create an instance of GoogleCloudStorageRequest from a dict
google_cloud_storage_request_from_dict = GoogleCloudStorageRequest.from_dict(google_cloud_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


