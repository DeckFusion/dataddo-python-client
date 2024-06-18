# AppAuthorizerFacebookStaticFacebookStaticAuthorizerNewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'facebook_static']
**data** | [**FacebookStaticDtoAuthorizer**](FacebookStaticDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_facebook_static_facebook_static_authorizer_new_request import AppAuthorizerFacebookStaticFacebookStaticAuthorizerNewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerFacebookStaticFacebookStaticAuthorizerNewRequest from a JSON string
app_authorizer_facebook_static_facebook_static_authorizer_new_request_instance = AppAuthorizerFacebookStaticFacebookStaticAuthorizerNewRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerFacebookStaticFacebookStaticAuthorizerNewRequest.to_json())

# convert the object into a dict
app_authorizer_facebook_static_facebook_static_authorizer_new_request_dict = app_authorizer_facebook_static_facebook_static_authorizer_new_request_instance.to_dict()
# create an instance of AppAuthorizerFacebookStaticFacebookStaticAuthorizerNewRequest from a dict
app_authorizer_facebook_static_facebook_static_authorizer_new_request_from_dict = AppAuthorizerFacebookStaticFacebookStaticAuthorizerNewRequest.from_dict(app_authorizer_facebook_static_facebook_static_authorizer_new_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


