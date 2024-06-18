# openapi_client.ConnectorsTikTokApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tik_tok_controller_action_advertiser**](ConnectorsTikTokApi.md#tik_tok_controller_action_advertiser) | **POST** /connectors/tik_tok/actions/advertiser | List of advertisers
[**tik_tok_controller_action_audience_dimension**](ConnectorsTikTokApi.md#tik_tok_controller_action_audience_dimension) | **POST** /connectors/tik_tok/actions/audienceDimension | List of all audience dimensions
[**tik_tok_controller_action_authorization**](ConnectorsTikTokApi.md#tik_tok_controller_action_authorization) | **GET** /connectors/tik_tok/actions/authorization | List of authorization objects
[**tik_tok_controller_action_data_label**](ConnectorsTikTokApi.md#tik_tok_controller_action_data_label) | **POST** /connectors/tik_tok/actions/dataLabel | List all data labels
[**tik_tok_controller_action_data_level**](ConnectorsTikTokApi.md#tik_tok_controller_action_data_level) | **POST** /connectors/tik_tok/actions/dataLevel | List of data levels
[**tik_tok_controller_action_date_range**](ConnectorsTikTokApi.md#tik_tok_controller_action_date_range) | **GET** /connectors/tik_tok/actions/dateRange | Method for listing date range
[**tik_tok_controller_action_id_dimension**](ConnectorsTikTokApi.md#tik_tok_controller_action_id_dimension) | **POST** /connectors/tik_tok/actions/idDimension | List of all ID dimensions
[**tik_tok_controller_action_load**](ConnectorsTikTokApi.md#tik_tok_controller_action_load) | **POST** /connectors/tik_tok/create-source | Create TikTok source
[**tik_tok_controller_action_metric**](ConnectorsTikTokApi.md#tik_tok_controller_action_metric) | **POST** /connectors/tik_tok/actions/metric | List all metrics
[**tik_tok_controller_action_preview**](ConnectorsTikTokApi.md#tik_tok_controller_action_preview) | **POST** /connectors/tik_tok/preview | Preview the data
[**tik_tok_controller_action_report_type**](ConnectorsTikTokApi.md#tik_tok_controller_action_report_type) | **GET** /connectors/tik_tok/actions/reportType | List of report types
[**tik_tok_controller_action_time_dimension**](ConnectorsTikTokApi.md#tik_tok_controller_action_time_dimension) | **POST** /connectors/tik_tok/actions/timeDimension | List of all time dimensions


# **tik_tok_controller_action_advertiser**
> List[LabelValueResponseInner] tik_tok_controller_action_advertiser(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List of advertisers

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
    api_instance = openapi_client.ConnectorsTikTokApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List of advertisers
        api_response = api_instance.tik_tok_controller_action_advertiser(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsTikTokApi->tik_tok_controller_action_advertiser:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTikTokApi->tik_tok_controller_action_advertiser: %s\n" % e)
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
**200** | List of advertisers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tik_tok_controller_action_audience_dimension**
> List[LabelValueResponseInner] tik_tok_controller_action_audience_dimension(tik_tok_controller_action_audience_dimension_request=tik_tok_controller_action_audience_dimension_request)

List of all audience dimensions

List all Audience dimensionss

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.tik_tok_controller_action_audience_dimension_request import TikTokControllerActionAudienceDimensionRequest
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
    api_instance = openapi_client.ConnectorsTikTokApi(api_client)
    tik_tok_controller_action_audience_dimension_request = openapi_client.TikTokControllerActionAudienceDimensionRequest() # TikTokControllerActionAudienceDimensionRequest |  (optional)

    try:
        # List of all audience dimensions
        api_response = api_instance.tik_tok_controller_action_audience_dimension(tik_tok_controller_action_audience_dimension_request=tik_tok_controller_action_audience_dimension_request)
        print("The response of ConnectorsTikTokApi->tik_tok_controller_action_audience_dimension:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTikTokApi->tik_tok_controller_action_audience_dimension: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tik_tok_controller_action_audience_dimension_request** | [**TikTokControllerActionAudienceDimensionRequest**](TikTokControllerActionAudienceDimensionRequest.md)|  | [optional] 

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
**200** | List of all audience dimensions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tik_tok_controller_action_authorization**
> List[ActionAuthorizationResponseInner] tik_tok_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsTikTokApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.tik_tok_controller_action_authorization()
        print("The response of ConnectorsTikTokApi->tik_tok_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTikTokApi->tik_tok_controller_action_authorization: %s\n" % e)
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

# **tik_tok_controller_action_data_label**
> List[LabelValueResponseInner] tik_tok_controller_action_data_label(tik_tok_controller_action_data_label_request=tik_tok_controller_action_data_label_request)

List all data labels

Data Label. Dimensions + labels ...

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.tik_tok_controller_action_data_label_request import TikTokControllerActionDataLabelRequest
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
    api_instance = openapi_client.ConnectorsTikTokApi(api_client)
    tik_tok_controller_action_data_label_request = openapi_client.TikTokControllerActionDataLabelRequest() # TikTokControllerActionDataLabelRequest |  (optional)

    try:
        # List all data labels
        api_response = api_instance.tik_tok_controller_action_data_label(tik_tok_controller_action_data_label_request=tik_tok_controller_action_data_label_request)
        print("The response of ConnectorsTikTokApi->tik_tok_controller_action_data_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTikTokApi->tik_tok_controller_action_data_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tik_tok_controller_action_data_label_request** | [**TikTokControllerActionDataLabelRequest**](TikTokControllerActionDataLabelRequest.md)|  | [optional] 

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
**200** | List data labels |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tik_tok_controller_action_data_level**
> List[LabelValueResponseInner] tik_tok_controller_action_data_level(tik_tok_controller_action_data_level_request=tik_tok_controller_action_data_level_request)

List of data levels

List all Data Levels

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.tik_tok_controller_action_data_level_request import TikTokControllerActionDataLevelRequest
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
    api_instance = openapi_client.ConnectorsTikTokApi(api_client)
    tik_tok_controller_action_data_level_request = openapi_client.TikTokControllerActionDataLevelRequest() # TikTokControllerActionDataLevelRequest |  (optional)

    try:
        # List of data levels
        api_response = api_instance.tik_tok_controller_action_data_level(tik_tok_controller_action_data_level_request=tik_tok_controller_action_data_level_request)
        print("The response of ConnectorsTikTokApi->tik_tok_controller_action_data_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTikTokApi->tik_tok_controller_action_data_level: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tik_tok_controller_action_data_level_request** | [**TikTokControllerActionDataLevelRequest**](TikTokControllerActionDataLevelRequest.md)|  | [optional] 

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
**200** | List of data levels |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tik_tok_controller_action_date_range**
> List[LabelValueResponseInner] tik_tok_controller_action_date_range()

Method for listing date range

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
    api_instance = openapi_client.ConnectorsTikTokApi(api_client)

    try:
        # Method for listing date range
        api_response = api_instance.tik_tok_controller_action_date_range()
        print("The response of ConnectorsTikTokApi->tik_tok_controller_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTikTokApi->tik_tok_controller_action_date_range: %s\n" % e)
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
**200** | List of TikTok date ranges |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tik_tok_controller_action_id_dimension**
> List[LabelValueResponseInner] tik_tok_controller_action_id_dimension(tik_tok_controller_action_id_dimension_request=tik_tok_controller_action_id_dimension_request)

List of all ID dimensions

List all ID dimensions

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.tik_tok_controller_action_id_dimension_request import TikTokControllerActionIdDimensionRequest
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
    api_instance = openapi_client.ConnectorsTikTokApi(api_client)
    tik_tok_controller_action_id_dimension_request = openapi_client.TikTokControllerActionIdDimensionRequest() # TikTokControllerActionIdDimensionRequest |  (optional)

    try:
        # List of all ID dimensions
        api_response = api_instance.tik_tok_controller_action_id_dimension(tik_tok_controller_action_id_dimension_request=tik_tok_controller_action_id_dimension_request)
        print("The response of ConnectorsTikTokApi->tik_tok_controller_action_id_dimension:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTikTokApi->tik_tok_controller_action_id_dimension: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tik_tok_controller_action_id_dimension_request** | [**TikTokControllerActionIdDimensionRequest**](TikTokControllerActionIdDimensionRequest.md)|  | [optional] 

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
**200** | List of all ID dimensions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tik_tok_controller_action_load**
> Source tik_tok_controller_action_load(tik_tok_connector_form=tik_tok_connector_form)

Create TikTok source

### Example


```python
import openapi_client
from openapi_client.models.source import Source
from openapi_client.models.tik_tok_connector_form import TikTokConnectorForm
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
    api_instance = openapi_client.ConnectorsTikTokApi(api_client)
    tik_tok_connector_form = openapi_client.TikTokConnectorForm() # TikTokConnectorForm |  (optional)

    try:
        # Create TikTok source
        api_response = api_instance.tik_tok_controller_action_load(tik_tok_connector_form=tik_tok_connector_form)
        print("The response of ConnectorsTikTokApi->tik_tok_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTikTokApi->tik_tok_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tik_tok_connector_form** | [**TikTokConnectorForm**](TikTokConnectorForm.md)|  | [optional] 

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
**200** | Create TikTok source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tik_tok_controller_action_metric**
> List[LabelValueResponseInner] tik_tok_controller_action_metric(tik_tok_controller_action_data_level_request=tik_tok_controller_action_data_level_request)

List all metrics

List all metrics

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.tik_tok_controller_action_data_level_request import TikTokControllerActionDataLevelRequest
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
    api_instance = openapi_client.ConnectorsTikTokApi(api_client)
    tik_tok_controller_action_data_level_request = openapi_client.TikTokControllerActionDataLevelRequest() # TikTokControllerActionDataLevelRequest |  (optional)

    try:
        # List all metrics
        api_response = api_instance.tik_tok_controller_action_metric(tik_tok_controller_action_data_level_request=tik_tok_controller_action_data_level_request)
        print("The response of ConnectorsTikTokApi->tik_tok_controller_action_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTikTokApi->tik_tok_controller_action_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tik_tok_controller_action_data_level_request** | [**TikTokControllerActionDataLevelRequest**](TikTokControllerActionDataLevelRequest.md)|  | [optional] 

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
**200** | List metrics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tik_tok_controller_action_preview**
> SuccessResponse tik_tok_controller_action_preview(tik_tok_connector_form=tik_tok_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.success_response import SuccessResponse
from openapi_client.models.tik_tok_connector_form import TikTokConnectorForm
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
    api_instance = openapi_client.ConnectorsTikTokApi(api_client)
    tik_tok_connector_form = openapi_client.TikTokConnectorForm() # TikTokConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.tik_tok_controller_action_preview(tik_tok_connector_form=tik_tok_connector_form)
        print("The response of ConnectorsTikTokApi->tik_tok_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTikTokApi->tik_tok_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tik_tok_connector_form** | [**TikTokConnectorForm**](TikTokConnectorForm.md)|  | [optional] 

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

# **tik_tok_controller_action_report_type**
> List[LabelValueResponseInner] tik_tok_controller_action_report_type()

List of report types

Reporting Type. Basic, Audience ...

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
    api_instance = openapi_client.ConnectorsTikTokApi(api_client)

    try:
        # List of report types
        api_response = api_instance.tik_tok_controller_action_report_type()
        print("The response of ConnectorsTikTokApi->tik_tok_controller_action_report_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTikTokApi->tik_tok_controller_action_report_type: %s\n" % e)
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

# **tik_tok_controller_action_time_dimension**
> List[LabelValueResponseInner] tik_tok_controller_action_time_dimension(tik_tok_controller_action_id_dimension_request=tik_tok_controller_action_id_dimension_request)

List of all time dimensions

List all Time dimensions

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.tik_tok_controller_action_id_dimension_request import TikTokControllerActionIdDimensionRequest
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
    api_instance = openapi_client.ConnectorsTikTokApi(api_client)
    tik_tok_controller_action_id_dimension_request = openapi_client.TikTokControllerActionIdDimensionRequest() # TikTokControllerActionIdDimensionRequest |  (optional)

    try:
        # List of all time dimensions
        api_response = api_instance.tik_tok_controller_action_time_dimension(tik_tok_controller_action_id_dimension_request=tik_tok_controller_action_id_dimension_request)
        print("The response of ConnectorsTikTokApi->tik_tok_controller_action_time_dimension:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTikTokApi->tik_tok_controller_action_time_dimension: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tik_tok_controller_action_id_dimension_request** | [**TikTokControllerActionIdDimensionRequest**](TikTokControllerActionIdDimensionRequest.md)|  | [optional] 

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
**200** | List of all time dimensions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

