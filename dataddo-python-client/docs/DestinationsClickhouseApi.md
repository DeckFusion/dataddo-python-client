# openapi_client.DestinationsClickhouseApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_destination_clickhouse_clickhouse_destination_action_authorization**](DestinationsClickhouseApi.md#app_destination_clickhouse_clickhouse_destination_action_authorization) | **GET** /destinations/clickhouse/actions/authorization | List of authorization objects
[**app_destination_clickhouse_clickhouse_destination_action_ssl**](DestinationsClickhouseApi.md#app_destination_clickhouse_clickhouse_destination_action_ssl) | **GET** /destinations/clickhouse/actions/ssl | List of SSL options
[**app_destination_clickhouse_clickhouse_destination_action_table_engine**](DestinationsClickhouseApi.md#app_destination_clickhouse_clickhouse_destination_action_table_engine) | **GET** /destinations/clickhouse/actions/tableEngine | List of table engines
[**app_destination_clickhouse_clickhouse_destination_action_write_modes**](DestinationsClickhouseApi.md#app_destination_clickhouse_clickhouse_destination_action_write_modes) | **POST** /destinations/clickhouse/actions/writeModes | List of write modes
[**app_destination_clickhouse_clickhouse_destination_create**](DestinationsClickhouseApi.md#app_destination_clickhouse_clickhouse_destination_create) | **POST** /destinations/clickhouse | Create destination


# **app_destination_clickhouse_clickhouse_destination_action_authorization**
> List[ActionAuthorizationResponseInner] app_destination_clickhouse_clickhouse_destination_action_authorization()

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
    api_instance = openapi_client.DestinationsClickhouseApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_destination_clickhouse_clickhouse_destination_action_authorization()
        print("The response of DestinationsClickhouseApi->app_destination_clickhouse_clickhouse_destination_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsClickhouseApi->app_destination_clickhouse_clickhouse_destination_action_authorization: %s\n" % e)
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

# **app_destination_clickhouse_clickhouse_destination_action_ssl**
> List[LabelValueResponseInner] app_destination_clickhouse_clickhouse_destination_action_ssl()

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
    api_instance = openapi_client.DestinationsClickhouseApi(api_client)

    try:
        # List of SSL options
        api_response = api_instance.app_destination_clickhouse_clickhouse_destination_action_ssl()
        print("The response of DestinationsClickhouseApi->app_destination_clickhouse_clickhouse_destination_action_ssl:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsClickhouseApi->app_destination_clickhouse_clickhouse_destination_action_ssl: %s\n" % e)
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

# **app_destination_clickhouse_clickhouse_destination_action_table_engine**
> List[LabelValueResponseInner] app_destination_clickhouse_clickhouse_destination_action_table_engine()

List of table engines

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
    api_instance = openapi_client.DestinationsClickhouseApi(api_client)

    try:
        # List of table engines
        api_response = api_instance.app_destination_clickhouse_clickhouse_destination_action_table_engine()
        print("The response of DestinationsClickhouseApi->app_destination_clickhouse_clickhouse_destination_action_table_engine:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsClickhouseApi->app_destination_clickhouse_clickhouse_destination_action_table_engine: %s\n" % e)
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
**200** | List of table engines |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_destination_clickhouse_clickhouse_destination_action_write_modes**
> List[LabelValueResponseInner] app_destination_clickhouse_clickhouse_destination_action_write_modes(app_destination_alloy_db_alloy_db_destination_action_write_modes_request=app_destination_alloy_db_alloy_db_destination_action_write_modes_request)

List of write modes

### Example


```python
import openapi_client
from openapi_client.models.app_destination_alloy_db_alloy_db_destination_action_write_modes_request import AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest
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
    api_instance = openapi_client.DestinationsClickhouseApi(api_client)
    app_destination_alloy_db_alloy_db_destination_action_write_modes_request = openapi_client.AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest() # AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest |  (optional)

    try:
        # List of write modes
        api_response = api_instance.app_destination_clickhouse_clickhouse_destination_action_write_modes(app_destination_alloy_db_alloy_db_destination_action_write_modes_request=app_destination_alloy_db_alloy_db_destination_action_write_modes_request)
        print("The response of DestinationsClickhouseApi->app_destination_clickhouse_clickhouse_destination_action_write_modes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsClickhouseApi->app_destination_clickhouse_clickhouse_destination_action_write_modes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_destination_alloy_db_alloy_db_destination_action_write_modes_request** | [**AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest**](AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest.md)|  | [optional] 

### Return type

[**List[LabelValueResponseInner]**](LabelValueResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of write modes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_destination_clickhouse_clickhouse_destination_create**
> ClickhouseDestination app_destination_clickhouse_clickhouse_destination_create(clickhouse_storage_request)

Create destination

### Example


```python
import openapi_client
from openapi_client.models.clickhouse_destination import ClickhouseDestination
from openapi_client.models.clickhouse_storage_request import ClickhouseStorageRequest
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
    api_instance = openapi_client.DestinationsClickhouseApi(api_client)
    clickhouse_storage_request = openapi_client.ClickhouseStorageRequest() # ClickhouseStorageRequest | 

    try:
        # Create destination
        api_response = api_instance.app_destination_clickhouse_clickhouse_destination_create(clickhouse_storage_request)
        print("The response of DestinationsClickhouseApi->app_destination_clickhouse_clickhouse_destination_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsClickhouseApi->app_destination_clickhouse_clickhouse_destination_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clickhouse_storage_request** | [**ClickhouseStorageRequest**](ClickhouseStorageRequest.md)|  | 

### Return type

[**ClickhouseDestination**](ClickhouseDestination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New destination |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

