# openapi_client.DestinationsGoogleBigQueryApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_destination_google_big_query_google_big_query_destination_action_authorization**](DestinationsGoogleBigQueryApi.md#app_destination_google_big_query_google_big_query_destination_action_authorization) | **GET** /destinations/google_big_query/actions/authorization | List of authorization objects
[**app_destination_google_big_query_google_big_query_destination_action_dataset**](DestinationsGoogleBigQueryApi.md#app_destination_google_big_query_google_big_query_destination_action_dataset) | **POST** /destinations/google_big_query/actions/dataset | List of datasets
[**app_destination_google_big_query_google_big_query_destination_action_project**](DestinationsGoogleBigQueryApi.md#app_destination_google_big_query_google_big_query_destination_action_project) | **POST** /destinations/google_big_query/actions/project | List of projects
[**app_destination_google_big_query_google_big_query_destination_action_write_modes**](DestinationsGoogleBigQueryApi.md#app_destination_google_big_query_google_big_query_destination_action_write_modes) | **POST** /destinations/google_big_query/actions/writeModes | List of write modes
[**app_destination_google_big_query_google_big_query_destination_create**](DestinationsGoogleBigQueryApi.md#app_destination_google_big_query_google_big_query_destination_create) | **POST** /destinations/google_big_query | Create destination


# **app_destination_google_big_query_google_big_query_destination_action_authorization**
> List[ActionAuthorizationResponseInner] app_destination_google_big_query_google_big_query_destination_action_authorization()

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
    api_instance = openapi_client.DestinationsGoogleBigQueryApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_destination_google_big_query_google_big_query_destination_action_authorization()
        print("The response of DestinationsGoogleBigQueryApi->app_destination_google_big_query_google_big_query_destination_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsGoogleBigQueryApi->app_destination_google_big_query_google_big_query_destination_action_authorization: %s\n" % e)
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

# **app_destination_google_big_query_google_big_query_destination_action_dataset**
> List[GoogleAnalyticsControllerActionAccount200ResponseInner] app_destination_google_big_query_google_big_query_destination_action_dataset(app_destination_google_big_query_google_big_query_destination_action_dataset_request=app_destination_google_big_query_google_big_query_destination_action_dataset_request)

List of datasets

### Example


```python
import openapi_client
from openapi_client.models.app_destination_google_big_query_google_big_query_destination_action_dataset_request import AppDestinationGoogleBigQueryGoogleBigQueryDestinationActionDatasetRequest
from openapi_client.models.google_analytics_controller_action_account200_response_inner import GoogleAnalyticsControllerActionAccount200ResponseInner
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
    api_instance = openapi_client.DestinationsGoogleBigQueryApi(api_client)
    app_destination_google_big_query_google_big_query_destination_action_dataset_request = openapi_client.AppDestinationGoogleBigQueryGoogleBigQueryDestinationActionDatasetRequest() # AppDestinationGoogleBigQueryGoogleBigQueryDestinationActionDatasetRequest |  (optional)

    try:
        # List of datasets
        api_response = api_instance.app_destination_google_big_query_google_big_query_destination_action_dataset(app_destination_google_big_query_google_big_query_destination_action_dataset_request=app_destination_google_big_query_google_big_query_destination_action_dataset_request)
        print("The response of DestinationsGoogleBigQueryApi->app_destination_google_big_query_google_big_query_destination_action_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsGoogleBigQueryApi->app_destination_google_big_query_google_big_query_destination_action_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_destination_google_big_query_google_big_query_destination_action_dataset_request** | [**AppDestinationGoogleBigQueryGoogleBigQueryDestinationActionDatasetRequest**](AppDestinationGoogleBigQueryGoogleBigQueryDestinationActionDatasetRequest.md)|  | [optional] 

### Return type

[**List[GoogleAnalyticsControllerActionAccount200ResponseInner]**](GoogleAnalyticsControllerActionAccount200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of datasets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_destination_google_big_query_google_big_query_destination_action_project**
> List[GoogleAnalyticsControllerActionAccount200ResponseInner] app_destination_google_big_query_google_big_query_destination_action_project(app_destination_google_big_query_google_big_query_destination_action_project_request=app_destination_google_big_query_google_big_query_destination_action_project_request)

List of projects

### Example


```python
import openapi_client
from openapi_client.models.app_destination_google_big_query_google_big_query_destination_action_project_request import AppDestinationGoogleBigQueryGoogleBigQueryDestinationActionProjectRequest
from openapi_client.models.google_analytics_controller_action_account200_response_inner import GoogleAnalyticsControllerActionAccount200ResponseInner
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
    api_instance = openapi_client.DestinationsGoogleBigQueryApi(api_client)
    app_destination_google_big_query_google_big_query_destination_action_project_request = openapi_client.AppDestinationGoogleBigQueryGoogleBigQueryDestinationActionProjectRequest() # AppDestinationGoogleBigQueryGoogleBigQueryDestinationActionProjectRequest |  (optional)

    try:
        # List of projects
        api_response = api_instance.app_destination_google_big_query_google_big_query_destination_action_project(app_destination_google_big_query_google_big_query_destination_action_project_request=app_destination_google_big_query_google_big_query_destination_action_project_request)
        print("The response of DestinationsGoogleBigQueryApi->app_destination_google_big_query_google_big_query_destination_action_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsGoogleBigQueryApi->app_destination_google_big_query_google_big_query_destination_action_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_destination_google_big_query_google_big_query_destination_action_project_request** | [**AppDestinationGoogleBigQueryGoogleBigQueryDestinationActionProjectRequest**](AppDestinationGoogleBigQueryGoogleBigQueryDestinationActionProjectRequest.md)|  | [optional] 

### Return type

[**List[GoogleAnalyticsControllerActionAccount200ResponseInner]**](GoogleAnalyticsControllerActionAccount200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of projects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_destination_google_big_query_google_big_query_destination_action_write_modes**
> List[LabelValueResponseInner] app_destination_google_big_query_google_big_query_destination_action_write_modes(app_destination_alloy_db_alloy_db_destination_action_write_modes_request=app_destination_alloy_db_alloy_db_destination_action_write_modes_request)

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
    api_instance = openapi_client.DestinationsGoogleBigQueryApi(api_client)
    app_destination_alloy_db_alloy_db_destination_action_write_modes_request = openapi_client.AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest() # AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest |  (optional)

    try:
        # List of write modes
        api_response = api_instance.app_destination_google_big_query_google_big_query_destination_action_write_modes(app_destination_alloy_db_alloy_db_destination_action_write_modes_request=app_destination_alloy_db_alloy_db_destination_action_write_modes_request)
        print("The response of DestinationsGoogleBigQueryApi->app_destination_google_big_query_google_big_query_destination_action_write_modes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsGoogleBigQueryApi->app_destination_google_big_query_google_big_query_destination_action_write_modes: %s\n" % e)
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

# **app_destination_google_big_query_google_big_query_destination_create**
> GoogleBigQueryDestination app_destination_google_big_query_google_big_query_destination_create(google_big_query_storage_request)

Create destination

### Example


```python
import openapi_client
from openapi_client.models.google_big_query_destination import GoogleBigQueryDestination
from openapi_client.models.google_big_query_storage_request import GoogleBigQueryStorageRequest
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
    api_instance = openapi_client.DestinationsGoogleBigQueryApi(api_client)
    google_big_query_storage_request = openapi_client.GoogleBigQueryStorageRequest() # GoogleBigQueryStorageRequest | 

    try:
        # Create destination
        api_response = api_instance.app_destination_google_big_query_google_big_query_destination_create(google_big_query_storage_request)
        print("The response of DestinationsGoogleBigQueryApi->app_destination_google_big_query_google_big_query_destination_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsGoogleBigQueryApi->app_destination_google_big_query_google_big_query_destination_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_big_query_storage_request** | [**GoogleBigQueryStorageRequest**](GoogleBigQueryStorageRequest.md)|  | 

### Return type

[**GoogleBigQueryDestination**](GoogleBigQueryDestination.md)

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

