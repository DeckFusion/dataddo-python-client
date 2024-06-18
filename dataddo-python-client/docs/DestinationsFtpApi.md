# openapi_client.DestinationsFtpApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_destination_ftp_ftp_destination_action_authorization**](DestinationsFtpApi.md#app_destination_ftp_ftp_destination_action_authorization) | **GET** /destinations/ftp/actions/authorization | List of authorization objects
[**app_destination_ftp_ftp_destination_action_file_formats**](DestinationsFtpApi.md#app_destination_ftp_ftp_destination_action_file_formats) | **GET** /destinations/ftp/actions/fileFormats | List of file formats
[**app_destination_ftp_ftp_destination_action_filename_patterns**](DestinationsFtpApi.md#app_destination_ftp_ftp_destination_action_filename_patterns) | **GET** /destinations/ftp/actions/filename_formats | List of filename patterns
[**app_destination_ftp_ftp_destination_action_write_modes**](DestinationsFtpApi.md#app_destination_ftp_ftp_destination_action_write_modes) | **POST** /destinations/ftp/actions/writeModes | List of write modes
[**app_destination_ftp_ftp_destination_create**](DestinationsFtpApi.md#app_destination_ftp_ftp_destination_create) | **POST** /destinations/ftp | Create destination


# **app_destination_ftp_ftp_destination_action_authorization**
> List[ActionAuthorizationResponseInner] app_destination_ftp_ftp_destination_action_authorization()

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
    api_instance = openapi_client.DestinationsFtpApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_destination_ftp_ftp_destination_action_authorization()
        print("The response of DestinationsFtpApi->app_destination_ftp_ftp_destination_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsFtpApi->app_destination_ftp_ftp_destination_action_authorization: %s\n" % e)
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

# **app_destination_ftp_ftp_destination_action_file_formats**
> List[LabelValueResponseInner] app_destination_ftp_ftp_destination_action_file_formats()

List of file formats

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
    api_instance = openapi_client.DestinationsFtpApi(api_client)

    try:
        # List of file formats
        api_response = api_instance.app_destination_ftp_ftp_destination_action_file_formats()
        print("The response of DestinationsFtpApi->app_destination_ftp_ftp_destination_action_file_formats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsFtpApi->app_destination_ftp_ftp_destination_action_file_formats: %s\n" % e)
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
**200** | List of file formats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_destination_ftp_ftp_destination_action_filename_patterns**
> List[LabelValueResponseInner] app_destination_ftp_ftp_destination_action_filename_patterns()

List of filename patterns

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
    api_instance = openapi_client.DestinationsFtpApi(api_client)

    try:
        # List of filename patterns
        api_response = api_instance.app_destination_ftp_ftp_destination_action_filename_patterns()
        print("The response of DestinationsFtpApi->app_destination_ftp_ftp_destination_action_filename_patterns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsFtpApi->app_destination_ftp_ftp_destination_action_filename_patterns: %s\n" % e)
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
**200** | List of filename patterns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_destination_ftp_ftp_destination_action_write_modes**
> List[LabelValueResponseInner] app_destination_ftp_ftp_destination_action_write_modes(app_destination_alloy_db_alloy_db_destination_action_write_modes_request=app_destination_alloy_db_alloy_db_destination_action_write_modes_request)

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
    api_instance = openapi_client.DestinationsFtpApi(api_client)
    app_destination_alloy_db_alloy_db_destination_action_write_modes_request = openapi_client.AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest() # AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest |  (optional)

    try:
        # List of write modes
        api_response = api_instance.app_destination_ftp_ftp_destination_action_write_modes(app_destination_alloy_db_alloy_db_destination_action_write_modes_request=app_destination_alloy_db_alloy_db_destination_action_write_modes_request)
        print("The response of DestinationsFtpApi->app_destination_ftp_ftp_destination_action_write_modes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsFtpApi->app_destination_ftp_ftp_destination_action_write_modes: %s\n" % e)
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

# **app_destination_ftp_ftp_destination_create**
> FtpDestination app_destination_ftp_ftp_destination_create(ftp_storage_request)

Create destination

### Example


```python
import openapi_client
from openapi_client.models.ftp_destination import FtpDestination
from openapi_client.models.ftp_storage_request import FtpStorageRequest
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
    api_instance = openapi_client.DestinationsFtpApi(api_client)
    ftp_storage_request = openapi_client.FtpStorageRequest() # FtpStorageRequest | 

    try:
        # Create destination
        api_response = api_instance.app_destination_ftp_ftp_destination_create(ftp_storage_request)
        print("The response of DestinationsFtpApi->app_destination_ftp_ftp_destination_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsFtpApi->app_destination_ftp_ftp_destination_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ftp_storage_request** | [**FtpStorageRequest**](FtpStorageRequest.md)|  | 

### Return type

[**FtpDestination**](FtpDestination.md)

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
