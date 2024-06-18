# openapi_client.ConnectorsPinterestApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pinterest_controller_action_advertiser**](ConnectorsPinterestApi.md#pinterest_controller_action_advertiser) | **POST** /connectors/pinterest/actions/advertiser | List of ads accounts
[**pinterest_controller_action_authorization**](ConnectorsPinterestApi.md#pinterest_controller_action_authorization) | **GET** /connectors/pinterest/actions/authorization | List of authorization objects
[**pinterest_controller_action_click_window_days**](ConnectorsPinterestApi.md#pinterest_controller_action_click_window_days) | **GET** /connectors/pinterest/actions/clickWindowDays | List of click windows
[**pinterest_controller_action_column**](ConnectorsPinterestApi.md#pinterest_controller_action_column) | **POST** /connectors/pinterest/actions/column | List of columns
[**pinterest_controller_action_conversion_time**](ConnectorsPinterestApi.md#pinterest_controller_action_conversion_time) | **GET** /connectors/pinterest/actions/conversionTime | List of conversion times
[**pinterest_controller_action_data_label**](ConnectorsPinterestApi.md#pinterest_controller_action_data_label) | **POST** /connectors/pinterest/actions/dataLabel | List of data labels
[**pinterest_controller_action_date_range**](ConnectorsPinterestApi.md#pinterest_controller_action_date_range) | **GET** /connectors/pinterest/actions/dateRange | List of date ranges
[**pinterest_controller_action_engagement_window_days**](ConnectorsPinterestApi.md#pinterest_controller_action_engagement_window_days) | **GET** /connectors/pinterest/actions/engagementWindowDays | List of engagement windows
[**pinterest_controller_action_granularity**](ConnectorsPinterestApi.md#pinterest_controller_action_granularity) | **GET** /connectors/pinterest/actions/granularity | List of time breakdowns
[**pinterest_controller_action_load**](ConnectorsPinterestApi.md#pinterest_controller_action_load) | **POST** /connectors/pinterest/create-source | Create Pinterest source
[**pinterest_controller_action_preview**](ConnectorsPinterestApi.md#pinterest_controller_action_preview) | **POST** /connectors/pinterest/preview | Preview the data
[**pinterest_controller_action_report_level**](ConnectorsPinterestApi.md#pinterest_controller_action_report_level) | **GET** /connectors/pinterest/actions/reportLevel | List of reporting levels
[**pinterest_controller_action_view_window_days**](ConnectorsPinterestApi.md#pinterest_controller_action_view_window_days) | **GET** /connectors/pinterest/actions/viewWindowDays | List of view windows


# **pinterest_controller_action_advertiser**
> List[LabelValueResponseInner] pinterest_controller_action_advertiser(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List of ads accounts

Gets all Advertisers ID. Data is displayed in connector form Is truncating the value of the advertise_id at the moment

### Example


```python
import openapi_client
from openapi_client.models.amazon_ads_controller_action_profile_request_value import AmazonAdsControllerActionProfileRequestValue
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
    api_instance = openapi_client.ConnectorsPinterestApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List of ads accounts
        api_response = api_instance.pinterest_controller_action_advertiser(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsPinterestApi->pinterest_controller_action_advertiser:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsPinterestApi->pinterest_controller_action_advertiser: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_ads_controller_action_profile_request_value** | [**AmazonAdsControllerActionProfileRequestValue**](AmazonAdsControllerActionProfileRequestValue.md)|  | [optional] 

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
**200** | List of ads accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pinterest_controller_action_authorization**
> List[ActionAuthorizationResponseInner] pinterest_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsPinterestApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.pinterest_controller_action_authorization()
        print("The response of ConnectorsPinterestApi->pinterest_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsPinterestApi->pinterest_controller_action_authorization: %s\n" % e)
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

# **pinterest_controller_action_click_window_days**
> List[LabelValueResponseInner] pinterest_controller_action_click_window_days()

List of click windows

View window days.

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
    api_instance = openapi_client.ConnectorsPinterestApi(api_client)

    try:
        # List of click windows
        api_response = api_instance.pinterest_controller_action_click_window_days()
        print("The response of ConnectorsPinterestApi->pinterest_controller_action_click_window_days:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsPinterestApi->pinterest_controller_action_click_window_days: %s\n" % e)
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
**200** | List of click windows |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pinterest_controller_action_column**
> List[LabelValueResponseInner] pinterest_controller_action_column(pinterest_controller_action_column_request=pinterest_controller_action_column_request)

List of columns

List all columns

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.pinterest_controller_action_column_request import PinterestControllerActionColumnRequest
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
    api_instance = openapi_client.ConnectorsPinterestApi(api_client)
    pinterest_controller_action_column_request = openapi_client.PinterestControllerActionColumnRequest() # PinterestControllerActionColumnRequest |  (optional)

    try:
        # List of columns
        api_response = api_instance.pinterest_controller_action_column(pinterest_controller_action_column_request=pinterest_controller_action_column_request)
        print("The response of ConnectorsPinterestApi->pinterest_controller_action_column:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsPinterestApi->pinterest_controller_action_column: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pinterest_controller_action_column_request** | [**PinterestControllerActionColumnRequest**](PinterestControllerActionColumnRequest.md)|  | [optional] 

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
**200** | List of columns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pinterest_controller_action_conversion_time**
> List[LabelValueResponseInner] pinterest_controller_action_conversion_time()

List of conversion times

Conversion report time.

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
    api_instance = openapi_client.ConnectorsPinterestApi(api_client)

    try:
        # List of conversion times
        api_response = api_instance.pinterest_controller_action_conversion_time()
        print("The response of ConnectorsPinterestApi->pinterest_controller_action_conversion_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsPinterestApi->pinterest_controller_action_conversion_time: %s\n" % e)
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
**200** | List of conversion times |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pinterest_controller_action_data_label**
> List[LabelValueResponseInner] pinterest_controller_action_data_label(pinterest_controller_action_column_request=pinterest_controller_action_column_request)

List of data labels

List all data labels

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.pinterest_controller_action_column_request import PinterestControllerActionColumnRequest
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
    api_instance = openapi_client.ConnectorsPinterestApi(api_client)
    pinterest_controller_action_column_request = openapi_client.PinterestControllerActionColumnRequest() # PinterestControllerActionColumnRequest |  (optional)

    try:
        # List of data labels
        api_response = api_instance.pinterest_controller_action_data_label(pinterest_controller_action_column_request=pinterest_controller_action_column_request)
        print("The response of ConnectorsPinterestApi->pinterest_controller_action_data_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsPinterestApi->pinterest_controller_action_data_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pinterest_controller_action_column_request** | [**PinterestControllerActionColumnRequest**](PinterestControllerActionColumnRequest.md)|  | [optional] 

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
**200** | List of data labels |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pinterest_controller_action_date_range**
> List[LabelValueResponseInner] pinterest_controller_action_date_range()

List of date ranges

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
    api_instance = openapi_client.ConnectorsPinterestApi(api_client)

    try:
        # List of date ranges
        api_response = api_instance.pinterest_controller_action_date_range()
        print("The response of ConnectorsPinterestApi->pinterest_controller_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsPinterestApi->pinterest_controller_action_date_range: %s\n" % e)
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
**200** | List of date range objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pinterest_controller_action_engagement_window_days**
> List[LabelValueResponseInner] pinterest_controller_action_engagement_window_days()

List of engagement windows

View window days.

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
    api_instance = openapi_client.ConnectorsPinterestApi(api_client)

    try:
        # List of engagement windows
        api_response = api_instance.pinterest_controller_action_engagement_window_days()
        print("The response of ConnectorsPinterestApi->pinterest_controller_action_engagement_window_days:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsPinterestApi->pinterest_controller_action_engagement_window_days: %s\n" % e)
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
**200** | List of engagement windows |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pinterest_controller_action_granularity**
> List[LabelValueResponseInner] pinterest_controller_action_granularity()

List of time breakdowns

Granularity.

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
    api_instance = openapi_client.ConnectorsPinterestApi(api_client)

    try:
        # List of time breakdowns
        api_response = api_instance.pinterest_controller_action_granularity()
        print("The response of ConnectorsPinterestApi->pinterest_controller_action_granularity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsPinterestApi->pinterest_controller_action_granularity: %s\n" % e)
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
**200** | List of time breakdowns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pinterest_controller_action_load**
> Source pinterest_controller_action_load(pinterest_connector_form=pinterest_connector_form)

Create Pinterest source

### Example


```python
import openapi_client
from openapi_client.models.pinterest_connector_form import PinterestConnectorForm
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
    api_instance = openapi_client.ConnectorsPinterestApi(api_client)
    pinterest_connector_form = openapi_client.PinterestConnectorForm() # PinterestConnectorForm |  (optional)

    try:
        # Create Pinterest source
        api_response = api_instance.pinterest_controller_action_load(pinterest_connector_form=pinterest_connector_form)
        print("The response of ConnectorsPinterestApi->pinterest_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsPinterestApi->pinterest_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pinterest_connector_form** | [**PinterestConnectorForm**](PinterestConnectorForm.md)|  | [optional] 

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
**200** | Create source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pinterest_controller_action_preview**
> SuccessResponse pinterest_controller_action_preview(pinterest_connector_form=pinterest_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.pinterest_connector_form import PinterestConnectorForm
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
    api_instance = openapi_client.ConnectorsPinterestApi(api_client)
    pinterest_connector_form = openapi_client.PinterestConnectorForm() # PinterestConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.pinterest_controller_action_preview(pinterest_connector_form=pinterest_connector_form)
        print("The response of ConnectorsPinterestApi->pinterest_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsPinterestApi->pinterest_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pinterest_connector_form** | [**PinterestConnectorForm**](PinterestConnectorForm.md)|  | [optional] 

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

# **pinterest_controller_action_report_level**
> List[LabelValueResponseInner] pinterest_controller_action_report_level()

List of reporting levels

Reporting Level

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
    api_instance = openapi_client.ConnectorsPinterestApi(api_client)

    try:
        # List of reporting levels
        api_response = api_instance.pinterest_controller_action_report_level()
        print("The response of ConnectorsPinterestApi->pinterest_controller_action_report_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsPinterestApi->pinterest_controller_action_report_level: %s\n" % e)
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
**200** | List of reporting levels |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pinterest_controller_action_view_window_days**
> List[LabelValueResponseInner] pinterest_controller_action_view_window_days()

List of view windows

View window days.

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
    api_instance = openapi_client.ConnectorsPinterestApi(api_client)

    try:
        # List of view windows
        api_response = api_instance.pinterest_controller_action_view_window_days()
        print("The response of ConnectorsPinterestApi->pinterest_controller_action_view_window_days:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsPinterestApi->pinterest_controller_action_view_window_days: %s\n" % e)
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
**200** | List of view windows |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

