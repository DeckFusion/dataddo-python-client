# openapi_client.ServicesSnapchatCustomApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_authorizer_snapchat_custom_snapchat_custom_authorizer_get_authorization_url**](ServicesSnapchatCustomApi.md#app_authorizer_snapchat_custom_snapchat_custom_authorizer_get_authorization_url) | **POST** /services/snapchat_custom/oauth-request-url | Builds redirect URL
[**app_authorizer_snapchat_custom_snapchat_custom_authorizer_new_o_auth_callback**](ServicesSnapchatCustomApi.md#app_authorizer_snapchat_custom_snapchat_custom_authorizer_new_o_auth_callback) | **POST** /services/snapchat_custom/oauth-process-callback | Processes callback URL


# **app_authorizer_snapchat_custom_snapchat_custom_authorizer_get_authorization_url**
> OAuthRequestUrlResponse app_authorizer_snapchat_custom_snapchat_custom_authorizer_get_authorization_url(app_authorizer_pinterest_custom_pinterest_custom_authorizer_get_authorization_url_request)

Builds redirect URL

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
    api_instance = openapi_client.ServicesSnapchatCustomApi(api_client)
    app_authorizer_pinterest_custom_pinterest_custom_authorizer_get_authorization_url_request = openapi_client.AppAuthorizerPinterestCustomPinterestCustomAuthorizerGetAuthorizationUrlRequest() # AppAuthorizerPinterestCustomPinterestCustomAuthorizerGetAuthorizationUrlRequest | 

    try:
        # Builds redirect URL
        api_response = api_instance.app_authorizer_snapchat_custom_snapchat_custom_authorizer_get_authorization_url(app_authorizer_pinterest_custom_pinterest_custom_authorizer_get_authorization_url_request)
        print("The response of ServicesSnapchatCustomApi->app_authorizer_snapchat_custom_snapchat_custom_authorizer_get_authorization_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesSnapchatCustomApi->app_authorizer_snapchat_custom_snapchat_custom_authorizer_get_authorization_url: %s\n" % e)
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

# **app_authorizer_snapchat_custom_snapchat_custom_authorizer_new_o_auth_callback**
> SnapchatCustomUserAuth app_authorizer_snapchat_custom_snapchat_custom_authorizer_new_o_auth_callback(app_authorizer_snapchat_custom_snapchat_custom_authorizer_new_o_auth_callback_request)

Processes callback URL

### Example


```python
import openapi_client
from openapi_client.models.app_authorizer_snapchat_custom_snapchat_custom_authorizer_new_o_auth_callback_request import AppAuthorizerSnapchatCustomSnapchatCustomAuthorizerNewOAuthCallbackRequest
from openapi_client.models.snapchat_custom_user_auth import SnapchatCustomUserAuth
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
    api_instance = openapi_client.ServicesSnapchatCustomApi(api_client)
    app_authorizer_snapchat_custom_snapchat_custom_authorizer_new_o_auth_callback_request = openapi_client.AppAuthorizerSnapchatCustomSnapchatCustomAuthorizerNewOAuthCallbackRequest() # AppAuthorizerSnapchatCustomSnapchatCustomAuthorizerNewOAuthCallbackRequest | 

    try:
        # Processes callback URL
        api_response = api_instance.app_authorizer_snapchat_custom_snapchat_custom_authorizer_new_o_auth_callback(app_authorizer_snapchat_custom_snapchat_custom_authorizer_new_o_auth_callback_request)
        print("The response of ServicesSnapchatCustomApi->app_authorizer_snapchat_custom_snapchat_custom_authorizer_new_o_auth_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesSnapchatCustomApi->app_authorizer_snapchat_custom_snapchat_custom_authorizer_new_o_auth_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_authorizer_snapchat_custom_snapchat_custom_authorizer_new_o_auth_callback_request** | [**AppAuthorizerSnapchatCustomSnapchatCustomAuthorizerNewOAuthCallbackRequest**](AppAuthorizerSnapchatCustomSnapchatCustomAuthorizerNewOAuthCallbackRequest.md)|  | 

### Return type

[**SnapchatCustomUserAuth**](SnapchatCustomUserAuth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

