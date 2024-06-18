# openapi_client.ConnectorsFacebookPageApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**facebook_page_controller_action_authorization**](ConnectorsFacebookPageApi.md#facebook_page_controller_action_authorization) | **GET** /connectors/facebook_page/actions/authorization | List of authorization objects
[**facebook_page_controller_action_data_label**](ConnectorsFacebookPageApi.md#facebook_page_controller_action_data_label) | **GET** /connectors/facebook_page/actions/dataLabel | List all Facebook Page data labels
[**facebook_page_controller_action_date_range**](ConnectorsFacebookPageApi.md#facebook_page_controller_action_date_range) | **GET** /connectors/facebook_page/actions/dateRange | Method for listing date range
[**facebook_page_controller_action_default_data_label**](ConnectorsFacebookPageApi.md#facebook_page_controller_action_default_data_label) | **GET** /connectors/facebook_page/actions/defaultDataLabel | List all default data labels
[**facebook_page_controller_action_default_metric**](ConnectorsFacebookPageApi.md#facebook_page_controller_action_default_metric) | **GET** /connectors/facebook_page/actions/defaultMetric | List all default metrics
[**facebook_page_controller_action_load**](ConnectorsFacebookPageApi.md#facebook_page_controller_action_load) | **POST** /connectors/facebook_page/create-source | Create Facebook Page source
[**facebook_page_controller_action_metric**](ConnectorsFacebookPageApi.md#facebook_page_controller_action_metric) | **GET** /connectors/facebook_page/actions/metric | List Facebook Page metrics
[**facebook_page_controller_action_page**](ConnectorsFacebookPageApi.md#facebook_page_controller_action_page) | **POST** /connectors/facebook_page/actions/page | List all available Facebook Pages
[**facebook_page_controller_action_preview**](ConnectorsFacebookPageApi.md#facebook_page_controller_action_preview) | **POST** /connectors/facebook_page/preview | Preview the data


# **facebook_page_controller_action_authorization**
> List[ActionAuthorizationResponseInner] facebook_page_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsFacebookPageApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.facebook_page_controller_action_authorization()
        print("The response of ConnectorsFacebookPageApi->facebook_page_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookPageApi->facebook_page_controller_action_authorization: %s\n" % e)
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

# **facebook_page_controller_action_data_label**
> List[LabelValueResponseInner] facebook_page_controller_action_data_label()

List all Facebook Page data labels

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
    api_instance = openapi_client.ConnectorsFacebookPageApi(api_client)

    try:
        # List all Facebook Page data labels
        api_response = api_instance.facebook_page_controller_action_data_label()
        print("The response of ConnectorsFacebookPageApi->facebook_page_controller_action_data_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookPageApi->facebook_page_controller_action_data_label: %s\n" % e)
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
**200** | List of data label objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facebook_page_controller_action_date_range**
> List[LabelValueResponseInner] facebook_page_controller_action_date_range()

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
    api_instance = openapi_client.ConnectorsFacebookPageApi(api_client)

    try:
        # Method for listing date range
        api_response = api_instance.facebook_page_controller_action_date_range()
        print("The response of ConnectorsFacebookPageApi->facebook_page_controller_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookPageApi->facebook_page_controller_action_date_range: %s\n" % e)
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
**200** | List of Facebook Page date ranges |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facebook_page_controller_action_default_data_label**
> List[LabelValueResponseInner] facebook_page_controller_action_default_data_label()

List all default data labels

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
    api_instance = openapi_client.ConnectorsFacebookPageApi(api_client)

    try:
        # List all default data labels
        api_response = api_instance.facebook_page_controller_action_default_data_label()
        print("The response of ConnectorsFacebookPageApi->facebook_page_controller_action_default_data_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookPageApi->facebook_page_controller_action_default_data_label: %s\n" % e)
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
**200** | List of default data labels |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facebook_page_controller_action_default_metric**
> List[LabelValueResponseInner] facebook_page_controller_action_default_metric()

List all default metrics

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
    api_instance = openapi_client.ConnectorsFacebookPageApi(api_client)

    try:
        # List all default metrics
        api_response = api_instance.facebook_page_controller_action_default_metric()
        print("The response of ConnectorsFacebookPageApi->facebook_page_controller_action_default_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookPageApi->facebook_page_controller_action_default_metric: %s\n" % e)
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
**200** | List of default metrics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facebook_page_controller_action_load**
> Source facebook_page_controller_action_load(facebook_page_connector_form=facebook_page_connector_form)

Create Facebook Page source

### Example


```python
import openapi_client
from openapi_client.models.facebook_page_connector_form import FacebookPageConnectorForm
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
    api_instance = openapi_client.ConnectorsFacebookPageApi(api_client)
    facebook_page_connector_form = openapi_client.FacebookPageConnectorForm() # FacebookPageConnectorForm |  (optional)

    try:
        # Create Facebook Page source
        api_response = api_instance.facebook_page_controller_action_load(facebook_page_connector_form=facebook_page_connector_form)
        print("The response of ConnectorsFacebookPageApi->facebook_page_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookPageApi->facebook_page_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facebook_page_connector_form** | [**FacebookPageConnectorForm**](FacebookPageConnectorForm.md)|  | [optional] 

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

# **facebook_page_controller_action_metric**
> List[LabelValueResponseInner] facebook_page_controller_action_metric()

List Facebook Page metrics

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
    api_instance = openapi_client.ConnectorsFacebookPageApi(api_client)

    try:
        # List Facebook Page metrics
        api_response = api_instance.facebook_page_controller_action_metric()
        print("The response of ConnectorsFacebookPageApi->facebook_page_controller_action_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookPageApi->facebook_page_controller_action_metric: %s\n" % e)
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
**200** | List of metric objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facebook_page_controller_action_page**
> List[LabelValueResponseInner] facebook_page_controller_action_page(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List all available Facebook Pages

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
    api_instance = openapi_client.ConnectorsFacebookPageApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List all available Facebook Pages
        api_response = api_instance.facebook_page_controller_action_page(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsFacebookPageApi->facebook_page_controller_action_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookPageApi->facebook_page_controller_action_page: %s\n" % e)
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
**200** | List of Facebook pages |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facebook_page_controller_action_preview**
> SuccessResponse facebook_page_controller_action_preview(facebook_page_connector_form=facebook_page_connector_form)

Preview the data

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.facebook_page_connector_form import FacebookPageConnectorForm
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
    api_instance = openapi_client.ConnectorsFacebookPageApi(api_client)
    facebook_page_connector_form = openapi_client.FacebookPageConnectorForm() # FacebookPageConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.facebook_page_controller_action_preview(facebook_page_connector_form=facebook_page_connector_form)
        print("The response of ConnectorsFacebookPageApi->facebook_page_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookPageApi->facebook_page_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facebook_page_connector_form** | [**FacebookPageConnectorForm**](FacebookPageConnectorForm.md)|  | [optional] 

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

