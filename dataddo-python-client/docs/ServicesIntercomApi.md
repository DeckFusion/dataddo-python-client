# openapi_client.ServicesIntercomApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_authorizer_intercom_intercom_authorizer_action_region**](ServicesIntercomApi.md#app_authorizer_intercom_intercom_authorizer_action_region) | **GET** /services/intercom/actions/region | List of region options
[**app_authorizer_intercom_intercom_authorizer_get_authorization_url**](ServicesIntercomApi.md#app_authorizer_intercom_intercom_authorizer_get_authorization_url) | **POST** /services/intercom/oauth-request-url | Builds redirect URL


# **app_authorizer_intercom_intercom_authorizer_action_region**
> List[LabelValueResponseInner] app_authorizer_intercom_intercom_authorizer_action_region()

List of region options

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
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
    api_instance = openapi_client.ServicesIntercomApi(api_client)

    try:
        # List of region options
        api_response = api_instance.app_authorizer_intercom_intercom_authorizer_action_region()
        print("The response of ServicesIntercomApi->app_authorizer_intercom_intercom_authorizer_action_region:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesIntercomApi->app_authorizer_intercom_intercom_authorizer_action_region: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[LabelValueResponseInner]**](LabelValueResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of region options |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_authorizer_intercom_intercom_authorizer_get_authorization_url**
> OAuthRequestUrlResponse app_authorizer_intercom_intercom_authorizer_get_authorization_url(app_authorizer_intercom_intercom_authorizer_get_authorization_url_request)

Builds redirect URL

### Example


```python
import openapi_client
from openapi_client.models.app_authorizer_intercom_intercom_authorizer_get_authorization_url_request import AppAuthorizerIntercomIntercomAuthorizerGetAuthorizationUrlRequest
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
    api_instance = openapi_client.ServicesIntercomApi(api_client)
    app_authorizer_intercom_intercom_authorizer_get_authorization_url_request = openapi_client.AppAuthorizerIntercomIntercomAuthorizerGetAuthorizationUrlRequest() # AppAuthorizerIntercomIntercomAuthorizerGetAuthorizationUrlRequest | 

    try:
        # Builds redirect URL
        api_response = api_instance.app_authorizer_intercom_intercom_authorizer_get_authorization_url(app_authorizer_intercom_intercom_authorizer_get_authorization_url_request)
        print("The response of ServicesIntercomApi->app_authorizer_intercom_intercom_authorizer_get_authorization_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesIntercomApi->app_authorizer_intercom_intercom_authorizer_get_authorization_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_authorizer_intercom_intercom_authorizer_get_authorization_url_request** | [**AppAuthorizerIntercomIntercomAuthorizerGetAuthorizationUrlRequest**](AppAuthorizerIntercomIntercomAuthorizerGetAuthorizationUrlRequest.md)|  | 

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

