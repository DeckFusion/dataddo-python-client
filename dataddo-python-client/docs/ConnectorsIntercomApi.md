# openapi_client.ConnectorsIntercomApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_intercom_intercom_connector_action_authorization**](ConnectorsIntercomApi.md#app_connector_intercom_intercom_connector_action_authorization) | **GET** /connectors/intercom/actions/authorization | List of authorization objects
[**app_connector_intercom_intercom_connector_action_date_range**](ConnectorsIntercomApi.md#app_connector_intercom_intercom_connector_action_date_range) | **GET** /connectors/intercom/actions/dateRange | Method for listing date range
[**app_connector_intercom_intercom_connector_create_source**](ConnectorsIntercomApi.md#app_connector_intercom_intercom_connector_create_source) | **POST** /connectors/intercom/create-source | Create Intercom source
[**app_connector_intercom_intercom_connector_preview**](ConnectorsIntercomApi.md#app_connector_intercom_intercom_connector_preview) | **POST** /connectors/intercom/preview | Data preview


# **app_connector_intercom_intercom_connector_action_authorization**
> List[ActionAuthorizationResponseInner] app_connector_intercom_intercom_connector_action_authorization()

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
    api_instance = openapi_client.ConnectorsIntercomApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_connector_intercom_intercom_connector_action_authorization()
        print("The response of ConnectorsIntercomApi->app_connector_intercom_intercom_connector_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsIntercomApi->app_connector_intercom_intercom_connector_action_authorization: %s\n" % e)
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

# **app_connector_intercom_intercom_connector_action_date_range**
> List[LabelValueResponseInner] app_connector_intercom_intercom_connector_action_date_range()

Method for listing date range

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
    api_instance = openapi_client.ConnectorsIntercomApi(api_client)

    try:
        # Method for listing date range
        api_response = api_instance.app_connector_intercom_intercom_connector_action_date_range()
        print("The response of ConnectorsIntercomApi->app_connector_intercom_intercom_connector_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsIntercomApi->app_connector_intercom_intercom_connector_action_date_range: %s\n" % e)
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
**200** | List of Intercom date ranges |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_intercom_intercom_connector_create_source**
> Source app_connector_intercom_intercom_connector_create_source(intercom_dto=intercom_dto)

Create Intercom source

### Example


```python
import openapi_client
from openapi_client.models.intercom_dto import IntercomDto
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
    api_instance = openapi_client.ConnectorsIntercomApi(api_client)
    intercom_dto = openapi_client.IntercomDto() # IntercomDto |  (optional)

    try:
        # Create Intercom source
        api_response = api_instance.app_connector_intercom_intercom_connector_create_source(intercom_dto=intercom_dto)
        print("The response of ConnectorsIntercomApi->app_connector_intercom_intercom_connector_create_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsIntercomApi->app_connector_intercom_intercom_connector_create_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **intercom_dto** | [**IntercomDto**](IntercomDto.md)|  | [optional] 

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

# **app_connector_intercom_intercom_connector_preview**
> SuccessResponse app_connector_intercom_intercom_connector_preview(intercom_dto=intercom_dto)

Data preview

### Example


```python
import openapi_client
from openapi_client.models.intercom_dto import IntercomDto
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
    api_instance = openapi_client.ConnectorsIntercomApi(api_client)
    intercom_dto = openapi_client.IntercomDto() # IntercomDto |  (optional)

    try:
        # Data preview
        api_response = api_instance.app_connector_intercom_intercom_connector_preview(intercom_dto=intercom_dto)
        print("The response of ConnectorsIntercomApi->app_connector_intercom_intercom_connector_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsIntercomApi->app_connector_intercom_intercom_connector_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **intercom_dto** | [**IntercomDto**](IntercomDto.md)|  | [optional] 

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

