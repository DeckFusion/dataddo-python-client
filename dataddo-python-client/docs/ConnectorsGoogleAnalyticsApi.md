# openapi_client.ConnectorsGoogleAnalyticsApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**google_analytics_controller_action_account**](ConnectorsGoogleAnalyticsApi.md#google_analytics_controller_action_account) | **POST** /connectors/google_analytics/actions/account | List of accounts
[**google_analytics_controller_action_authorization**](ConnectorsGoogleAnalyticsApi.md#google_analytics_controller_action_authorization) | **GET** /connectors/google_analytics/actions/authorization | List of authorization objects
[**google_analytics_controller_action_data_label**](ConnectorsGoogleAnalyticsApi.md#google_analytics_controller_action_data_label) | **GET** /connectors/google_analytics/actions/dataLabel | List of data label objects
[**google_analytics_controller_action_dimension**](ConnectorsGoogleAnalyticsApi.md#google_analytics_controller_action_dimension) | **GET** /connectors/google_analytics/actions/dimension | List of dimension objects
[**google_analytics_controller_action_load**](ConnectorsGoogleAnalyticsApi.md#google_analytics_controller_action_load) | **POST** /connectors/google_analytics/create-source | Create Google Analytics source
[**google_analytics_controller_action_metric**](ConnectorsGoogleAnalyticsApi.md#google_analytics_controller_action_metric) | **GET** /connectors/google_analytics/actions/metric | List of metric objects
[**google_analytics_controller_action_preview**](ConnectorsGoogleAnalyticsApi.md#google_analytics_controller_action_preview) | **POST** /connectors/google_analytics/preview | Preview the data
[**google_analytics_controller_action_property**](ConnectorsGoogleAnalyticsApi.md#google_analytics_controller_action_property) | **POST** /connectors/google_analytics/actions/property | List of properties
[**google_analytics_controller_action_segment**](ConnectorsGoogleAnalyticsApi.md#google_analytics_controller_action_segment) | **POST** /connectors/google_analytics/actions/segment | List of saved segments
[**google_analytics_controller_action_view**](ConnectorsGoogleAnalyticsApi.md#google_analytics_controller_action_view) | **POST** /connectors/google_analytics/actions/view | List of views


# **google_analytics_controller_action_account**
> List[GoogleAnalyticsControllerActionAccount200ResponseInner] google_analytics_controller_action_account(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List of accounts

### Example


```python
import openapi_client
from openapi_client.models.amazon_ads_controller_action_profile_request_value import AmazonAdsControllerActionProfileRequestValue
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
    api_instance = openapi_client.ConnectorsGoogleAnalyticsApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List of accounts
        api_response = api_instance.google_analytics_controller_action_account(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_ads_controller_action_profile_request_value** | [**AmazonAdsControllerActionProfileRequestValue**](AmazonAdsControllerActionProfileRequestValue.md)|  | [optional] 

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
**200** | List of accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_analytics_controller_action_authorization**
> List[ActionAuthorizationResponseInner] google_analytics_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsGoogleAnalyticsApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.google_analytics_controller_action_authorization()
        print("The response of ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_authorization: %s\n" % e)
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

# **google_analytics_controller_action_data_label**
> List[FacebookPostControllerActionMetric200ResponseInner] google_analytics_controller_action_data_label()

List of data label objects

### Example


```python
import openapi_client
from openapi_client.models.facebook_post_controller_action_metric200_response_inner import FacebookPostControllerActionMetric200ResponseInner
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
    api_instance = openapi_client.ConnectorsGoogleAnalyticsApi(api_client)

    try:
        # List of data label objects
        api_response = api_instance.google_analytics_controller_action_data_label()
        print("The response of ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_data_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_data_label: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FacebookPostControllerActionMetric200ResponseInner]**](FacebookPostControllerActionMetric200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of data label objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_analytics_controller_action_dimension**
> List[FacebookPostControllerActionMetric200ResponseInner] google_analytics_controller_action_dimension()

List of dimension objects

### Example


```python
import openapi_client
from openapi_client.models.facebook_post_controller_action_metric200_response_inner import FacebookPostControllerActionMetric200ResponseInner
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
    api_instance = openapi_client.ConnectorsGoogleAnalyticsApi(api_client)

    try:
        # List of dimension objects
        api_response = api_instance.google_analytics_controller_action_dimension()
        print("The response of ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_dimension:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_dimension: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FacebookPostControllerActionMetric200ResponseInner]**](FacebookPostControllerActionMetric200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of dimension objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_analytics_controller_action_load**
> Source google_analytics_controller_action_load(google_analytics_connector_form=google_analytics_connector_form)

Create Google Analytics source

### Example


```python
import openapi_client
from openapi_client.models.google_analytics_connector_form import GoogleAnalyticsConnectorForm
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
    api_instance = openapi_client.ConnectorsGoogleAnalyticsApi(api_client)
    google_analytics_connector_form = openapi_client.GoogleAnalyticsConnectorForm() # GoogleAnalyticsConnectorForm |  (optional)

    try:
        # Create Google Analytics source
        api_response = api_instance.google_analytics_controller_action_load(google_analytics_connector_form=google_analytics_connector_form)
        print("The response of ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_analytics_connector_form** | [**GoogleAnalyticsConnectorForm**](GoogleAnalyticsConnectorForm.md)|  | [optional] 

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

# **google_analytics_controller_action_metric**
> List[FacebookPostControllerActionMetric200ResponseInner] google_analytics_controller_action_metric()

List of metric objects

### Example


```python
import openapi_client
from openapi_client.models.facebook_post_controller_action_metric200_response_inner import FacebookPostControllerActionMetric200ResponseInner
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
    api_instance = openapi_client.ConnectorsGoogleAnalyticsApi(api_client)

    try:
        # List of metric objects
        api_response = api_instance.google_analytics_controller_action_metric()
        print("The response of ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_metric: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FacebookPostControllerActionMetric200ResponseInner]**](FacebookPostControllerActionMetric200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of metric objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_analytics_controller_action_preview**
> SuccessResponse google_analytics_controller_action_preview(google_analytics_connector_form=google_analytics_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.google_analytics_connector_form import GoogleAnalyticsConnectorForm
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
    api_instance = openapi_client.ConnectorsGoogleAnalyticsApi(api_client)
    google_analytics_connector_form = openapi_client.GoogleAnalyticsConnectorForm() # GoogleAnalyticsConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.google_analytics_controller_action_preview(google_analytics_connector_form=google_analytics_connector_form)
        print("The response of ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_analytics_connector_form** | [**GoogleAnalyticsConnectorForm**](GoogleAnalyticsConnectorForm.md)|  | [optional] 

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

# **google_analytics_controller_action_property**
> List[GoogleAnalyticsControllerActionAccount200ResponseInner] google_analytics_controller_action_property(google_analytics4_controller_action_property_request=google_analytics4_controller_action_property_request)

List of properties

### Example


```python
import openapi_client
from openapi_client.models.google_analytics4_controller_action_property_request import GoogleAnalytics4ControllerActionPropertyRequest
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
    api_instance = openapi_client.ConnectorsGoogleAnalyticsApi(api_client)
    google_analytics4_controller_action_property_request = openapi_client.GoogleAnalytics4ControllerActionPropertyRequest() # GoogleAnalytics4ControllerActionPropertyRequest |  (optional)

    try:
        # List of properties
        api_response = api_instance.google_analytics_controller_action_property(google_analytics4_controller_action_property_request=google_analytics4_controller_action_property_request)
        print("The response of ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_analytics4_controller_action_property_request** | [**GoogleAnalytics4ControllerActionPropertyRequest**](GoogleAnalytics4ControllerActionPropertyRequest.md)|  | [optional] 

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
**200** | List of properties |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_analytics_controller_action_segment**
> List[LabelValueResponseInner] google_analytics_controller_action_segment(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List of saved segments

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
    api_instance = openapi_client.ConnectorsGoogleAnalyticsApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List of saved segments
        api_response = api_instance.google_analytics_controller_action_segment(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_segment: %s\n" % e)
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
**200** | List of saved segments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_analytics_controller_action_view**
> List[GoogleAnalyticsControllerActionAccount200ResponseInner] google_analytics_controller_action_view(google_analytics_controller_action_view_request=google_analytics_controller_action_view_request)

List of views

### Example


```python
import openapi_client
from openapi_client.models.google_analytics_controller_action_account200_response_inner import GoogleAnalyticsControllerActionAccount200ResponseInner
from openapi_client.models.google_analytics_controller_action_view_request import GoogleAnalyticsControllerActionViewRequest
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
    api_instance = openapi_client.ConnectorsGoogleAnalyticsApi(api_client)
    google_analytics_controller_action_view_request = openapi_client.GoogleAnalyticsControllerActionViewRequest() # GoogleAnalyticsControllerActionViewRequest |  (optional)

    try:
        # List of views
        api_response = api_instance.google_analytics_controller_action_view(google_analytics_controller_action_view_request=google_analytics_controller_action_view_request)
        print("The response of ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAnalyticsApi->google_analytics_controller_action_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_analytics_controller_action_view_request** | [**GoogleAnalyticsControllerActionViewRequest**](GoogleAnalyticsControllerActionViewRequest.md)|  | [optional] 

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
**200** | List of views |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

