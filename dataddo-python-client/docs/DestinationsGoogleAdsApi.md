# openapi_client.DestinationsGoogleAdsApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_destination_google_ads_google_ads_destination_action_conversion_id**](DestinationsGoogleAdsApi.md#app_destination_google_ads_google_ads_destination_action_conversion_id) | **GET** /destinations/google_ads/actions/conversionId | List of Google Ads customers
[**app_destination_google_ads_google_ads_destination_action_destination_fields**](DestinationsGoogleAdsApi.md#app_destination_google_ads_google_ads_destination_action_destination_fields) | **POST** /destinations/google_ads/actions/destinationFields | List of destination fields
[**app_destination_google_ads_google_ads_destination_action_google_customer**](DestinationsGoogleAdsApi.md#app_destination_google_ads_google_ads_destination_action_google_customer) | **GET** /destinations/google_ads/actions/googleCustomer | List of Google Ads customers
[**app_destination_google_ads_google_ads_destination_action_google_manager**](DestinationsGoogleAdsApi.md#app_destination_google_ads_google_ads_destination_action_google_manager) | **GET** /destinations/google_ads/actions/googleManager | List of Google Ads customers
[**app_destination_google_ads_google_ads_destination_action_object**](DestinationsGoogleAdsApi.md#app_destination_google_ads_google_ads_destination_action_object) | **GET** /destinations/google_ads/actions/object | List of Google Ads object types
[**app_destination_google_ads_google_ads_destination_action_source_fields**](DestinationsGoogleAdsApi.md#app_destination_google_ads_google_ads_destination_action_source_fields) | **POST** /destinations/google_ads/actions/sourceFields | List of source fields
[**app_destination_google_ads_google_ads_destination_action_write_modes**](DestinationsGoogleAdsApi.md#app_destination_google_ads_google_ads_destination_action_write_modes) | **POST** /destinations/google_ads/actions/writeModes | List of write modes


# **app_destination_google_ads_google_ads_destination_action_conversion_id**
> List[LabelValueResponseInner] app_destination_google_ads_google_ads_destination_action_conversion_id()

List of Google Ads customers

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
    api_instance = openapi_client.DestinationsGoogleAdsApi(api_client)

    try:
        # List of Google Ads customers
        api_response = api_instance.app_destination_google_ads_google_ads_destination_action_conversion_id()
        print("The response of DestinationsGoogleAdsApi->app_destination_google_ads_google_ads_destination_action_conversion_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsGoogleAdsApi->app_destination_google_ads_google_ads_destination_action_conversion_id: %s\n" % e)
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
**200** | List of Google Ads customers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_destination_google_ads_google_ads_destination_action_destination_fields**
> List[DestinationFieldResponseInner] app_destination_google_ads_google_ads_destination_action_destination_fields(app_destination_exact_online_exact_online_destination_action_destination_fields_request)

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
    api_instance = openapi_client.DestinationsGoogleAdsApi(api_client)
    app_destination_exact_online_exact_online_destination_action_destination_fields_request = openapi_client.AppDestinationExactOnlineExactOnlineDestinationActionDestinationFieldsRequest() # AppDestinationExactOnlineExactOnlineDestinationActionDestinationFieldsRequest | 

    try:
        # List of destination fields
        api_response = api_instance.app_destination_google_ads_google_ads_destination_action_destination_fields(app_destination_exact_online_exact_online_destination_action_destination_fields_request)
        print("The response of DestinationsGoogleAdsApi->app_destination_google_ads_google_ads_destination_action_destination_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsGoogleAdsApi->app_destination_google_ads_google_ads_destination_action_destination_fields: %s\n" % e)
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

# **app_destination_google_ads_google_ads_destination_action_google_customer**
> List[LabelValueResponseInner] app_destination_google_ads_google_ads_destination_action_google_customer()

List of Google Ads customers

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
    api_instance = openapi_client.DestinationsGoogleAdsApi(api_client)

    try:
        # List of Google Ads customers
        api_response = api_instance.app_destination_google_ads_google_ads_destination_action_google_customer()
        print("The response of DestinationsGoogleAdsApi->app_destination_google_ads_google_ads_destination_action_google_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsGoogleAdsApi->app_destination_google_ads_google_ads_destination_action_google_customer: %s\n" % e)
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
**200** | List of Google Ads customers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_destination_google_ads_google_ads_destination_action_google_manager**
> List[LabelValueResponseInner] app_destination_google_ads_google_ads_destination_action_google_manager()

List of Google Ads customers

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
    api_instance = openapi_client.DestinationsGoogleAdsApi(api_client)

    try:
        # List of Google Ads customers
        api_response = api_instance.app_destination_google_ads_google_ads_destination_action_google_manager()
        print("The response of DestinationsGoogleAdsApi->app_destination_google_ads_google_ads_destination_action_google_manager:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsGoogleAdsApi->app_destination_google_ads_google_ads_destination_action_google_manager: %s\n" % e)
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
**200** | List of Google Ads customers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_destination_google_ads_google_ads_destination_action_object**
> List[LabelValueResponseInner] app_destination_google_ads_google_ads_destination_action_object()

List of Google Ads object types

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
    api_instance = openapi_client.DestinationsGoogleAdsApi(api_client)

    try:
        # List of Google Ads object types
        api_response = api_instance.app_destination_google_ads_google_ads_destination_action_object()
        print("The response of DestinationsGoogleAdsApi->app_destination_google_ads_google_ads_destination_action_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsGoogleAdsApi->app_destination_google_ads_google_ads_destination_action_object: %s\n" % e)
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
**200** | List of Google Ads object types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_destination_google_ads_google_ads_destination_action_source_fields**
> List[SourceFieldResponseInner] app_destination_google_ads_google_ads_destination_action_source_fields(flow_preview_request)

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
    api_instance = openapi_client.DestinationsGoogleAdsApi(api_client)
    flow_preview_request = openapi_client.FlowPreviewRequest() # FlowPreviewRequest | 

    try:
        # List of source fields
        api_response = api_instance.app_destination_google_ads_google_ads_destination_action_source_fields(flow_preview_request)
        print("The response of DestinationsGoogleAdsApi->app_destination_google_ads_google_ads_destination_action_source_fields:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsGoogleAdsApi->app_destination_google_ads_google_ads_destination_action_source_fields: %s\n" % e)
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

# **app_destination_google_ads_google_ads_destination_action_write_modes**
> List[LabelValueResponseInner] app_destination_google_ads_google_ads_destination_action_write_modes(app_destination_alloy_db_alloy_db_destination_action_write_modes_request=app_destination_alloy_db_alloy_db_destination_action_write_modes_request)

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
    api_instance = openapi_client.DestinationsGoogleAdsApi(api_client)
    app_destination_alloy_db_alloy_db_destination_action_write_modes_request = openapi_client.AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest() # AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest |  (optional)

    try:
        # List of write modes
        api_response = api_instance.app_destination_google_ads_google_ads_destination_action_write_modes(app_destination_alloy_db_alloy_db_destination_action_write_modes_request=app_destination_alloy_db_alloy_db_destination_action_write_modes_request)
        print("The response of DestinationsGoogleAdsApi->app_destination_google_ads_google_ads_destination_action_write_modes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsGoogleAdsApi->app_destination_google_ads_google_ads_destination_action_write_modes: %s\n" % e)
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

