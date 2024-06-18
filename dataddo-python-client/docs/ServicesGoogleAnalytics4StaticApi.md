# openapi_client.ServicesGoogleAnalytics4StaticApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_authorizer_google_analytics4_static_google_analytics4_static_authorizer_new**](ServicesGoogleAnalytics4StaticApi.md#app_authorizer_google_analytics4_static_google_analytics4_static_authorizer_new) | **POST** /services/google_analytics4_static | Authorize a service
[**app_authorizer_shoptet_shoptet_authorizer_new**](ServicesGoogleAnalytics4StaticApi.md#app_authorizer_shoptet_shoptet_authorizer_new) | **POST** /services/shoptet | Authorize a service


# **app_authorizer_google_analytics4_static_google_analytics4_static_authorizer_new**
> GoogleAnalytics4StaticUserAuth app_authorizer_google_analytics4_static_google_analytics4_static_authorizer_new(app_authorizer_google_analytics4_static_google_analytics4_static_authorizer_new_request)

Authorize a service

### Example


```python
import openapi_client
from openapi_client.models.app_authorizer_google_analytics4_static_google_analytics4_static_authorizer_new_request import AppAuthorizerGoogleAnalytics4StaticGoogleAnalytics4StaticAuthorizerNewRequest
from openapi_client.models.google_analytics4_static_user_auth import GoogleAnalytics4StaticUserAuth
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
    api_instance = openapi_client.ServicesGoogleAnalytics4StaticApi(api_client)
    app_authorizer_google_analytics4_static_google_analytics4_static_authorizer_new_request = openapi_client.AppAuthorizerGoogleAnalytics4StaticGoogleAnalytics4StaticAuthorizerNewRequest() # AppAuthorizerGoogleAnalytics4StaticGoogleAnalytics4StaticAuthorizerNewRequest | 

    try:
        # Authorize a service
        api_response = api_instance.app_authorizer_google_analytics4_static_google_analytics4_static_authorizer_new(app_authorizer_google_analytics4_static_google_analytics4_static_authorizer_new_request)
        print("The response of ServicesGoogleAnalytics4StaticApi->app_authorizer_google_analytics4_static_google_analytics4_static_authorizer_new:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesGoogleAnalytics4StaticApi->app_authorizer_google_analytics4_static_google_analytics4_static_authorizer_new: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_authorizer_google_analytics4_static_google_analytics4_static_authorizer_new_request** | [**AppAuthorizerGoogleAnalytics4StaticGoogleAnalytics4StaticAuthorizerNewRequest**](AppAuthorizerGoogleAnalytics4StaticGoogleAnalytics4StaticAuthorizerNewRequest.md)|  | 

### Return type

[**GoogleAnalytics4StaticUserAuth**](GoogleAnalytics4StaticUserAuth.md)

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

# **app_authorizer_shoptet_shoptet_authorizer_new**
> GoogleAnalytics4StaticUserAuth app_authorizer_shoptet_shoptet_authorizer_new(app_authorizer_shoptet_shoptet_authorizer_new_request)

Authorize a service

### Example


```python
import openapi_client
from openapi_client.models.app_authorizer_shoptet_shoptet_authorizer_new_request import AppAuthorizerShoptetShoptetAuthorizerNewRequest
from openapi_client.models.google_analytics4_static_user_auth import GoogleAnalytics4StaticUserAuth
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
    api_instance = openapi_client.ServicesGoogleAnalytics4StaticApi(api_client)
    app_authorizer_shoptet_shoptet_authorizer_new_request = openapi_client.AppAuthorizerShoptetShoptetAuthorizerNewRequest() # AppAuthorizerShoptetShoptetAuthorizerNewRequest | 

    try:
        # Authorize a service
        api_response = api_instance.app_authorizer_shoptet_shoptet_authorizer_new(app_authorizer_shoptet_shoptet_authorizer_new_request)
        print("The response of ServicesGoogleAnalytics4StaticApi->app_authorizer_shoptet_shoptet_authorizer_new:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesGoogleAnalytics4StaticApi->app_authorizer_shoptet_shoptet_authorizer_new: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_authorizer_shoptet_shoptet_authorizer_new_request** | [**AppAuthorizerShoptetShoptetAuthorizerNewRequest**](AppAuthorizerShoptetShoptetAuthorizerNewRequest.md)|  | 

### Return type

[**GoogleAnalytics4StaticUserAuth**](GoogleAnalytics4StaticUserAuth.md)

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

