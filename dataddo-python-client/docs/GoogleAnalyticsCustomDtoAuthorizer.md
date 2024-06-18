# GoogleAnalyticsCustomDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.google_analytics_custom_dto_authorizer import GoogleAnalyticsCustomDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAnalyticsCustomDtoAuthorizer from a JSON string
google_analytics_custom_dto_authorizer_instance = GoogleAnalyticsCustomDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(GoogleAnalyticsCustomDtoAuthorizer.to_json())

# convert the object into a dict
google_analytics_custom_dto_authorizer_dict = google_analytics_custom_dto_authorizer_instance.to_dict()
# create an instance of GoogleAnalyticsCustomDtoAuthorizer from a dict
google_analytics_custom_dto_authorizer_from_dict = GoogleAnalyticsCustomDtoAuthorizer.from_dict(google_analytics_custom_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


