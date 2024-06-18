# openapi_client.ServicesMicrosoftSharePointApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_authorizer_microsoft_share_point_microsoft_share_point_authorizer_get_authorization_url**](ServicesMicrosoftSharePointApi.md#app_authorizer_microsoft_share_point_microsoft_share_point_authorizer_get_authorization_url) | **POST** /services/microsoft_share_point/oauth-request-url | Builds redirect URL


# **app_authorizer_microsoft_share_point_microsoft_share_point_authorizer_get_authorization_url**
> OAuthRequestUrlResponse app_authorizer_microsoft_share_point_microsoft_share_point_authorizer_get_authorization_url(app_authorizer_microsoft_share_point_microsoft_share_point_authorizer_get_authorization_url_request)

Builds redirect URL

### Example


```python
import openapi_client
from openapi_client.models.app_authorizer_microsoft_share_point_microsoft_share_point_authorizer_get_authorization_url_request import AppAuthorizerMicrosoftSharePointMicrosoftSharePointAuthorizerGetAuthorizationUrlRequest
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
    api_instance = openapi_client.ServicesMicrosoftSharePointApi(api_client)
    app_authorizer_microsoft_share_point_microsoft_share_point_authorizer_get_authorization_url_request = openapi_client.AppAuthorizerMicrosoftSharePointMicrosoftSharePointAuthorizerGetAuthorizationUrlRequest() # AppAuthorizerMicrosoftSharePointMicrosoftSharePointAuthorizerGetAuthorizationUrlRequest | 

    try:
        # Builds redirect URL
        api_response = api_instance.app_authorizer_microsoft_share_point_microsoft_share_point_authorizer_get_authorization_url(app_authorizer_microsoft_share_point_microsoft_share_point_authorizer_get_authorization_url_request)
        print("The response of ServicesMicrosoftSharePointApi->app_authorizer_microsoft_share_point_microsoft_share_point_authorizer_get_authorization_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesMicrosoftSharePointApi->app_authorizer_microsoft_share_point_microsoft_share_point_authorizer_get_authorization_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_authorizer_microsoft_share_point_microsoft_share_point_authorizer_get_authorization_url_request** | [**AppAuthorizerMicrosoftSharePointMicrosoftSharePointAuthorizerGetAuthorizationUrlRequest**](AppAuthorizerMicrosoftSharePointMicrosoftSharePointAuthorizerGetAuthorizationUrlRequest.md)|  | 

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

