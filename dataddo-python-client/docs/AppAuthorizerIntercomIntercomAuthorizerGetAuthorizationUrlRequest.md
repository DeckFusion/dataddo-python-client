# AppAuthorizerIntercomIntercomAuthorizerGetAuthorizationUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**AppAuthorizerIntercomIntercomAuthorizerGetAuthorizationUrlRequestConfig**](AppAuthorizerIntercomIntercomAuthorizerGetAuthorizationUrlRequestConfig.md) |  | 
**state** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_intercom_intercom_authorizer_get_authorization_url_request import AppAuthorizerIntercomIntercomAuthorizerGetAuthorizationUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerIntercomIntercomAuthorizerGetAuthorizationUrlRequest from a JSON string
app_authorizer_intercom_intercom_authorizer_get_authorization_url_request_instance = AppAuthorizerIntercomIntercomAuthorizerGetAuthorizationUrlRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerIntercomIntercomAuthorizerGetAuthorizationUrlRequest.to_json())

# convert the object into a dict
app_authorizer_intercom_intercom_authorizer_get_authorization_url_request_dict = app_authorizer_intercom_intercom_authorizer_get_authorization_url_request_instance.to_dict()
# create an instance of AppAuthorizerIntercomIntercomAuthorizerGetAuthorizationUrlRequest from a dict
app_authorizer_intercom_intercom_authorizer_get_authorization_url_request_from_dict = AppAuthorizerIntercomIntercomAuthorizerGetAuthorizationUrlRequest.from_dict(app_authorizer_intercom_intercom_authorizer_get_authorization_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

