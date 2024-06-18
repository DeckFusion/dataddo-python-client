# openapi_client.ConnectorsAmazonDspApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_amazon_dsp_amazon_dsp_connector_action_account_id**](ConnectorsAmazonDspApi.md#app_connector_amazon_dsp_amazon_dsp_connector_action_account_id) | **POST** /connectors/amazon_dsp/actions/accountId | List of Amazon Dsp account ids
[**app_connector_amazon_dsp_amazon_dsp_connector_action_date_range**](ConnectorsAmazonDspApi.md#app_connector_amazon_dsp_amazon_dsp_connector_action_date_range) | **GET** /connectors/amazon_dsp/actions/dateRange | Method for listing date range
[**app_connector_amazon_dsp_amazon_dsp_connector_action_dimensions**](ConnectorsAmazonDspApi.md#app_connector_amazon_dsp_amazon_dsp_connector_action_dimensions) | **GET** /connectors/amazon_dsp/actions/dimensions | List of Amazon Dsp common fields
[**app_connector_amazon_dsp_amazon_dsp_connector_action_metrics**](ConnectorsAmazonDspApi.md#app_connector_amazon_dsp_amazon_dsp_connector_action_metrics) | **POST** /connectors/amazon_dsp/actions/metrics | List of Amazon Dsp common fields
[**app_connector_amazon_dsp_amazon_dsp_connector_action_report_type**](ConnectorsAmazonDspApi.md#app_connector_amazon_dsp_amazon_dsp_connector_action_report_type) | **GET** /connectors/amazon_dsp/actions/reportType | List of Amazon Dsp common fields
[**app_connector_amazon_dsp_amazon_dsp_connector_action_time_unit**](ConnectorsAmazonDspApi.md#app_connector_amazon_dsp_amazon_dsp_connector_action_time_unit) | **GET** /connectors/amazon_dsp/actions/timeUnit | List of Amazon Dsp common fields
[**app_connector_amazon_dsp_amazon_dsp_connector_preview**](ConnectorsAmazonDspApi.md#app_connector_amazon_dsp_amazon_dsp_connector_preview) | **POST** /connectors/amazon_dsp/preview | Data preview


# **app_connector_amazon_dsp_amazon_dsp_connector_action_account_id**
> List[LabelValueResponseInner] app_connector_amazon_dsp_amazon_dsp_connector_action_account_id(app_connector_amazon_dsp_amazon_dsp_connector_action_account_id_request=app_connector_amazon_dsp_amazon_dsp_connector_action_account_id_request)

List of Amazon Dsp account ids

### Example


```python
import openapi_client
from openapi_client.models.app_connector_amazon_dsp_amazon_dsp_connector_action_account_id_request import AppConnectorAmazonDspAmazonDspConnectorActionAccountIdRequest
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
    api_instance = openapi_client.ConnectorsAmazonDspApi(api_client)
    app_connector_amazon_dsp_amazon_dsp_connector_action_account_id_request = openapi_client.AppConnectorAmazonDspAmazonDspConnectorActionAccountIdRequest() # AppConnectorAmazonDspAmazonDspConnectorActionAccountIdRequest |  (optional)

    try:
        # List of Amazon Dsp account ids
        api_response = api_instance.app_connector_amazon_dsp_amazon_dsp_connector_action_account_id(app_connector_amazon_dsp_amazon_dsp_connector_action_account_id_request=app_connector_amazon_dsp_amazon_dsp_connector_action_account_id_request)
        print("The response of ConnectorsAmazonDspApi->app_connector_amazon_dsp_amazon_dsp_connector_action_account_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAmazonDspApi->app_connector_amazon_dsp_amazon_dsp_connector_action_account_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_connector_amazon_dsp_amazon_dsp_connector_action_account_id_request** | [**AppConnectorAmazonDspAmazonDspConnectorActionAccountIdRequest**](AppConnectorAmazonDspAmazonDspConnectorActionAccountIdRequest.md)|  | [optional] 

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
**200** | List of available fields |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_amazon_dsp_amazon_dsp_connector_action_date_range**
> List[LabelValueResponseInner] app_connector_amazon_dsp_amazon_dsp_connector_action_date_range()

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
    api_instance = openapi_client.ConnectorsAmazonDspApi(api_client)

    try:
        # Method for listing date range
        api_response = api_instance.app_connector_amazon_dsp_amazon_dsp_connector_action_date_range()
        print("The response of ConnectorsAmazonDspApi->app_connector_amazon_dsp_amazon_dsp_connector_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAmazonDspApi->app_connector_amazon_dsp_amazon_dsp_connector_action_date_range: %s\n" % e)
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
**200** | List of AmazonDsp date ranges |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_amazon_dsp_amazon_dsp_connector_action_dimensions**
> List[LabelValueResponseInner] app_connector_amazon_dsp_amazon_dsp_connector_action_dimensions()

List of Amazon Dsp common fields

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
    api_instance = openapi_client.ConnectorsAmazonDspApi(api_client)

    try:
        # List of Amazon Dsp common fields
        api_response = api_instance.app_connector_amazon_dsp_amazon_dsp_connector_action_dimensions()
        print("The response of ConnectorsAmazonDspApi->app_connector_amazon_dsp_amazon_dsp_connector_action_dimensions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAmazonDspApi->app_connector_amazon_dsp_amazon_dsp_connector_action_dimensions: %s\n" % e)
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
**200** | List of available fields |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_amazon_dsp_amazon_dsp_connector_action_metrics**
> List[LabelValueResponseInner] app_connector_amazon_dsp_amazon_dsp_connector_action_metrics(app_connector_amazon_dsp_amazon_dsp_connector_action_metrics_request=app_connector_amazon_dsp_amazon_dsp_connector_action_metrics_request)

List of Amazon Dsp common fields

### Example


```python
import openapi_client
from openapi_client.models.app_connector_amazon_dsp_amazon_dsp_connector_action_metrics_request import AppConnectorAmazonDspAmazonDspConnectorActionMetricsRequest
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
    api_instance = openapi_client.ConnectorsAmazonDspApi(api_client)
    app_connector_amazon_dsp_amazon_dsp_connector_action_metrics_request = openapi_client.AppConnectorAmazonDspAmazonDspConnectorActionMetricsRequest() # AppConnectorAmazonDspAmazonDspConnectorActionMetricsRequest |  (optional)

    try:
        # List of Amazon Dsp common fields
        api_response = api_instance.app_connector_amazon_dsp_amazon_dsp_connector_action_metrics(app_connector_amazon_dsp_amazon_dsp_connector_action_metrics_request=app_connector_amazon_dsp_amazon_dsp_connector_action_metrics_request)
        print("The response of ConnectorsAmazonDspApi->app_connector_amazon_dsp_amazon_dsp_connector_action_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAmazonDspApi->app_connector_amazon_dsp_amazon_dsp_connector_action_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_connector_amazon_dsp_amazon_dsp_connector_action_metrics_request** | [**AppConnectorAmazonDspAmazonDspConnectorActionMetricsRequest**](AppConnectorAmazonDspAmazonDspConnectorActionMetricsRequest.md)|  | [optional] 

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
**200** | List of available fields |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_amazon_dsp_amazon_dsp_connector_action_report_type**
> List[LabelValueResponseInner] app_connector_amazon_dsp_amazon_dsp_connector_action_report_type()

List of Amazon Dsp common fields

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
    api_instance = openapi_client.ConnectorsAmazonDspApi(api_client)

    try:
        # List of Amazon Dsp common fields
        api_response = api_instance.app_connector_amazon_dsp_amazon_dsp_connector_action_report_type()
        print("The response of ConnectorsAmazonDspApi->app_connector_amazon_dsp_amazon_dsp_connector_action_report_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAmazonDspApi->app_connector_amazon_dsp_amazon_dsp_connector_action_report_type: %s\n" % e)
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
**200** | List of available fields |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_amazon_dsp_amazon_dsp_connector_action_time_unit**
> List[LabelValueResponseInner] app_connector_amazon_dsp_amazon_dsp_connector_action_time_unit()

List of Amazon Dsp common fields

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
    api_instance = openapi_client.ConnectorsAmazonDspApi(api_client)

    try:
        # List of Amazon Dsp common fields
        api_response = api_instance.app_connector_amazon_dsp_amazon_dsp_connector_action_time_unit()
        print("The response of ConnectorsAmazonDspApi->app_connector_amazon_dsp_amazon_dsp_connector_action_time_unit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAmazonDspApi->app_connector_amazon_dsp_amazon_dsp_connector_action_time_unit: %s\n" % e)
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
**200** | List of available fields |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_amazon_dsp_amazon_dsp_connector_preview**
> SuccessResponse app_connector_amazon_dsp_amazon_dsp_connector_preview(amazon_dsp_dto=amazon_dsp_dto)

Data preview

### Example


```python
import openapi_client
from openapi_client.models.amazon_dsp_dto import AmazonDspDto
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
    api_instance = openapi_client.ConnectorsAmazonDspApi(api_client)
    amazon_dsp_dto = openapi_client.AmazonDspDto() # AmazonDspDto |  (optional)

    try:
        # Data preview
        api_response = api_instance.app_connector_amazon_dsp_amazon_dsp_connector_preview(amazon_dsp_dto=amazon_dsp_dto)
        print("The response of ConnectorsAmazonDspApi->app_connector_amazon_dsp_amazon_dsp_connector_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAmazonDspApi->app_connector_amazon_dsp_amazon_dsp_connector_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_dsp_dto** | [**AmazonDspDto**](AmazonDspDto.md)|  | [optional] 

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

