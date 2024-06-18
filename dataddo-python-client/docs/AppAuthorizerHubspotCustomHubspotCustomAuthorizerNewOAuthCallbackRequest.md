# AppAuthorizerHubspotCustomHubspotCustomAuthorizerNewOAuthCallbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** |  | [optional] [default to 'https://my.app.com/callback?code=aaaaBBBBccc1234']
**config** | [**HubspotCustomDtoAuthorizer**](HubspotCustomDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_hubspot_custom_hubspot_custom_authorizer_new_o_auth_callback_request import AppAuthorizerHubspotCustomHubspotCustomAuthorizerNewOAuthCallbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerHubspotCustomHubspotCustomAuthorizerNewOAuthCallbackRequest from a JSON string
app_authorizer_hubspot_custom_hubspot_custom_authorizer_new_o_auth_callback_request_instance = AppAuthorizerHubspotCustomHubspotCustomAuthorizerNewOAuthCallbackRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerHubspotCustomHubspotCustomAuthorizerNewOAuthCallbackRequest.to_json())

# convert the object into a dict
app_authorizer_hubspot_custom_hubspot_custom_authorizer_new_o_auth_callback_request_dict = app_authorizer_hubspot_custom_hubspot_custom_authorizer_new_o_auth_callback_request_instance.to_dict()
# create an instance of AppAuthorizerHubspotCustomHubspotCustomAuthorizerNewOAuthCallbackRequest from a dict
app_authorizer_hubspot_custom_hubspot_custom_authorizer_new_o_auth_callback_request_from_dict = AppAuthorizerHubspotCustomHubspotCustomAuthorizerNewOAuthCallbackRequest.from_dict(app_authorizer_hubspot_custom_hubspot_custom_authorizer_new_o_auth_callback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


