# AppAuthorizerQuickbooksCustomQuickbooksCustomAuthorizerNewOAuthCallbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** |  | [optional] [default to 'https://my.app.com/callback?code=aaaaBBBBccc1234']
**config** | [**QuickbooksCustomDtoAuthorizer**](QuickbooksCustomDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_quickbooks_custom_quickbooks_custom_authorizer_new_o_auth_callback_request import AppAuthorizerQuickbooksCustomQuickbooksCustomAuthorizerNewOAuthCallbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerQuickbooksCustomQuickbooksCustomAuthorizerNewOAuthCallbackRequest from a JSON string
app_authorizer_quickbooks_custom_quickbooks_custom_authorizer_new_o_auth_callback_request_instance = AppAuthorizerQuickbooksCustomQuickbooksCustomAuthorizerNewOAuthCallbackRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerQuickbooksCustomQuickbooksCustomAuthorizerNewOAuthCallbackRequest.to_json())

# convert the object into a dict
app_authorizer_quickbooks_custom_quickbooks_custom_authorizer_new_o_auth_callback_request_dict = app_authorizer_quickbooks_custom_quickbooks_custom_authorizer_new_o_auth_callback_request_instance.to_dict()
# create an instance of AppAuthorizerQuickbooksCustomQuickbooksCustomAuthorizerNewOAuthCallbackRequest from a dict
app_authorizer_quickbooks_custom_quickbooks_custom_authorizer_new_o_auth_callback_request_from_dict = AppAuthorizerQuickbooksCustomQuickbooksCustomAuthorizerNewOAuthCallbackRequest.from_dict(app_authorizer_quickbooks_custom_quickbooks_custom_authorizer_new_o_auth_callback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


