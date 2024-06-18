# AppAuthorizerTwitterCustomTwitterCustomAuthorizerNewOAuthCallbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** |  | [optional] [default to 'https://my.app.com/callback?code=aaaaBBBBccc1234']
**config** | [**TwitterCustomDtoAuthorizer**](TwitterCustomDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_twitter_custom_twitter_custom_authorizer_new_o_auth_callback_request import AppAuthorizerTwitterCustomTwitterCustomAuthorizerNewOAuthCallbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerTwitterCustomTwitterCustomAuthorizerNewOAuthCallbackRequest from a JSON string
app_authorizer_twitter_custom_twitter_custom_authorizer_new_o_auth_callback_request_instance = AppAuthorizerTwitterCustomTwitterCustomAuthorizerNewOAuthCallbackRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerTwitterCustomTwitterCustomAuthorizerNewOAuthCallbackRequest.to_json())

# convert the object into a dict
app_authorizer_twitter_custom_twitter_custom_authorizer_new_o_auth_callback_request_dict = app_authorizer_twitter_custom_twitter_custom_authorizer_new_o_auth_callback_request_instance.to_dict()
# create an instance of AppAuthorizerTwitterCustomTwitterCustomAuthorizerNewOAuthCallbackRequest from a dict
app_authorizer_twitter_custom_twitter_custom_authorizer_new_o_auth_callback_request_from_dict = AppAuthorizerTwitterCustomTwitterCustomAuthorizerNewOAuthCallbackRequest.from_dict(app_authorizer_twitter_custom_twitter_custom_authorizer_new_o_auth_callback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


