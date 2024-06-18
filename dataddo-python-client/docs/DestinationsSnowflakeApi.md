# openapi_client.DestinationsSnowflakeApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_destination_snowflake_snowflake_destination_action_authorization**](DestinationsSnowflakeApi.md#app_destination_snowflake_snowflake_destination_action_authorization) | **GET** /destinations/snowflake/actions/authorization | List of authorization objects
[**app_destination_snowflake_snowflake_destination_action_schema**](DestinationsSnowflakeApi.md#app_destination_snowflake_snowflake_destination_action_schema) | **POST** /destinations/snowflake/actions/schema | Default schema from destination defined by destination
[**app_destination_snowflake_snowflake_destination_action_write_modes**](DestinationsSnowflakeApi.md#app_destination_snowflake_snowflake_destination_action_write_modes) | **POST** /destinations/snowflake/actions/writeModes | List of write modes
[**app_destination_snowflake_snowflake_destination_create**](DestinationsSnowflakeApi.md#app_destination_snowflake_snowflake_destination_create) | **POST** /destinations/snowflake | Create destination


# **app_destination_snowflake_snowflake_destination_action_authorization**
> List[ActionAuthorizationResponseInner] app_destination_snowflake_snowflake_destination_action_authorization()

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
    api_instance = openapi_client.DestinationsSnowflakeApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_destination_snowflake_snowflake_destination_action_authorization()
        print("The response of DestinationsSnowflakeApi->app_destination_snowflake_snowflake_destination_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsSnowflakeApi->app_destination_snowflake_snowflake_destination_action_authorization: %s\n" % e)
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

# **app_destination_snowflake_snowflake_destination_action_schema**
> List[LabelValueResponseInner] app_destination_snowflake_snowflake_destination_action_schema(app_destination_snowflake_snowflake_destination_action_schema_request=app_destination_snowflake_snowflake_destination_action_schema_request)

Default schema from destination defined by destination

### Example


```python
import openapi_client
from openapi_client.models.app_destination_snowflake_snowflake_destination_action_schema_request import AppDestinationSnowflakeSnowflakeDestinationActionSchemaRequest
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
    api_instance = openapi_client.DestinationsSnowflakeApi(api_client)
    app_destination_snowflake_snowflake_destination_action_schema_request = openapi_client.AppDestinationSnowflakeSnowflakeDestinationActionSchemaRequest() # AppDestinationSnowflakeSnowflakeDestinationActionSchemaRequest |  (optional)

    try:
        # Default schema from destination defined by destination
        api_response = api_instance.app_destination_snowflake_snowflake_destination_action_schema(app_destination_snowflake_snowflake_destination_action_schema_request=app_destination_snowflake_snowflake_destination_action_schema_request)
        print("The response of DestinationsSnowflakeApi->app_destination_snowflake_snowflake_destination_action_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsSnowflakeApi->app_destination_snowflake_snowflake_destination_action_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_destination_snowflake_snowflake_destination_action_schema_request** | [**AppDestinationSnowflakeSnowflakeDestinationActionSchemaRequest**](AppDestinationSnowflakeSnowflakeDestinationActionSchemaRequest.md)|  | [optional] 

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
**200** | Get the default schema for the destination |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_destination_snowflake_snowflake_destination_action_write_modes**
> List[LabelValueResponseInner] app_destination_snowflake_snowflake_destination_action_write_modes(app_destination_alloy_db_alloy_db_destination_action_write_modes_request=app_destination_alloy_db_alloy_db_destination_action_write_modes_request)

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
    api_instance = openapi_client.DestinationsSnowflakeApi(api_client)
    app_destination_alloy_db_alloy_db_destination_action_write_modes_request = openapi_client.AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest() # AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest |  (optional)

    try:
        # List of write modes
        api_response = api_instance.app_destination_snowflake_snowflake_destination_action_write_modes(app_destination_alloy_db_alloy_db_destination_action_write_modes_request=app_destination_alloy_db_alloy_db_destination_action_write_modes_request)
        print("The response of DestinationsSnowflakeApi->app_destination_snowflake_snowflake_destination_action_write_modes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsSnowflakeApi->app_destination_snowflake_snowflake_destination_action_write_modes: %s\n" % e)
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

# **app_destination_snowflake_snowflake_destination_create**
> SnowflakeDestination app_destination_snowflake_snowflake_destination_create(snowflake_storage_request)

Create destination

### Example


```python
import openapi_client
from openapi_client.models.snowflake_destination import SnowflakeDestination
from openapi_client.models.snowflake_storage_request import SnowflakeStorageRequest
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
    api_instance = openapi_client.DestinationsSnowflakeApi(api_client)
    snowflake_storage_request = openapi_client.SnowflakeStorageRequest() # SnowflakeStorageRequest | 

    try:
        # Create destination
        api_response = api_instance.app_destination_snowflake_snowflake_destination_create(snowflake_storage_request)
        print("The response of DestinationsSnowflakeApi->app_destination_snowflake_snowflake_destination_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsSnowflakeApi->app_destination_snowflake_snowflake_destination_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snowflake_storage_request** | [**SnowflakeStorageRequest**](SnowflakeStorageRequest.md)|  | 

### Return type

[**SnowflakeDestination**](SnowflakeDestination.md)

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

