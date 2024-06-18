# GoogleAnalytics4StaticDtoAuthorizer


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
from openapi_client.models.google_analytics4_static_dto_authorizer import GoogleAnalytics4StaticDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAnalytics4StaticDtoAuthorizer from a JSON string
google_analytics4_static_dto_authorizer_instance = GoogleAnalytics4StaticDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(GoogleAnalytics4StaticDtoAuthorizer.to_json())

# convert the object into a dict
google_analytics4_static_dto_authorizer_dict = google_analytics4_static_dto_authorizer_instance.to_dict()
# create an instance of GoogleAnalytics4StaticDtoAuthorizer from a dict
google_analytics4_static_dto_authorizer_from_dict = GoogleAnalytics4StaticDtoAuthorizer.from_dict(google_analytics4_static_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


