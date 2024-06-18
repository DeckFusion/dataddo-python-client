# openapi_client.ServicesBlackDiamondApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_authorizer_black_diamond_black_diamond_authorizer_get_authorization_url**](ServicesBlackDiamondApi.md#app_authorizer_black_diamond_black_diamond_authorizer_get_authorization_url) | **POST** /services/black_diamond/oauth-request-url | Builds redirect URL


# **app_authorizer_black_diamond_black_diamond_authorizer_get_authorization_url**
> OAuthRequestUrlResponse app_authorizer_black_diamond_black_diamond_authorizer_get_authorization_url(app_authorizer_black_diamond_black_diamond_authorizer_get_authorization_url_request)

Builds redirect URL

### Example


```python
import openapi_client
from openapi_client.models.app_authorizer_black_diamond_black_diamond_authorizer_get_authorization_url_request import AppAuthorizerBlackDiamondBlackDiamondAuthorizerGetAuthorizationUrlRequest
from openapi_client.models.o_auth_request_url_response import OAuthRequestUrlResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://headless.dataddo.com/customer-api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://headless.dataddo.com/customer-api/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ServicesBlackDiamondApi(api_client)
    app_authorizer_black_diamond_black_diamond_authorizer_get_authorization_url_request = openapi_client.AppAuthorizerBlackDiamondBlackDiamondAuthorizerGetAuthorizationUrlRequest() # AppAuthorizerBlackDiamondBlackDiamondAuthorizerGetAuthorizationUrlRequest | 

    try:
        # Builds redirect URL
        api_response = api_instance.app_authorizer_black_diamond_black_diamond_authorizer_get_authorization_url(app_authorizer_black_diamond_black_diamond_authorizer_get_authorization_url_request)
        print("The response of ServicesBlackDiamondApi->app_authorizer_black_diamond_black_diamond_authorizer_get_authorization_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesBlackDiamondApi->app_authorizer_black_diamond_black_diamond_authorizer_get_authorization_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_authorizer_black_diamond_black_diamond_authorizer_get_authorization_url_request** | [**AppAuthorizerBlackDiamondBlackDiamondAuthorizerGetAuthorizationUrlRequest**](AppAuthorizerBlackDiamondBlackDiamondAuthorizerGetAuthorizationUrlRequest.md)|  | 

### Return type

[**OAuthRequestUrlResponse**](OAuthRequestUrlResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the redirect URL |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

