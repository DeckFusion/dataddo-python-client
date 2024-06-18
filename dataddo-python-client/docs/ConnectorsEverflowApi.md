# openapi_client.ConnectorsEverflowApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**everflow_controller_action_authorization**](ConnectorsEverflowApi.md#everflow_controller_action_authorization) | **GET** /connectors/everflow/actions/authorization | List of authorization objects
[**everflow_controller_action_column**](ConnectorsEverflowApi.md#everflow_controller_action_column) | **GET** /connectors/everflow/actions/column | List of all columns
[**everflow_controller_action_currency**](ConnectorsEverflowApi.md#everflow_controller_action_currency) | **GET** /connectors/everflow/actions/currency | List of all currencies
[**everflow_controller_action_date_range**](ConnectorsEverflowApi.md#everflow_controller_action_date_range) | **GET** /connectors/everflow/actions/dateRange | List of all date ranges
[**everflow_controller_action_load**](ConnectorsEverflowApi.md#everflow_controller_action_load) | **POST** /connectors/everflow/create-source | Create Everflow source
[**everflow_controller_action_metric**](ConnectorsEverflowApi.md#everflow_controller_action_metric) | **POST** /connectors/everflow/actions/metric | List of all metrics
[**everflow_controller_action_preview**](ConnectorsEverflowApi.md#everflow_controller_action_preview) | **POST** /connectors/everflow/preview | Preview the data
[**everflow_controller_action_report_type**](ConnectorsEverflowApi.md#everflow_controller_action_report_type) | **GET** /connectors/everflow/actions/reportType | List of all report types
[**everflow_controller_action_time_column**](ConnectorsEverflowApi.md#everflow_controller_action_time_column) | **GET** /connectors/everflow/actions/timeColumn | List of all time columns
[**everflow_controller_action_timezone_id**](ConnectorsEverflowApi.md#everflow_controller_action_timezone_id) | **GET** /connectors/everflow/actions/timezoneId | List of all timezones


# **everflow_controller_action_authorization**
> List[ActionAuthorizationResponseInner] everflow_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsEverflowApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.everflow_controller_action_authorization()
        print("The response of ConnectorsEverflowApi->everflow_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsEverflowApi->everflow_controller_action_authorization: %s\n" % e)
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

# **everflow_controller_action_column**
> List[LabelValueResponseInner] everflow_controller_action_column()

List of all columns

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
    api_instance = openapi_client.ConnectorsEverflowApi(api_client)

    try:
        # List of all columns
        api_response = api_instance.everflow_controller_action_column()
        print("The response of ConnectorsEverflowApi->everflow_controller_action_column:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsEverflowApi->everflow_controller_action_column: %s\n" % e)
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
**200** | List of column objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **everflow_controller_action_currency**
> List[LabelValueResponseInner] everflow_controller_action_currency()

List of all currencies

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
    api_instance = openapi_client.ConnectorsEverflowApi(api_client)

    try:
        # List of all currencies
        api_response = api_instance.everflow_controller_action_currency()
        print("The response of ConnectorsEverflowApi->everflow_controller_action_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsEverflowApi->everflow_controller_action_currency: %s\n" % e)
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
**200** | List of currency objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **everflow_controller_action_date_range**
> List[LabelValueResponseInner] everflow_controller_action_date_range()

List of all date ranges

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
    api_instance = openapi_client.ConnectorsEverflowApi(api_client)

    try:
        # List of all date ranges
        api_response = api_instance.everflow_controller_action_date_range()
        print("The response of ConnectorsEverflowApi->everflow_controller_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsEverflowApi->everflow_controller_action_date_range: %s\n" % e)
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
**200** | List of Everflow date ranges |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **everflow_controller_action_load**
> Source everflow_controller_action_load(everflow_connector_form=everflow_connector_form)

Create Everflow source

### Example


```python
import openapi_client
from openapi_client.models.everflow_connector_form import EverflowConnectorForm
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
    api_instance = openapi_client.ConnectorsEverflowApi(api_client)
    everflow_connector_form = openapi_client.EverflowConnectorForm() # EverflowConnectorForm |  (optional)

    try:
        # Create Everflow source
        api_response = api_instance.everflow_controller_action_load(everflow_connector_form=everflow_connector_form)
        print("The response of ConnectorsEverflowApi->everflow_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsEverflowApi->everflow_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **everflow_connector_form** | [**EverflowConnectorForm**](EverflowConnectorForm.md)|  | [optional] 

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

# **everflow_controller_action_metric**
> List[LabelValueResponseInner] everflow_controller_action_metric(everflow_controller_action_metric_request=everflow_controller_action_metric_request)

List of all metrics

### Example


```python
import openapi_client
from openapi_client.models.everflow_controller_action_metric_request import EverflowControllerActionMetricRequest
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
    api_instance = openapi_client.ConnectorsEverflowApi(api_client)
    everflow_controller_action_metric_request = openapi_client.EverflowControllerActionMetricRequest() # EverflowControllerActionMetricRequest |  (optional)

    try:
        # List of all metrics
        api_response = api_instance.everflow_controller_action_metric(everflow_controller_action_metric_request=everflow_controller_action_metric_request)
        print("The response of ConnectorsEverflowApi->everflow_controller_action_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsEverflowApi->everflow_controller_action_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **everflow_controller_action_metric_request** | [**EverflowControllerActionMetricRequest**](EverflowControllerActionMetricRequest.md)|  | [optional] 

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
**200** | List of Everflow metrics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **everflow_controller_action_preview**
> SuccessResponse everflow_controller_action_preview(everflow_connector_form=everflow_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.everflow_connector_form import EverflowConnectorForm
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
    api_instance = openapi_client.ConnectorsEverflowApi(api_client)
    everflow_connector_form = openapi_client.EverflowConnectorForm() # EverflowConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.everflow_controller_action_preview(everflow_connector_form=everflow_connector_form)
        print("The response of ConnectorsEverflowApi->everflow_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsEverflowApi->everflow_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **everflow_connector_form** | [**EverflowConnectorForm**](EverflowConnectorForm.md)|  | [optional] 

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

# **everflow_controller_action_report_type**
> List[LabelValueResponseInner] everflow_controller_action_report_type()

List of all report types

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
    api_instance = openapi_client.ConnectorsEverflowApi(api_client)

    try:
        # List of all report types
        api_response = api_instance.everflow_controller_action_report_type()
        print("The response of ConnectorsEverflowApi->everflow_controller_action_report_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsEverflowApi->everflow_controller_action_report_type: %s\n" % e)
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
**200** | List of report types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **everflow_controller_action_time_column**
> List[LabelValueResponseInner] everflow_controller_action_time_column()

List of all time columns

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
    api_instance = openapi_client.ConnectorsEverflowApi(api_client)

    try:
        # List of all time columns
        api_response = api_instance.everflow_controller_action_time_column()
        print("The response of ConnectorsEverflowApi->everflow_controller_action_time_column:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsEverflowApi->everflow_controller_action_time_column: %s\n" % e)
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
**200** | List of time column objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **everflow_controller_action_timezone_id**
> List[LabelValueResponseInner] everflow_controller_action_timezone_id()

List of all timezones

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
    api_instance = openapi_client.ConnectorsEverflowApi(api_client)

    try:
        # List of all timezones
        api_response = api_instance.everflow_controller_action_timezone_id()
        print("The response of ConnectorsEverflowApi->everflow_controller_action_timezone_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsEverflowApi->everflow_controller_action_timezone_id: %s\n" % e)
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
**200** | List of timezone objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

