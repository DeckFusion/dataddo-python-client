# GoogleSheetsStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.google_sheets_storage_request import GoogleSheetsStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleSheetsStorageRequest from a JSON string
google_sheets_storage_request_instance = GoogleSheetsStorageRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleSheetsStorageRequest.to_json())

# convert the object into a dict
google_sheets_storage_request_dict = google_sheets_storage_request_instance.to_dict()
# create an instance of GoogleSheetsStorageRequest from a dict
google_sheets_storage_request_from_dict = GoogleSheetsStorageRequest.from_dict(google_sheets_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


