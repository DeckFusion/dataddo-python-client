# openapi_client.DestinationsAwsAuroraApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_destination_aws_aurora_aws_aurora_destination_action_authorization**](DestinationsAwsAuroraApi.md#app_destination_aws_aurora_aws_aurora_destination_action_authorization) | **GET** /destinations/aws_aurora/actions/authorization | List of authorization objects
[**app_destination_aws_aurora_aws_aurora_destination_action_tls**](DestinationsAwsAuroraApi.md#app_destination_aws_aurora_aws_aurora_destination_action_tls) | **GET** /destinations/aws_aurora/actions/tls | List of TLS options
[**app_destination_aws_aurora_aws_aurora_destination_action_write_modes**](DestinationsAwsAuroraApi.md#app_destination_aws_aurora_aws_aurora_destination_action_write_modes) | **POST** /destinations/aws_aurora/actions/writeModes | List of write modes
[**app_destination_aws_aurora_aws_aurora_destination_create**](DestinationsAwsAuroraApi.md#app_destination_aws_aurora_aws_aurora_destination_create) | **POST** /destinations/aws_aurora | Create destination


# **app_destination_aws_aurora_aws_aurora_destination_action_authorization**
> List[ActionAuthorizationResponseInner] app_destination_aws_aurora_aws_aurora_destination_action_authorization()

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
    api_instance = openapi_client.DestinationsAwsAuroraApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_destination_aws_aurora_aws_aurora_destination_action_authorization()
        print("The response of DestinationsAwsAuroraApi->app_destination_aws_aurora_aws_aurora_destination_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsAwsAuroraApi->app_destination_aws_aurora_aws_aurora_destination_action_authorization: %s\n" % e)
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

# **app_destination_aws_aurora_aws_aurora_destination_action_tls**
> List[LabelValueResponseInner] app_destination_aws_aurora_aws_aurora_destination_action_tls()

List of TLS options

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
    api_instance = openapi_client.DestinationsAwsAuroraApi(api_client)

    try:
        # List of TLS options
        api_response = api_instance.app_destination_aws_aurora_aws_aurora_destination_action_tls()
        print("The response of DestinationsAwsAuroraApi->app_destination_aws_aurora_aws_aurora_destination_action_tls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsAwsAuroraApi->app_destination_aws_aurora_aws_aurora_destination_action_tls: %s\n" % e)
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
**200** | List of TLS options |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_destination_aws_aurora_aws_aurora_destination_action_write_modes**
> List[LabelValueResponseInner] app_destination_aws_aurora_aws_aurora_destination_action_write_modes(app_destination_alloy_db_alloy_db_destination_action_write_modes_request=app_destination_alloy_db_alloy_db_destination_action_write_modes_request)

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
    api_instance = openapi_client.DestinationsAwsAuroraApi(api_client)
    app_destination_alloy_db_alloy_db_destination_action_write_modes_request = openapi_client.AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest() # AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest |  (optional)

    try:
        # List of write modes
        api_response = api_instance.app_destination_aws_aurora_aws_aurora_destination_action_write_modes(app_destination_alloy_db_alloy_db_destination_action_write_modes_request=app_destination_alloy_db_alloy_db_destination_action_write_modes_request)
        print("The response of DestinationsAwsAuroraApi->app_destination_aws_aurora_aws_aurora_destination_action_write_modes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsAwsAuroraApi->app_destination_aws_aurora_aws_aurora_destination_action_write_modes: %s\n" % e)
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

# **app_destination_aws_aurora_aws_aurora_destination_create**
> AwsAuroraDestination app_destination_aws_aurora_aws_aurora_destination_create(my_sql_storage_request)

Create destination

### Example


```python
import openapi_client
from openapi_client.models.aws_aurora_destination import AwsAuroraDestination
from openapi_client.models.my_sql_storage_request import MySQLStorageRequest
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
    api_instance = openapi_client.DestinationsAwsAuroraApi(api_client)
    my_sql_storage_request = openapi_client.MySQLStorageRequest() # MySQLStorageRequest | 

    try:
        # Create destination
        api_response = api_instance.app_destination_aws_aurora_aws_aurora_destination_create(my_sql_storage_request)
        print("The response of DestinationsAwsAuroraApi->app_destination_aws_aurora_aws_aurora_destination_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsAwsAuroraApi->app_destination_aws_aurora_aws_aurora_destination_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **my_sql_storage_request** | [**MySQLStorageRequest**](MySQLStorageRequest.md)|  | 

### Return type

[**AwsAuroraDestination**](AwsAuroraDestination.md)

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

