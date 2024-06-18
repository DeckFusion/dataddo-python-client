# GoogleSheetsCustomDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.google_sheets_custom_dto_authorizer import GoogleSheetsCustomDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleSheetsCustomDtoAuthorizer from a JSON string
google_sheets_custom_dto_authorizer_instance = GoogleSheetsCustomDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(GoogleSheetsCustomDtoAuthorizer.to_json())

# convert the object into a dict
google_sheets_custom_dto_authorizer_dict = google_sheets_custom_dto_authorizer_instance.to_dict()
# create an instance of GoogleSheetsCustomDtoAuthorizer from a dict
google_sheets_custom_dto_authorizer_from_dict = GoogleSheetsCustomDtoAuthorizer.from_dict(google_sheets_custom_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


