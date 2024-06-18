# AppAuthorizerFacebookPageAccessTokenFacebookPageAccessTokenAuthorizerNewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'facebook_page_access_token']
**data** | [**FacebookPagesAccessTokenDtoAuthorizer**](FacebookPagesAccessTokenDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_facebook_page_access_token_facebook_page_access_token_authorizer_new_request import AppAuthorizerFacebookPageAccessTokenFacebookPageAccessTokenAuthorizerNewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerFacebookPageAccessTokenFacebookPageAccessTokenAuthorizerNewRequest from a JSON string
app_authorizer_facebook_page_access_token_facebook_page_access_token_authorizer_new_request_instance = AppAuthorizerFacebookPageAccessTokenFacebookPageAccessTokenAuthorizerNewRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerFacebookPageAccessTokenFacebookPageAccessTokenAuthorizerNewRequest.to_json())

# convert the object into a dict
app_authorizer_facebook_page_access_token_facebook_page_access_token_authorizer_new_request_dict = app_authorizer_facebook_page_access_token_facebook_page_access_token_authorizer_new_request_instance.to_dict()
# create an instance of AppAuthorizerFacebookPageAccessTokenFacebookPageAccessTokenAuthorizerNewRequest from a dict
app_authorizer_facebook_page_access_token_facebook_page_access_token_authorizer_new_request_from_dict = AppAuthorizerFacebookPageAccessTokenFacebookPageAccessTokenAuthorizerNewRequest.from_dict(app_authorizer_facebook_page_access_token_facebook_page_access_token_authorizer_new_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


