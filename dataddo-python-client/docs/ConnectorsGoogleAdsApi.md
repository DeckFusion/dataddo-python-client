# openapi_client.ConnectorsGoogleAdsApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**google_ads_controller_action_attribute**](ConnectorsGoogleAdsApi.md#google_ads_controller_action_attribute) | **POST** /connectors/google_ads/actions/attribute | List of all attributes
[**google_ads_controller_action_authorization**](ConnectorsGoogleAdsApi.md#google_ads_controller_action_authorization) | **GET** /connectors/google_ads/actions/authorization | List of authorization objects
[**google_ads_controller_action_customer**](ConnectorsGoogleAdsApi.md#google_ads_controller_action_customer) | **POST** /connectors/google_ads/actions/customer | List of customers
[**google_ads_controller_action_customer_client**](ConnectorsGoogleAdsApi.md#google_ads_controller_action_customer_client) | **POST** /connectors/google_ads/actions/customerClient | List of clients
[**google_ads_controller_action_load**](ConnectorsGoogleAdsApi.md#google_ads_controller_action_load) | **POST** /connectors/google_ads/create-source | Create GoogleAds source
[**google_ads_controller_action_metric**](ConnectorsGoogleAdsApi.md#google_ads_controller_action_metric) | **POST** /connectors/google_ads/actions/metric | List of metric objects
[**google_ads_controller_action_preview**](ConnectorsGoogleAdsApi.md#google_ads_controller_action_preview) | **POST** /connectors/google_ads/preview | Preview the data
[**google_ads_controller_action_report_type**](ConnectorsGoogleAdsApi.md#google_ads_controller_action_report_type) | **GET** /connectors/google_ads/actions/reportType | List of all report types
[**google_ads_controller_action_segment**](ConnectorsGoogleAdsApi.md#google_ads_controller_action_segment) | **POST** /connectors/google_ads/actions/segment | List of all segments


# **google_ads_controller_action_attribute**
> List[LabelValueResponseInner] google_ads_controller_action_attribute(google_ads_controller_action_metric_request=google_ads_controller_action_metric_request)

List of all attributes

### Example


```python
import openapi_client
from openapi_client.models.google_ads_controller_action_metric_request import GoogleAdsControllerActionMetricRequest
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
    api_instance = openapi_client.ConnectorsGoogleAdsApi(api_client)
    google_ads_controller_action_metric_request = openapi_client.GoogleAdsControllerActionMetricRequest() # GoogleAdsControllerActionMetricRequest |  (optional)

    try:
        # List of all attributes
        api_response = api_instance.google_ads_controller_action_attribute(google_ads_controller_action_metric_request=google_ads_controller_action_metric_request)
        print("The response of ConnectorsGoogleAdsApi->google_ads_controller_action_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAdsApi->google_ads_controller_action_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_ads_controller_action_metric_request** | [**GoogleAdsControllerActionMetricRequest**](GoogleAdsControllerActionMetricRequest.md)|  | [optional] 

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
**200** | List of attribute objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_ads_controller_action_authorization**
> List[ActionAuthorizationResponseInner] google_ads_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsGoogleAdsApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.google_ads_controller_action_authorization()
        print("The response of ConnectorsGoogleAdsApi->google_ads_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAdsApi->google_ads_controller_action_authorization: %s\n" % e)
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

# **google_ads_controller_action_customer**
> List[LabelValueResponseInner] google_ads_controller_action_customer(black_diamond_batch_controller_action_object_request=black_diamond_batch_controller_action_object_request)

List of customers

### Example


```python
import openapi_client
from openapi_client.models.black_diamond_batch_controller_action_object_request import BlackDiamondBatchControllerActionObjectRequest
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
    api_instance = openapi_client.ConnectorsGoogleAdsApi(api_client)
    black_diamond_batch_controller_action_object_request = openapi_client.BlackDiamondBatchControllerActionObjectRequest() # BlackDiamondBatchControllerActionObjectRequest |  (optional)

    try:
        # List of customers
        api_response = api_instance.google_ads_controller_action_customer(black_diamond_batch_controller_action_object_request=black_diamond_batch_controller_action_object_request)
        print("The response of ConnectorsGoogleAdsApi->google_ads_controller_action_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAdsApi->google_ads_controller_action_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **black_diamond_batch_controller_action_object_request** | [**BlackDiamondBatchControllerActionObjectRequest**](BlackDiamondBatchControllerActionObjectRequest.md)|  | [optional] 

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
**200** | List of customers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_ads_controller_action_customer_client**
> List[LabelValueResponseInner] google_ads_controller_action_customer_client(google_ads_controller_action_customer_client_request=google_ads_controller_action_customer_client_request)

List of clients

### Example


```python
import openapi_client
from openapi_client.models.google_ads_controller_action_customer_client_request import GoogleAdsControllerActionCustomerClientRequest
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
    api_instance = openapi_client.ConnectorsGoogleAdsApi(api_client)
    google_ads_controller_action_customer_client_request = openapi_client.GoogleAdsControllerActionCustomerClientRequest() # GoogleAdsControllerActionCustomerClientRequest |  (optional)

    try:
        # List of clients
        api_response = api_instance.google_ads_controller_action_customer_client(google_ads_controller_action_customer_client_request=google_ads_controller_action_customer_client_request)
        print("The response of ConnectorsGoogleAdsApi->google_ads_controller_action_customer_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAdsApi->google_ads_controller_action_customer_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_ads_controller_action_customer_client_request** | [**GoogleAdsControllerActionCustomerClientRequest**](GoogleAdsControllerActionCustomerClientRequest.md)|  | [optional] 

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
**200** | List of clients |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_ads_controller_action_load**
> Source google_ads_controller_action_load(google_ads_connector_form=google_ads_connector_form)

Create GoogleAds source

### Example


```python
import openapi_client
from openapi_client.models.google_ads_connector_form import GoogleAdsConnectorForm
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
    api_instance = openapi_client.ConnectorsGoogleAdsApi(api_client)
    google_ads_connector_form = openapi_client.GoogleAdsConnectorForm() # GoogleAdsConnectorForm |  (optional)

    try:
        # Create GoogleAds source
        api_response = api_instance.google_ads_controller_action_load(google_ads_connector_form=google_ads_connector_form)
        print("The response of ConnectorsGoogleAdsApi->google_ads_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAdsApi->google_ads_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_ads_connector_form** | [**GoogleAdsConnectorForm**](GoogleAdsConnectorForm.md)|  | [optional] 

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

# **google_ads_controller_action_metric**
> List[LabelValueResponseInner] google_ads_controller_action_metric(google_ads_controller_action_metric_request=google_ads_controller_action_metric_request)

List of metric objects

### Example


```python
import openapi_client
from openapi_client.models.google_ads_controller_action_metric_request import GoogleAdsControllerActionMetricRequest
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
    api_instance = openapi_client.ConnectorsGoogleAdsApi(api_client)
    google_ads_controller_action_metric_request = openapi_client.GoogleAdsControllerActionMetricRequest() # GoogleAdsControllerActionMetricRequest |  (optional)

    try:
        # List of metric objects
        api_response = api_instance.google_ads_controller_action_metric(google_ads_controller_action_metric_request=google_ads_controller_action_metric_request)
        print("The response of ConnectorsGoogleAdsApi->google_ads_controller_action_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAdsApi->google_ads_controller_action_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_ads_controller_action_metric_request** | [**GoogleAdsControllerActionMetricRequest**](GoogleAdsControllerActionMetricRequest.md)|  | [optional] 

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
**200** | List of metric objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_ads_controller_action_preview**
> SuccessResponse google_ads_controller_action_preview(google_ads_connector_form=google_ads_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.google_ads_connector_form import GoogleAdsConnectorForm
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
    api_instance = openapi_client.ConnectorsGoogleAdsApi(api_client)
    google_ads_connector_form = openapi_client.GoogleAdsConnectorForm() # GoogleAdsConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.google_ads_controller_action_preview(google_ads_connector_form=google_ads_connector_form)
        print("The response of ConnectorsGoogleAdsApi->google_ads_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAdsApi->google_ads_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_ads_connector_form** | [**GoogleAdsConnectorForm**](GoogleAdsConnectorForm.md)|  | [optional] 

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

# **google_ads_controller_action_report_type**
> List[LabelValueResponseInner] google_ads_controller_action_report_type()

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
    api_instance = openapi_client.ConnectorsGoogleAdsApi(api_client)

    try:
        # List of all report types
        api_response = api_instance.google_ads_controller_action_report_type()
        print("The response of ConnectorsGoogleAdsApi->google_ads_controller_action_report_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAdsApi->google_ads_controller_action_report_type: %s\n" % e)
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

# **google_ads_controller_action_segment**
> List[LabelValueResponseInner] google_ads_controller_action_segment(google_ads_controller_action_metric_request=google_ads_controller_action_metric_request)

List of all segments

### Example


```python
import openapi_client
from openapi_client.models.google_ads_controller_action_metric_request import GoogleAdsControllerActionMetricRequest
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
    api_instance = openapi_client.ConnectorsGoogleAdsApi(api_client)
    google_ads_controller_action_metric_request = openapi_client.GoogleAdsControllerActionMetricRequest() # GoogleAdsControllerActionMetricRequest |  (optional)

    try:
        # List of all segments
        api_response = api_instance.google_ads_controller_action_segment(google_ads_controller_action_metric_request=google_ads_controller_action_metric_request)
        print("The response of ConnectorsGoogleAdsApi->google_ads_controller_action_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAdsApi->google_ads_controller_action_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_ads_controller_action_metric_request** | [**GoogleAdsControllerActionMetricRequest**](GoogleAdsControllerActionMetricRequest.md)|  | [optional] 

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
**200** | List of all segments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

