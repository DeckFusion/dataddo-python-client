# GoogleBigQueryStorageRequest


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
from openapi_client.models.google_big_query_storage_request import GoogleBigQueryStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleBigQueryStorageRequest from a JSON string
google_big_query_storage_request_instance = GoogleBigQueryStorageRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleBigQueryStorageRequest.to_json())

# convert the object into a dict
google_big_query_storage_request_dict = google_big_query_storage_request_instance.to_dict()
# create an instance of GoogleBigQueryStorageRequest from a dict
google_big_query_storage_request_from_dict = GoogleBigQueryStorageRequest.from_dict(google_big_query_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


