# openapi_client.ServicesAlloyDbApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_authorizer_alloy_db_alloy_db_authorizer_action_ssl**](ServicesAlloyDbApi.md#app_authorizer_alloy_db_alloy_db_authorizer_action_ssl) | **GET** /services/alloy_db/actions/tls | List of SSL options
[**app_authorizer_alloy_db_alloy_db_authorizer_create_service**](ServicesAlloyDbApi.md#app_authorizer_alloy_db_alloy_db_authorizer_create_service) | **POST** /services/alloy_db | Create service


# **app_authorizer_alloy_db_alloy_db_authorizer_action_ssl**
> List[LabelValueResponseInner] app_authorizer_alloy_db_alloy_db_authorizer_action_ssl()

List of SSL options

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
    api_instance = openapi_client.ServicesAlloyDbApi(api_client)

    try:
        # List of SSL options
        api_response = api_instance.app_authorizer_alloy_db_alloy_db_authorizer_action_ssl()
        print("The response of ServicesAlloyDbApi->app_authorizer_alloy_db_alloy_db_authorizer_action_ssl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesAlloyDbApi->app_authorizer_alloy_db_alloy_db_authorizer_action_ssl: %s\n" % e)
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
**200** | List of SSL options |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_authorizer_alloy_db_alloy_db_authorizer_create_service**
> AlloyDbUserAuth app_authorizer_alloy_db_alloy_db_authorizer_create_service(app_authorizer_alloy_db_alloy_db_authorizer_create_service_request)

Create service

### Example


```python
import openapi_client
from openapi_client.models.alloy_db_user_auth import AlloyDbUserAuth
from openapi_client.models.app_authorizer_alloy_db_alloy_db_authorizer_create_service_request import AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest
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
    api_instance = openapi_client.ServicesAlloyDbApi(api_client)
    app_authorizer_alloy_db_alloy_db_authorizer_create_service_request = openapi_client.AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest() # AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest | 

    try:
        # Create service
        api_response = api_instance.app_authorizer_alloy_db_alloy_db_authorizer_create_service(app_authorizer_alloy_db_alloy_db_authorizer_create_service_request)
        print("The response of ServicesAlloyDbApi->app_authorizer_alloy_db_alloy_db_authorizer_create_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesAlloyDbApi->app_authorizer_alloy_db_alloy_db_authorizer_create_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_authorizer_alloy_db_alloy_db_authorizer_create_service_request** | [**AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest**](AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest.md)|  | 

### Return type

[**AlloyDbUserAuth**](AlloyDbUserAuth.md)

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

