# GoogleAnalyticsStaticDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**static_key** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.google_analytics_static_dto_authorizer import GoogleAnalyticsStaticDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAnalyticsStaticDtoAuthorizer from a JSON string
google_analytics_static_dto_authorizer_instance = GoogleAnalyticsStaticDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(GoogleAnalyticsStaticDtoAuthorizer.to_json())

# convert the object into a dict
google_analytics_static_dto_authorizer_dict = google_analytics_static_dto_authorizer_instance.to_dict()
# create an instance of GoogleAnalyticsStaticDtoAuthorizer from a dict
google_analytics_static_dto_authorizer_from_dict = GoogleAnalyticsStaticDtoAuthorizer.from_dict(google_analytics_static_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


