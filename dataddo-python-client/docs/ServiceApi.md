# openapi_client.ServiceApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_controller_create**](ServiceApi.md#service_controller_create) | **POST** /services | 
[**service_controller_debug**](ServiceApi.md#service_controller_debug) | **GET** /services/{id}/debug | 
[**service_controller_delete**](ServiceApi.md#service_controller_delete) | **DELETE** /services/{id} | 
[**service_controller_detail**](ServiceApi.md#service_controller_detail) | **GET** /services/{id} | 
[**service_controller_list**](ServiceApi.md#service_controller_list) | **GET** /services | 
[**service_controller_o_auth_process_callback**](ServiceApi.md#service_controller_o_auth_process_callback) | **POST** /services/{serviceName}/oauth-process-callback | 
[**service_controller_o_auth_request_url**](ServiceApi.md#service_controller_o_auth_request_url) | **POST** /services/{serviceName}/oauth-request-url | 
[**service_controller_update**](ServiceApi.md#service_controller_update) | **PUT** /services/{id} | 


# **service_controller_create**
> object service_controller_create(create_service_request)



### Example


```python
import openapi_client
from openapi_client.models.create_service_request import CreateServiceRequest
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
    api_instance = openapi_client.ServiceApi(api_client)
    create_service_request = openapi_client.CreateServiceRequest() # CreateServiceRequest | 

    try:
        api_response = api_instance.service_controller_create(create_service_request)
        print("The response of ServiceApi->service_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->service_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_service_request** | [**CreateServiceRequest**](CreateServiceRequest.md)|  | 

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
**200** | Creates new service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_controller_debug**
> AuthorizerDebugResponse service_controller_debug(id)



### Example


```python
import openapi_client
from openapi_client.models.authorizer_debug_response import AuthorizerDebugResponse
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
    api_instance = openapi_client.ServiceApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.service_controller_debug(id)
        print("The response of ServiceApi->service_controller_debug:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->service_controller_debug: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AuthorizerDebugResponse**](AuthorizerDebugResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Checks whether service is operable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_controller_delete**
> service_controller_delete(id)



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
    api_instance = openapi_client.ServiceApi(api_client)
    id = 56 # int | 

    try:
        api_instance.service_controller_delete(id)
    except Exception as e:
        print("Exception when calling ServiceApi->service_controller_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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
**204** | Delete single service. Fails if service is being used |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_controller_detail**
> object service_controller_detail(id)



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
    api_instance = openapi_client.ServiceApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.service_controller_detail(id)
        print("The response of ServiceApi->service_controller_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->service_controller_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get service detail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_controller_list**
> List[ServiceListResponse] service_controller_list()



### Example


```python
import openapi_client
from openapi_client.models.service_list_response import ServiceListResponse
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
    api_instance = openapi_client.ServiceApi(api_client)

    try:
        api_response = api_instance.service_controller_list()
        print("The response of ServiceApi->service_controller_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->service_controller_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ServiceListResponse]**](ServiceListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all services |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_controller_o_auth_process_callback**
> object service_controller_o_auth_process_callback(service_name, o_auth_process_callback_request)



### Example


```python
import openapi_client
from openapi_client.models.o_auth_process_callback_request import OAuthProcessCallbackRequest
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
    api_instance = openapi_client.ServiceApi(api_client)
    service_name = 'service_name_example' # str | 
    o_auth_process_callback_request = openapi_client.OAuthProcessCallbackRequest() # OAuthProcessCallbackRequest | 

    try:
        api_response = api_instance.service_controller_o_auth_process_callback(service_name, o_auth_process_callback_request)
        print("The response of ServiceApi->service_controller_o_auth_process_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->service_controller_o_auth_process_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**|  | 
 **o_auth_process_callback_request** | [**OAuthProcessCallbackRequest**](OAuthProcessCallbackRequest.md)|  | 

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

# **service_controller_o_auth_request_url**
> object service_controller_o_auth_request_url(service_name, o_auth_url_request)



### Example


```python
import openapi_client
from openapi_client.models.o_auth_url_request import OAuthURLRequest
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
    api_instance = openapi_client.ServiceApi(api_client)
    service_name = 'service_name_example' # str | 
    o_auth_url_request = openapi_client.OAuthURLRequest() # OAuthURLRequest | Parameters for OAuth URL

    try:
        api_response = api_instance.service_controller_o_auth_request_url(service_name, o_auth_url_request)
        print("The response of ServiceApi->service_controller_o_auth_request_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->service_controller_o_auth_request_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**|  | 
 **o_auth_url_request** | [**OAuthURLRequest**](OAuthURLRequest.md)| Parameters for OAuth URL | 

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
**200** | Returns the url |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_controller_update**
> object service_controller_update(id, body)



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
    api_instance = openapi_client.ServiceApi(api_client)
    id = 56 # int | 
    body = None # object | 

    try:
        api_response = api_instance.service_controller_update(id, body)
        print("The response of ServiceApi->service_controller_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->service_controller_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | **object**|  | 

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
**200** | Updates the source and it&#39;s related documents |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

