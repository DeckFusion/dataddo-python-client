# openapi_client.ConnectorsGoogleAnalytics4Api

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**google_analytics4_controller_action_account**](ConnectorsGoogleAnalytics4Api.md#google_analytics4_controller_action_account) | **POST** /connectors/google_analytics4/actions/account | List of accounts
[**google_analytics4_controller_action_authorization**](ConnectorsGoogleAnalytics4Api.md#google_analytics4_controller_action_authorization) | **GET** /connectors/google_analytics4/actions/authorization | List of authorization objects
[**google_analytics4_controller_action_dimension**](ConnectorsGoogleAnalytics4Api.md#google_analytics4_controller_action_dimension) | **POST** /connectors/google_analytics4/actions/dimension | Get Google Analytics dimensions
[**google_analytics4_controller_action_load**](ConnectorsGoogleAnalytics4Api.md#google_analytics4_controller_action_load) | **POST** /connectors/google_analytics4/create-source | Create Google Analytics 4 source
[**google_analytics4_controller_action_metric**](ConnectorsGoogleAnalytics4Api.md#google_analytics4_controller_action_metric) | **POST** /connectors/google_analytics4/actions/metric | List of metrics
[**google_analytics4_controller_action_preview**](ConnectorsGoogleAnalytics4Api.md#google_analytics4_controller_action_preview) | **POST** /connectors/google_analytics4/preview | Preview the data
[**google_analytics4_controller_action_property**](ConnectorsGoogleAnalytics4Api.md#google_analytics4_controller_action_property) | **POST** /connectors/google_analytics4/actions/property | List of properties


# **google_analytics4_controller_action_account**
> List[LabelValueResponseInner] google_analytics4_controller_action_account(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List of accounts

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
    api_instance = openapi_client.ConnectorsGoogleAnalytics4Api(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List of accounts
        api_response = api_instance.google_analytics4_controller_action_account(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsGoogleAnalytics4Api->google_analytics4_controller_action_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAnalytics4Api->google_analytics4_controller_action_account: %s\n" % e)
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
**200** | List of accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_analytics4_controller_action_authorization**
> List[ActionAuthorizationResponseInner] google_analytics4_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsGoogleAnalytics4Api(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.google_analytics4_controller_action_authorization()
        print("The response of ConnectorsGoogleAnalytics4Api->google_analytics4_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAnalytics4Api->google_analytics4_controller_action_authorization: %s\n" % e)
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

# **google_analytics4_controller_action_dimension**
> List[LabelValueResponseInner] google_analytics4_controller_action_dimension(google_analytics4_controller_action_dimension_request=google_analytics4_controller_action_dimension_request)

Get Google Analytics dimensions

### Example


```python
import openapi_client
from openapi_client.models.google_analytics4_controller_action_dimension_request import GoogleAnalytics4ControllerActionDimensionRequest
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
    api_instance = openapi_client.ConnectorsGoogleAnalytics4Api(api_client)
    google_analytics4_controller_action_dimension_request = openapi_client.GoogleAnalytics4ControllerActionDimensionRequest() # GoogleAnalytics4ControllerActionDimensionRequest |  (optional)

    try:
        # Get Google Analytics dimensions
        api_response = api_instance.google_analytics4_controller_action_dimension(google_analytics4_controller_action_dimension_request=google_analytics4_controller_action_dimension_request)
        print("The response of ConnectorsGoogleAnalytics4Api->google_analytics4_controller_action_dimension:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAnalytics4Api->google_analytics4_controller_action_dimension: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_analytics4_controller_action_dimension_request** | [**GoogleAnalytics4ControllerActionDimensionRequest**](GoogleAnalytics4ControllerActionDimensionRequest.md)|  | [optional] 

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
**200** | List of dimensions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_analytics4_controller_action_load**
> Source google_analytics4_controller_action_load(google_analytics4_connector_form=google_analytics4_connector_form)

Create Google Analytics 4 source

### Example


```python
import openapi_client
from openapi_client.models.google_analytics4_connector_form import GoogleAnalytics4ConnectorForm
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
    api_instance = openapi_client.ConnectorsGoogleAnalytics4Api(api_client)
    google_analytics4_connector_form = openapi_client.GoogleAnalytics4ConnectorForm() # GoogleAnalytics4ConnectorForm |  (optional)

    try:
        # Create Google Analytics 4 source
        api_response = api_instance.google_analytics4_controller_action_load(google_analytics4_connector_form=google_analytics4_connector_form)
        print("The response of ConnectorsGoogleAnalytics4Api->google_analytics4_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAnalytics4Api->google_analytics4_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_analytics4_connector_form** | [**GoogleAnalytics4ConnectorForm**](GoogleAnalytics4ConnectorForm.md)|  | [optional] 

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

# **google_analytics4_controller_action_metric**
> List[LabelValueResponseInner] google_analytics4_controller_action_metric(request_body=request_body)

List of metrics

### Example


```python
import openapi_client
from openapi_client.models.google_analytics4_controller_action_metric_request_value import GoogleAnalytics4ControllerActionMetricRequestValue
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
    api_instance = openapi_client.ConnectorsGoogleAnalytics4Api(api_client)
    request_body = {'key': openapi_client.GoogleAnalytics4ControllerActionMetricRequestValue()} # Dict[str, GoogleAnalytics4ControllerActionMetricRequestValue] |  (optional)

    try:
        # List of metrics
        api_response = api_instance.google_analytics4_controller_action_metric(request_body=request_body)
        print("The response of ConnectorsGoogleAnalytics4Api->google_analytics4_controller_action_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAnalytics4Api->google_analytics4_controller_action_metric: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, GoogleAnalytics4ControllerActionMetricRequestValue]**](GoogleAnalytics4ControllerActionMetricRequestValue.md)|  | [optional] 

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
**200** | List of metrics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_analytics4_controller_action_preview**
> SuccessResponse google_analytics4_controller_action_preview(google_analytics4_connector_form=google_analytics4_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.google_analytics4_connector_form import GoogleAnalytics4ConnectorForm
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
    api_instance = openapi_client.ConnectorsGoogleAnalytics4Api(api_client)
    google_analytics4_connector_form = openapi_client.GoogleAnalytics4ConnectorForm() # GoogleAnalytics4ConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.google_analytics4_controller_action_preview(google_analytics4_connector_form=google_analytics4_connector_form)
        print("The response of ConnectorsGoogleAnalytics4Api->google_analytics4_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAnalytics4Api->google_analytics4_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_analytics4_connector_form** | [**GoogleAnalytics4ConnectorForm**](GoogleAnalytics4ConnectorForm.md)|  | [optional] 

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

# **google_analytics4_controller_action_property**
> List[LabelValueResponseInner] google_analytics4_controller_action_property(google_analytics4_controller_action_property_request=google_analytics4_controller_action_property_request)

List of properties

### Example


```python
import openapi_client
from openapi_client.models.google_analytics4_controller_action_property_request import GoogleAnalytics4ControllerActionPropertyRequest
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
    api_instance = openapi_client.ConnectorsGoogleAnalytics4Api(api_client)
    google_analytics4_controller_action_property_request = openapi_client.GoogleAnalytics4ControllerActionPropertyRequest() # GoogleAnalytics4ControllerActionPropertyRequest |  (optional)

    try:
        # List of properties
        api_response = api_instance.google_analytics4_controller_action_property(google_analytics4_controller_action_property_request=google_analytics4_controller_action_property_request)
        print("The response of ConnectorsGoogleAnalytics4Api->google_analytics4_controller_action_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleAnalytics4Api->google_analytics4_controller_action_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_analytics4_controller_action_property_request** | [**GoogleAnalytics4ControllerActionPropertyRequest**](GoogleAnalytics4ControllerActionPropertyRequest.md)|  | [optional] 

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
**200** | List of properties |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

