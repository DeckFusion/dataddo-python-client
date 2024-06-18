# GoogleCloudStorageDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**last_use** | **datetime** |  | [optional] 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**status_detail** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 
**bucket** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.google_cloud_storage_destination import GoogleCloudStorageDestination

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCloudStorageDestination from a JSON string
google_cloud_storage_destination_instance = GoogleCloudStorageDestination.from_json(json)
# print the JSON string representation of the object
print(GoogleCloudStorageDestination.to_json())

# convert the object into a dict
google_cloud_storage_destination_dict = google_cloud_storage_destination_instance.to_dict()
# create an instance of GoogleCloudStorageDestination from a dict
google_cloud_storage_destination_from_dict = GoogleCloudStorageDestination.from_dict(google_cloud_storage_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


