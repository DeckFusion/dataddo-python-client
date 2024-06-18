# GoogleMyBusinessStaticDtoAuthorizer


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
from openapi_client.models.google_my_business_static_dto_authorizer import GoogleMyBusinessStaticDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleMyBusinessStaticDtoAuthorizer from a JSON string
google_my_business_static_dto_authorizer_instance = GoogleMyBusinessStaticDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(GoogleMyBusinessStaticDtoAuthorizer.to_json())

# convert the object into a dict
google_my_business_static_dto_authorizer_dict = google_my_business_static_dto_authorizer_instance.to_dict()
# create an instance of GoogleMyBusinessStaticDtoAuthorizer from a dict
google_my_business_static_dto_authorizer_from_dict = GoogleMyBusinessStaticDtoAuthorizer.from_dict(google_my_business_static_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


