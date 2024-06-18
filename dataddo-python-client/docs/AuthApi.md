# openapi_client.AuthApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_controller_auth**](AuthApi.md#auth_controller_auth) | **POST** /auth | 
[**auth_controller_auth_mfa**](AuthApi.md#auth_controller_auth_mfa) | **POST** /auth-mfa | 
[**auth_controller_refresh**](AuthApi.md#auth_controller_refresh) | **GET** /refresh | 
[**auth_controller_revoke**](AuthApi.md#auth_controller_revoke) | **GET** /revoke | 


# **auth_controller_auth**
> SecurityDto auth_controller_auth(auth_request)



auth

### Example


```python
import openapi_client
from openapi_client.models.auth_request import AuthRequest
from openapi_client.models.security_dto import SecurityDto
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
    api_instance = openapi_client.AuthApi(api_client)
    auth_request = openapi_client.AuthRequest() # AuthRequest | 

    try:
        api_response = api_instance.auth_controller_auth(auth_request)
        print("The response of AuthApi->auth_controller_auth:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_controller_auth: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_request** | [**AuthRequest**](AuthRequest.md)|  | 

### Return type

[**SecurityDto**](SecurityDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_controller_auth_mfa**
> SecurityDto auth_controller_auth_mfa(auth_mfa_request)



### Example


```python
import openapi_client
from openapi_client.models.auth_mfa_request import AuthMFARequest
from openapi_client.models.security_dto import SecurityDto
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
    api_instance = openapi_client.AuthApi(api_client)
    auth_mfa_request = openapi_client.AuthMFARequest() # AuthMFARequest | 

    try:
        api_response = api_instance.auth_controller_auth_mfa(auth_mfa_request)
        print("The response of AuthApi->auth_controller_auth_mfa:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_controller_auth_mfa: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_mfa_request** | [**AuthMFARequest**](AuthMFARequest.md)|  | 

### Return type

[**SecurityDto**](SecurityDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_controller_refresh**
> SecurityDto auth_controller_refresh(x_realm_id, x_refresh_token, x_provider, authorization=authorization)



### Example


```python
import openapi_client
from openapi_client.models.security_dto import SecurityDto
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
    api_instance = openapi_client.AuthApi(api_client)
    x_realm_id = 'x_realm_id_example' # str | Realm ID
    x_refresh_token = 'x_refresh_token_example' # str | Refresh token
    x_provider = 'x_provider_example' # str | Provider
    authorization = 'authorization_example' # str | Access token (optional) (optional)

    try:
        api_response = api_instance.auth_controller_refresh(x_realm_id, x_refresh_token, x_provider, authorization=authorization)
        print("The response of AuthApi->auth_controller_refresh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_controller_refresh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_realm_id** | **str**| Realm ID | 
 **x_refresh_token** | **str**| Refresh token | 
 **x_provider** | **str**| Provider | 
 **authorization** | **str**| Access token (optional) | [optional] 

### Return type

[**SecurityDto**](SecurityDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_controller_revoke**
> auth_controller_revoke()



### Example


```python
import openapi_client
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
    api_instance = openapi_client.AuthApi(api_client)

    try:
        api_instance.auth_controller_revoke()
    except Exception as e:
        print("Exception when calling AuthApi->auth_controller_revoke: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

