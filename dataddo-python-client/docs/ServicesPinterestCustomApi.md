# openapi_client.ServicesPinterestCustomApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_authorizer_pinterest_custom_pinterest_custom_authorizer_get_authorization_url**](ServicesPinterestCustomApi.md#app_authorizer_pinterest_custom_pinterest_custom_authorizer_get_authorization_url) | **POST** /services/pinterest_custom/oauth-request-url | Get url for service authentication


# **app_authorizer_pinterest_custom_pinterest_custom_authorizer_get_authorization_url**
> OAuthRequestUrlResponse app_authorizer_pinterest_custom_pinterest_custom_authorizer_get_authorization_url(app_authorizer_pinterest_custom_pinterest_custom_authorizer_get_authorization_url_request)

Get url for service authentication

### Example


```python
import openapi_client
from openapi_client.models.app_authorizer_pinterest_custom_pinterest_custom_authorizer_get_authorization_url_request import AppAuthorizerPinterestCustomPinterestCustomAuthorizerGetAuthorizationUrlRequest
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
    api_instance = openapi_client.ServicesPinterestCustomApi(api_client)
    app_authorizer_pinterest_custom_pinterest_custom_authorizer_get_authorization_url_request = openapi_client.AppAuthorizerPinterestCustomPinterestCustomAuthorizerGetAuthorizationUrlRequest() # AppAuthorizerPinterestCustomPinterestCustomAuthorizerGetAuthorizationUrlRequest | 

    try:
        # Get url for service authentication
        api_response = api_instance.app_authorizer_pinterest_custom_pinterest_custom_authorizer_get_authorization_url(app_authorizer_pinterest_custom_pinterest_custom_authorizer_get_authorization_url_request)
        print("The response of ServicesPinterestCustomApi->app_authorizer_pinterest_custom_pinterest_custom_authorizer_get_authorization_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesPinterestCustomApi->app_authorizer_pinterest_custom_pinterest_custom_authorizer_get_authorization_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_authorizer_pinterest_custom_pinterest_custom_authorizer_get_authorization_url_request** | [**AppAuthorizerPinterestCustomPinterestCustomAuthorizerGetAuthorizationUrlRequest**](AppAuthorizerPinterestCustomPinterestCustomAuthorizerGetAuthorizationUrlRequest.md)|  | 

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

