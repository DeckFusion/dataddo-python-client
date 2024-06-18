# AppAuthorizerFacebookCustomFacebookCustomAuthorizerGetAuthorizationUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**AppAuthorizerFacebookCustomFacebookCustomAuthorizerGetAuthorizationUrlRequestConfig**](AppAuthorizerFacebookCustomFacebookCustomAuthorizerGetAuthorizationUrlRequestConfig.md) |  | 
**state** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_facebook_custom_facebook_custom_authorizer_get_authorization_url_request import AppAuthorizerFacebookCustomFacebookCustomAuthorizerGetAuthorizationUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerFacebookCustomFacebookCustomAuthorizerGetAuthorizationUrlRequest from a JSON string
app_authorizer_facebook_custom_facebook_custom_authorizer_get_authorization_url_request_instance = AppAuthorizerFacebookCustomFacebookCustomAuthorizerGetAuthorizationUrlRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerFacebookCustomFacebookCustomAuthorizerGetAuthorizationUrlRequest.to_json())

# convert the object into a dict
app_authorizer_facebook_custom_facebook_custom_authorizer_get_authorization_url_request_dict = app_authorizer_facebook_custom_facebook_custom_authorizer_get_authorization_url_request_instance.to_dict()
# create an instance of AppAuthorizerFacebookCustomFacebookCustomAuthorizerGetAuthorizationUrlRequest from a dict
app_authorizer_facebook_custom_facebook_custom_authorizer_get_authorization_url_request_from_dict = AppAuthorizerFacebookCustomFacebookCustomAuthorizerGetAuthorizationUrlRequest.from_dict(app_authorizer_facebook_custom_facebook_custom_authorizer_get_authorization_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


