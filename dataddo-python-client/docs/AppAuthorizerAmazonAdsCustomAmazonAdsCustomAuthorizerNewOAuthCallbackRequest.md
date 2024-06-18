# AppAuthorizerAmazonAdsCustomAmazonAdsCustomAuthorizerNewOAuthCallbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** |  | [optional] [default to 'https://my.app.com/callback?code=aaaaBBBBccc1234']
**config** | [**AmazonAdsCustomDtoAuthorizer**](AmazonAdsCustomDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_amazon_ads_custom_amazon_ads_custom_authorizer_new_o_auth_callback_request import AppAuthorizerAmazonAdsCustomAmazonAdsCustomAuthorizerNewOAuthCallbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerAmazonAdsCustomAmazonAdsCustomAuthorizerNewOAuthCallbackRequest from a JSON string
app_authorizer_amazon_ads_custom_amazon_ads_custom_authorizer_new_o_auth_callback_request_instance = AppAuthorizerAmazonAdsCustomAmazonAdsCustomAuthorizerNewOAuthCallbackRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerAmazonAdsCustomAmazonAdsCustomAuthorizerNewOAuthCallbackRequest.to_json())

# convert the object into a dict
app_authorizer_amazon_ads_custom_amazon_ads_custom_authorizer_new_o_auth_callback_request_dict = app_authorizer_amazon_ads_custom_amazon_ads_custom_authorizer_new_o_auth_callback_request_instance.to_dict()
# create an instance of AppAuthorizerAmazonAdsCustomAmazonAdsCustomAuthorizerNewOAuthCallbackRequest from a dict
app_authorizer_amazon_ads_custom_amazon_ads_custom_authorizer_new_o_auth_callback_request_from_dict = AppAuthorizerAmazonAdsCustomAmazonAdsCustomAuthorizerNewOAuthCallbackRequest.from_dict(app_authorizer_amazon_ads_custom_amazon_ads_custom_authorizer_new_o_auth_callback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


