# openapi_client.DestinationsGoogleCloudStorageApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_destination_google_cloud_storage_google_cloud_storage_destination_action_authorization**](DestinationsGoogleCloudStorageApi.md#app_destination_google_cloud_storage_google_cloud_storage_destination_action_authorization) | **GET** /destinations/google_cloud_storage/actions/authorization | List of authorization objects
[**app_destination_google_cloud_storage_google_cloud_storage_destination_action_filename_patterns**](DestinationsGoogleCloudStorageApi.md#app_destination_google_cloud_storage_google_cloud_storage_destination_action_filename_patterns) | **GET** /destinations/google_cloud_storage/actions/filename_formats | List of filename patterns
[**app_destination_google_cloud_storage_google_cloud_storage_destination_action_write_modes**](DestinationsGoogleCloudStorageApi.md#app_destination_google_cloud_storage_google_cloud_storage_destination_action_write_modes) | **POST** /destinations/google_cloud_storage/actions/writeModes | List of write modes
[**app_destination_google_cloud_storage_google_cloud_storage_destination_create**](DestinationsGoogleCloudStorageApi.md#app_destination_google_cloud_storage_google_cloud_storage_destination_create) | **POST** /destinations/google_cloud_storage | Create destination


# **app_destination_google_cloud_storage_google_cloud_storage_destination_action_authorization**
> List[ActionAuthorizationResponseInner] app_destination_google_cloud_storage_google_cloud_storage_destination_action_authorization()

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
    api_instance = openapi_client.DestinationsGoogleCloudStorageApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_destination_google_cloud_storage_google_cloud_storage_destination_action_authorization()
        print("The response of DestinationsGoogleCloudStorageApi->app_destination_google_cloud_storage_google_cloud_storage_destination_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsGoogleCloudStorageApi->app_destination_google_cloud_storage_google_cloud_storage_destination_action_authorization: %s\n" % e)
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

# **app_destination_google_cloud_storage_google_cloud_storage_destination_action_filename_patterns**
> List[LabelValueResponseInner] app_destination_google_cloud_storage_google_cloud_storage_destination_action_filename_patterns()

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
    api_instance = openapi_client.DestinationsGoogleCloudStorageApi(api_client)

    try:
        # List of filename patterns
        api_response = api_instance.app_destination_google_cloud_storage_google_cloud_storage_destination_action_filename_patterns()
        print("The response of DestinationsGoogleCloudStorageApi->app_destination_google_cloud_storage_google_cloud_storage_destination_action_filename_patterns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsGoogleCloudStorageApi->app_destination_google_cloud_storage_google_cloud_storage_destination_action_filename_patterns: %s\n" % e)
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

# **app_destination_google_cloud_storage_google_cloud_storage_destination_action_write_modes**
> List[LabelValueResponseInner] app_destination_google_cloud_storage_google_cloud_storage_destination_action_write_modes(app_destination_alloy_db_alloy_db_destination_action_write_modes_request=app_destination_alloy_db_alloy_db_destination_action_write_modes_request)

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
    api_instance = openapi_client.DestinationsGoogleCloudStorageApi(api_client)
    app_destination_alloy_db_alloy_db_destination_action_write_modes_request = openapi_client.AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest() # AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest |  (optional)

    try:
        # List of write modes
        api_response = api_instance.app_destination_google_cloud_storage_google_cloud_storage_destination_action_write_modes(app_destination_alloy_db_alloy_db_destination_action_write_modes_request=app_destination_alloy_db_alloy_db_destination_action_write_modes_request)
        print("The response of DestinationsGoogleCloudStorageApi->app_destination_google_cloud_storage_google_cloud_storage_destination_action_write_modes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsGoogleCloudStorageApi->app_destination_google_cloud_storage_google_cloud_storage_destination_action_write_modes: %s\n" % e)
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

# **app_destination_google_cloud_storage_google_cloud_storage_destination_create**
> GoogleCloudStorageDestination app_destination_google_cloud_storage_google_cloud_storage_destination_create(google_cloud_storage_request)

Create destination

### Example


```python
import openapi_client
from openapi_client.models.google_cloud_storage_destination import GoogleCloudStorageDestination
from openapi_client.models.google_cloud_storage_request import GoogleCloudStorageRequest
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
    api_instance = openapi_client.DestinationsGoogleCloudStorageApi(api_client)
    google_cloud_storage_request = openapi_client.GoogleCloudStorageRequest() # GoogleCloudStorageRequest | 

    try:
        # Create destination
        api_response = api_instance.app_destination_google_cloud_storage_google_cloud_storage_destination_create(google_cloud_storage_request)
        print("The response of DestinationsGoogleCloudStorageApi->app_destination_google_cloud_storage_google_cloud_storage_destination_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsGoogleCloudStorageApi->app_destination_google_cloud_storage_google_cloud_storage_destination_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_cloud_storage_request** | [**GoogleCloudStorageRequest**](GoogleCloudStorageRequest.md)|  | 

### Return type

[**GoogleCloudStorageDestination**](GoogleCloudStorageDestination.md)

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

