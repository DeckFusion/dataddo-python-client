# openapi_client.ConnectorsCoreWebVitalsApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_core_web_vitals_core_web_vitals_connector_action_authorization**](ConnectorsCoreWebVitalsApi.md#app_connector_core_web_vitals_core_web_vitals_connector_action_authorization) | **GET** /connectors/core_web_vitals/actions/authorization | List of authorization objects
[**app_connector_core_web_vitals_core_web_vitals_connector_create_source**](ConnectorsCoreWebVitalsApi.md#app_connector_core_web_vitals_core_web_vitals_connector_create_source) | **POST** /connectors/coreWebVitals/create-source | Create CoreWebVital source
[**app_connector_core_web_vitals_core_web_vitals_connector_preview**](ConnectorsCoreWebVitalsApi.md#app_connector_core_web_vitals_core_web_vitals_connector_preview) | **POST** /connectors/core_web_vitals/preview | Data preview


# **app_connector_core_web_vitals_core_web_vitals_connector_action_authorization**
> List[ActionAuthorizationResponseInner] app_connector_core_web_vitals_core_web_vitals_connector_action_authorization()

List of authorization objects

### Example


```python
import openapi_client
from openapi_client.models.action_authorization_response_inner import ActionAuthorizationResponseInner
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
    api_instance = openapi_client.ConnectorsCoreWebVitalsApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_connector_core_web_vitals_core_web_vitals_connector_action_authorization()
        print("The response of ConnectorsCoreWebVitalsApi->app_connector_core_web_vitals_core_web_vitals_connector_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsCoreWebVitalsApi->app_connector_core_web_vitals_core_web_vitals_connector_action_authorization: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ActionAuthorizationResponseInner]**](ActionAuthorizationResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of authorization objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_core_web_vitals_core_web_vitals_connector_create_source**
> Source app_connector_core_web_vitals_core_web_vitals_connector_create_source(core_web_vitals_dto=core_web_vitals_dto)

Create CoreWebVital source

### Example


```python
import openapi_client
from openapi_client.models.core_web_vitals_dto import CoreWebVitalsDto
from openapi_client.models.source import Source
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
    api_instance = openapi_client.ConnectorsCoreWebVitalsApi(api_client)
    core_web_vitals_dto = openapi_client.CoreWebVitalsDto() # CoreWebVitalsDto |  (optional)

    try:
        # Create CoreWebVital source
        api_response = api_instance.app_connector_core_web_vitals_core_web_vitals_connector_create_source(core_web_vitals_dto=core_web_vitals_dto)
        print("The response of ConnectorsCoreWebVitalsApi->app_connector_core_web_vitals_core_web_vitals_connector_create_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsCoreWebVitalsApi->app_connector_core_web_vitals_core_web_vitals_connector_create_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **core_web_vitals_dto** | [**CoreWebVitalsDto**](CoreWebVitalsDto.md)|  | [optional] 

### Return type

[**Source**](Source.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_core_web_vitals_core_web_vitals_connector_preview**
> SuccessResponse app_connector_core_web_vitals_core_web_vitals_connector_preview(core_web_vitals_dto=core_web_vitals_dto)

Data preview

### Example


```python
import openapi_client
from openapi_client.models.core_web_vitals_dto import CoreWebVitalsDto
from openapi_client.models.success_response import SuccessResponse
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
    api_instance = openapi_client.ConnectorsCoreWebVitalsApi(api_client)
    core_web_vitals_dto = openapi_client.CoreWebVitalsDto() # CoreWebVitalsDto |  (optional)

    try:
        # Data preview
        api_response = api_instance.app_connector_core_web_vitals_core_web_vitals_connector_preview(core_web_vitals_dto=core_web_vitals_dto)
        print("The response of ConnectorsCoreWebVitalsApi->app_connector_core_web_vitals_core_web_vitals_connector_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsCoreWebVitalsApi->app_connector_core_web_vitals_core_web_vitals_connector_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **core_web_vitals_dto** | [**CoreWebVitalsDto**](CoreWebVitalsDto.md)|  | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data preview |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

