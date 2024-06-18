# AppAuthorizerBlackDiamondBlackDiamondAuthorizerGetAuthorizationUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**AppAuthorizerBlackDiamondBlackDiamondAuthorizerGetAuthorizationUrlRequestConfig**](AppAuthorizerBlackDiamondBlackDiamondAuthorizerGetAuthorizationUrlRequestConfig.md) |  | [optional] 
**state** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_black_diamond_black_diamond_authorizer_get_authorization_url_request import AppAuthorizerBlackDiamondBlackDiamondAuthorizerGetAuthorizationUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerBlackDiamondBlackDiamondAuthorizerGetAuthorizationUrlRequest from a JSON string
app_authorizer_black_diamond_black_diamond_authorizer_get_authorization_url_request_instance = AppAuthorizerBlackDiamondBlackDiamondAuthorizerGetAuthorizationUrlRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerBlackDiamondBlackDiamondAuthorizerGetAuthorizationUrlRequest.to_json())

# convert the object into a dict
app_authorizer_black_diamond_black_diamond_authorizer_get_authorization_url_request_dict = app_authorizer_black_diamond_black_diamond_authorizer_get_authorization_url_request_instance.to_dict()
# create an instance of AppAuthorizerBlackDiamondBlackDiamondAuthorizerGetAuthorizationUrlRequest from a dict
app_authorizer_black_diamond_black_diamond_authorizer_get_authorization_url_request_from_dict = AppAuthorizerBlackDiamondBlackDiamondAuthorizerGetAuthorizationUrlRequest.from_dict(app_authorizer_black_diamond_black_diamond_authorizer_get_authorization_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


