# openapi_client.ConnectorsFacebookPostApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**facebook_post_controller_action_authorization**](ConnectorsFacebookPostApi.md#facebook_post_controller_action_authorization) | **GET** /connectors/facebook_post/actions/authorization | List of authorization objects
[**facebook_post_controller_action_data_label**](ConnectorsFacebookPostApi.md#facebook_post_controller_action_data_label) | **GET** /connectors/facebook_post/actions/dataLabel | List of all data labels
[**facebook_post_controller_action_default_data_label**](ConnectorsFacebookPostApi.md#facebook_post_controller_action_default_data_label) | **GET** /connectors/facebook_post/actions/defaultDataLabel | List of all default data labels
[**facebook_post_controller_action_limit**](ConnectorsFacebookPostApi.md#facebook_post_controller_action_limit) | **GET** /connectors/facebook_post/actions/limit | List of all limits
[**facebook_post_controller_action_load**](ConnectorsFacebookPostApi.md#facebook_post_controller_action_load) | **POST** /connectors/facebook_post/create-source | Create FacebookPost source
[**facebook_post_controller_action_metric**](ConnectorsFacebookPostApi.md#facebook_post_controller_action_metric) | **GET** /connectors/facebook_post/actions/metric | List of all metrics
[**facebook_post_controller_action_page**](ConnectorsFacebookPostApi.md#facebook_post_controller_action_page) | **POST** /connectors/facebook_post/actions/page | List of all Facebook pages
[**facebook_post_controller_action_preview**](ConnectorsFacebookPostApi.md#facebook_post_controller_action_preview) | **POST** /connectors/facebook_post/preview | Preview the data


# **facebook_post_controller_action_authorization**
> List[ActionAuthorizationResponseInner] facebook_post_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsFacebookPostApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.facebook_post_controller_action_authorization()
        print("The response of ConnectorsFacebookPostApi->facebook_post_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookPostApi->facebook_post_controller_action_authorization: %s\n" % e)
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

# **facebook_post_controller_action_data_label**
> List[LabelValueResponseInner] facebook_post_controller_action_data_label()

List of all data labels

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
    api_instance = openapi_client.ConnectorsFacebookPostApi(api_client)

    try:
        # List of all data labels
        api_response = api_instance.facebook_post_controller_action_data_label()
        print("The response of ConnectorsFacebookPostApi->facebook_post_controller_action_data_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookPostApi->facebook_post_controller_action_data_label: %s\n" % e)
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

# **facebook_post_controller_action_default_data_label**
> List[LabelValueResponseInner] facebook_post_controller_action_default_data_label()

List of all default data labels

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
    api_instance = openapi_client.ConnectorsFacebookPostApi(api_client)

    try:
        # List of all default data labels
        api_response = api_instance.facebook_post_controller_action_default_data_label()
        print("The response of ConnectorsFacebookPostApi->facebook_post_controller_action_default_data_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookPostApi->facebook_post_controller_action_default_data_label: %s\n" % e)
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
**200** | List of default data label objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facebook_post_controller_action_limit**
> List[LabelValueResponseInner] facebook_post_controller_action_limit()

List of all limits

List all post limit options

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
    api_instance = openapi_client.ConnectorsFacebookPostApi(api_client)

    try:
        # List of all limits
        api_response = api_instance.facebook_post_controller_action_limit()
        print("The response of ConnectorsFacebookPostApi->facebook_post_controller_action_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookPostApi->facebook_post_controller_action_limit: %s\n" % e)
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
**200** | List of all limits |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facebook_post_controller_action_load**
> Source facebook_post_controller_action_load(facebook_post_connector_form=facebook_post_connector_form)

Create FacebookPost source

### Example


```python
import openapi_client
from openapi_client.models.facebook_post_connector_form import FacebookPostConnectorForm
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
    api_instance = openapi_client.ConnectorsFacebookPostApi(api_client)
    facebook_post_connector_form = openapi_client.FacebookPostConnectorForm() # FacebookPostConnectorForm |  (optional)

    try:
        # Create FacebookPost source
        api_response = api_instance.facebook_post_controller_action_load(facebook_post_connector_form=facebook_post_connector_form)
        print("The response of ConnectorsFacebookPostApi->facebook_post_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookPostApi->facebook_post_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facebook_post_connector_form** | [**FacebookPostConnectorForm**](FacebookPostConnectorForm.md)|  | [optional] 

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

# **facebook_post_controller_action_metric**
> List[FacebookPostControllerActionMetric200ResponseInner] facebook_post_controller_action_metric()

List of all metrics

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
    api_instance = openapi_client.ConnectorsFacebookPostApi(api_client)

    try:
        # List of all metrics
        api_response = api_instance.facebook_post_controller_action_metric()
        print("The response of ConnectorsFacebookPostApi->facebook_post_controller_action_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookPostApi->facebook_post_controller_action_metric: %s\n" % e)
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

# **facebook_post_controller_action_page**
> List[LabelValueResponseInner] facebook_post_controller_action_page(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List of all Facebook pages

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
    api_instance = openapi_client.ConnectorsFacebookPostApi(api_client)
    amazon_ads_controller_action_profile_request_value = {"oAuthId":0} # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List of all Facebook pages
        api_response = api_instance.facebook_post_controller_action_page(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsFacebookPostApi->facebook_post_controller_action_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookPostApi->facebook_post_controller_action_page: %s\n" % e)
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
**200** | List of all Facebook pages |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facebook_post_controller_action_preview**
> SuccessResponse facebook_post_controller_action_preview(facebook_post_connector_form=facebook_post_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.facebook_post_connector_form import FacebookPostConnectorForm
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
    api_instance = openapi_client.ConnectorsFacebookPostApi(api_client)
    facebook_post_connector_form = openapi_client.FacebookPostConnectorForm() # FacebookPostConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.facebook_post_controller_action_preview(facebook_post_connector_form=facebook_post_connector_form)
        print("The response of ConnectorsFacebookPostApi->facebook_post_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookPostApi->facebook_post_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facebook_post_connector_form** | [**FacebookPostConnectorForm**](FacebookPostConnectorForm.md)|  | [optional] 

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

