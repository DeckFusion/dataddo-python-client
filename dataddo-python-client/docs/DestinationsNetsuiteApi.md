# openapi_client.DestinationsNetsuiteApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_destination_netsuite_netsuite_destination_action_authorization**](DestinationsNetsuiteApi.md#app_destination_netsuite_netsuite_destination_action_authorization) | **GET** /destinations/netsuite/actions/authorization | List of authorization objects
[**app_destination_netsuite_netsuite_destination_action_destination_fields**](DestinationsNetsuiteApi.md#app_destination_netsuite_netsuite_destination_action_destination_fields) | **POST** /destinations/netsuite/actions/destinationFields | List of destination fields
[**app_destination_netsuite_netsuite_destination_action_endpoint**](DestinationsNetsuiteApi.md#app_destination_netsuite_netsuite_destination_action_endpoint) | **GET** /destinations/netsuite/actions/endpoint | List of endpoints
[**app_destination_netsuite_netsuite_destination_action_source_fields**](DestinationsNetsuiteApi.md#app_destination_netsuite_netsuite_destination_action_source_fields) | **POST** /destinations/netsuite/actions/sourceFields | List of source fields
[**app_destination_netsuite_netsuite_destination_action_write_modes**](DestinationsNetsuiteApi.md#app_destination_netsuite_netsuite_destination_action_write_modes) | **POST** /destinations/netsuite/actions/writeModes | List of write modes
[**app_destination_netsuite_netsuite_destination_create**](DestinationsNetsuiteApi.md#app_destination_netsuite_netsuite_destination_create) | **POST** /destinations/netsuite | Create destination


# **app_destination_netsuite_netsuite_destination_action_authorization**
> List[ActionAuthorizationResponseInner] app_destination_netsuite_netsuite_destination_action_authorization()

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
    api_instance = openapi_client.DestinationsNetsuiteApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_destination_netsuite_netsuite_destination_action_authorization()
        print("The response of DestinationsNetsuiteApi->app_destination_netsuite_netsuite_destination_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsNetsuiteApi->app_destination_netsuite_netsuite_destination_action_authorization: %s\n" % e)
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

# **app_destination_netsuite_netsuite_destination_action_destination_fields**
> List[DestinationFieldResponseInner] app_destination_netsuite_netsuite_destination_action_destination_fields(app_destination_exact_online_exact_online_destination_action_destination_fields_request)

List of destination fields

### Example


```python
import openapi_client
from openapi_client.models.app_destination_exact_online_exact_online_destination_action_destination_fields_request import AppDestinationExactOnlineExactOnlineDestinationActionDestinationFieldsRequest
from openapi_client.models.destination_field_response_inner import DestinationFieldResponseInner
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
    api_instance = openapi_client.DestinationsNetsuiteApi(api_client)
    app_destination_exact_online_exact_online_destination_action_destination_fields_request = openapi_client.AppDestinationExactOnlineExactOnlineDestinationActionDestinationFieldsRequest() # AppDestinationExactOnlineExactOnlineDestinationActionDestinationFieldsRequest | 

    try:
        # List of destination fields
        api_response = api_instance.app_destination_netsuite_netsuite_destination_action_destination_fields(app_destination_exact_online_exact_online_destination_action_destination_fields_request)
        print("The response of DestinationsNetsuiteApi->app_destination_netsuite_netsuite_destination_action_destination_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsNetsuiteApi->app_destination_netsuite_netsuite_destination_action_destination_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_destination_exact_online_exact_online_destination_action_destination_fields_request** | [**AppDestinationExactOnlineExactOnlineDestinationActionDestinationFieldsRequest**](AppDestinationExactOnlineExactOnlineDestinationActionDestinationFieldsRequest.md)|  | 

### Return type

[**List[DestinationFieldResponseInner]**](DestinationFieldResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of destination fields |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_destination_netsuite_netsuite_destination_action_endpoint**
> List[LabelValueResponseInner] app_destination_netsuite_netsuite_destination_action_endpoint()

List of endpoints

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
    api_instance = openapi_client.DestinationsNetsuiteApi(api_client)

    try:
        # List of endpoints
        api_response = api_instance.app_destination_netsuite_netsuite_destination_action_endpoint()
        print("The response of DestinationsNetsuiteApi->app_destination_netsuite_netsuite_destination_action_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsNetsuiteApi->app_destination_netsuite_netsuite_destination_action_endpoint: %s\n" % e)
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
**200** | List of endpoints |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_destination_netsuite_netsuite_destination_action_source_fields**
> List[SourceFieldResponseInner] app_destination_netsuite_netsuite_destination_action_source_fields(flow_preview_request)

List of source fields

### Example


```python
import openapi_client
from openapi_client.models.flow_preview_request import FlowPreviewRequest
from openapi_client.models.source_field_response_inner import SourceFieldResponseInner
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
    api_instance = openapi_client.DestinationsNetsuiteApi(api_client)
    flow_preview_request = openapi_client.FlowPreviewRequest() # FlowPreviewRequest | 

    try:
        # List of source fields
        api_response = api_instance.app_destination_netsuite_netsuite_destination_action_source_fields(flow_preview_request)
        print("The response of DestinationsNetsuiteApi->app_destination_netsuite_netsuite_destination_action_source_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsNetsuiteApi->app_destination_netsuite_netsuite_destination_action_source_fields: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_preview_request** | [**FlowPreviewRequest**](FlowPreviewRequest.md)|  | 

### Return type

[**List[SourceFieldResponseInner]**](SourceFieldResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of source fields |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_destination_netsuite_netsuite_destination_action_write_modes**
> List[LabelValueResponseInner] app_destination_netsuite_netsuite_destination_action_write_modes(app_destination_alloy_db_alloy_db_destination_action_write_modes_request=app_destination_alloy_db_alloy_db_destination_action_write_modes_request)

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
    api_instance = openapi_client.DestinationsNetsuiteApi(api_client)
    app_destination_alloy_db_alloy_db_destination_action_write_modes_request = openapi_client.AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest() # AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest |  (optional)

    try:
        # List of write modes
        api_response = api_instance.app_destination_netsuite_netsuite_destination_action_write_modes(app_destination_alloy_db_alloy_db_destination_action_write_modes_request=app_destination_alloy_db_alloy_db_destination_action_write_modes_request)
        print("The response of DestinationsNetsuiteApi->app_destination_netsuite_netsuite_destination_action_write_modes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsNetsuiteApi->app_destination_netsuite_netsuite_destination_action_write_modes: %s\n" % e)
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

# **app_destination_netsuite_netsuite_destination_create**
> NetsuiteDestination app_destination_netsuite_netsuite_destination_create(netsuite_storage_request)

Create destination

### Example


```python
import openapi_client
from openapi_client.models.netsuite_destination import NetsuiteDestination
from openapi_client.models.netsuite_storage_request import NetsuiteStorageRequest
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
    api_instance = openapi_client.DestinationsNetsuiteApi(api_client)
    netsuite_storage_request = openapi_client.NetsuiteStorageRequest() # NetsuiteStorageRequest | 

    try:
        # Create destination
        api_response = api_instance.app_destination_netsuite_netsuite_destination_create(netsuite_storage_request)
        print("The response of DestinationsNetsuiteApi->app_destination_netsuite_netsuite_destination_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsNetsuiteApi->app_destination_netsuite_netsuite_destination_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **netsuite_storage_request** | [**NetsuiteStorageRequest**](NetsuiteStorageRequest.md)|  | 

### Return type

[**NetsuiteDestination**](NetsuiteDestination.md)

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

