# openapi_client.ServicesMicrosoftDynamics365Api

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_get_authorization_url**](ServicesMicrosoftDynamics365Api.md#app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_get_authorization_url) | **POST** /services/microsoft_dynamics365/oauth-request-url | Get url for service authentication
[**app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_o_auth_process_callback**](ServicesMicrosoftDynamics365Api.md#app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_o_auth_process_callback) | **POST** /services/microsoft_dynamics365/oauth-process-callback | Create service


# **app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_get_authorization_url**
> OAuthRequestUrlResponse app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_get_authorization_url(app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_get_authorization_url_request)

Get url for service authentication

### Example


```python
import openapi_client
from openapi_client.models.app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_get_authorization_url_request import AppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerGetAuthorizationUrlRequest
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
    api_instance = openapi_client.ServicesMicrosoftDynamics365Api(api_client)
    app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_get_authorization_url_request = openapi_client.AppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerGetAuthorizationUrlRequest() # AppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerGetAuthorizationUrlRequest | 

    try:
        # Get url for service authentication
        api_response = api_instance.app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_get_authorization_url(app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_get_authorization_url_request)
        print("The response of ServicesMicrosoftDynamics365Api->app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_get_authorization_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesMicrosoftDynamics365Api->app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_get_authorization_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_get_authorization_url_request** | [**AppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerGetAuthorizationUrlRequest**](AppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerGetAuthorizationUrlRequest.md)|  | 

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

# **app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_o_auth_process_callback**
> object app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_o_auth_process_callback(app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_o_auth_process_callback_request)

Create service

### Example


```python
import openapi_client
from openapi_client.models.app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_o_auth_process_callback_request import AppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerOAuthProcessCallbackRequest
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
    api_instance = openapi_client.ServicesMicrosoftDynamics365Api(api_client)
    app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_o_auth_process_callback_request = openapi_client.AppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerOAuthProcessCallbackRequest() # AppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerOAuthProcessCallbackRequest | 

    try:
        # Create service
        api_response = api_instance.app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_o_auth_process_callback(app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_o_auth_process_callback_request)
        print("The response of ServicesMicrosoftDynamics365Api->app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_o_auth_process_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesMicrosoftDynamics365Api->app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_o_auth_process_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_o_auth_process_callback_request** | [**AppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerOAuthProcessCallbackRequest**](AppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerOAuthProcessCallbackRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Processes the callback and fetches the refresh token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

