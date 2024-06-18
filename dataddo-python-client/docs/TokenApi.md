# openapi_client.TokenApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**token_controller_create**](TokenApi.md#token_controller_create) | **POST** /tokens | 
[**token_controller_delete**](TokenApi.md#token_controller_delete) | **DELETE** /tokens/{id} | 
[**token_controller_list**](TokenApi.md#token_controller_list) | **GET** /tokens | 


# **token_controller_create**
> Token token_controller_create(create_token_request)



### Example


```python
import openapi_client
from openapi_client.models.create_token_request import CreateTokenRequest
from openapi_client.models.token import Token
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
    api_instance = openapi_client.TokenApi(api_client)
    create_token_request = openapi_client.CreateTokenRequest() # CreateTokenRequest | 

    try:
        api_response = api_instance.token_controller_create(create_token_request)
        print("The response of TokenApi->token_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenApi->token_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_token_request** | [**CreateTokenRequest**](CreateTokenRequest.md)|  | 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Creates new token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_controller_delete**
> token_controller_delete(id)



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
    api_instance = openapi_client.TokenApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.token_controller_delete(id)
    except Exception as e:
        print("Exception when calling TokenApi->token_controller_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**204** | Deletes the token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_controller_list**
> List[Token] token_controller_list()



### Example


```python
import openapi_client
from openapi_client.models.token import Token
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
    api_instance = openapi_client.TokenApi(api_client)

    try:
        api_response = api_instance.token_controller_list()
        print("The response of TokenApi->token_controller_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenApi->token_controller_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Token]**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lists all customer tokens |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

