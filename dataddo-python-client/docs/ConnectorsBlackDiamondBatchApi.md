# openapi_client.ConnectorsBlackDiamondBatchApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**black_diamond_batch_controller_action_authorization**](ConnectorsBlackDiamondBatchApi.md#black_diamond_batch_controller_action_authorization) | **GET** /connectors/black_diamond_batch/actions/authorization | List of authorization objects
[**black_diamond_batch_controller_action_load**](ConnectorsBlackDiamondBatchApi.md#black_diamond_batch_controller_action_load) | **POST** /connectors/black_diamond_batch/create-source | Create Black Diamond Batch source
[**black_diamond_batch_controller_action_metrics**](ConnectorsBlackDiamondBatchApi.md#black_diamond_batch_controller_action_metrics) | **POST** /connectors/blackDiamondBatch/actions/metrics | List Black Diamond metrics
[**black_diamond_batch_controller_action_object**](ConnectorsBlackDiamondBatchApi.md#black_diamond_batch_controller_action_object) | **POST** /connectors/blackDiamondBatch/actions/object | List of objects
[**black_diamond_batch_controller_action_preview**](ConnectorsBlackDiamondBatchApi.md#black_diamond_batch_controller_action_preview) | **POST** /connectors/black_diamond_batch/preview | Preview the data


# **black_diamond_batch_controller_action_authorization**
> List[ActionAuthorizationResponseInner] black_diamond_batch_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsBlackDiamondBatchApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.black_diamond_batch_controller_action_authorization()
        print("The response of ConnectorsBlackDiamondBatchApi->black_diamond_batch_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsBlackDiamondBatchApi->black_diamond_batch_controller_action_authorization: %s\n" % e)
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

# **black_diamond_batch_controller_action_load**
> Source black_diamond_batch_controller_action_load(black_diamond_batch_connector_form=black_diamond_batch_connector_form)

Create Black Diamond Batch source

### Example


```python
import openapi_client
from openapi_client.models.black_diamond_batch_connector_form import BlackDiamondBatchConnectorForm
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
    api_instance = openapi_client.ConnectorsBlackDiamondBatchApi(api_client)
    black_diamond_batch_connector_form = openapi_client.BlackDiamondBatchConnectorForm() # BlackDiamondBatchConnectorForm |  (optional)

    try:
        # Create Black Diamond Batch source
        api_response = api_instance.black_diamond_batch_controller_action_load(black_diamond_batch_connector_form=black_diamond_batch_connector_form)
        print("The response of ConnectorsBlackDiamondBatchApi->black_diamond_batch_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsBlackDiamondBatchApi->black_diamond_batch_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **black_diamond_batch_connector_form** | [**BlackDiamondBatchConnectorForm**](BlackDiamondBatchConnectorForm.md)|  | [optional] 

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

# **black_diamond_batch_controller_action_metrics**
> black_diamond_batch_controller_action_metrics(request_body=request_body)

List Black Diamond metrics

### Example


```python
import openapi_client
from openapi_client.models.black_diamond_batch_controller_action_metrics_request_value import BlackDiamondBatchControllerActionMetricsRequestValue
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
    api_instance = openapi_client.ConnectorsBlackDiamondBatchApi(api_client)
    request_body = {'key': openapi_client.BlackDiamondBatchControllerActionMetricsRequestValue()} # Dict[str, BlackDiamondBatchControllerActionMetricsRequestValue] |  (optional)

    try:
        # List Black Diamond metrics
        api_instance.black_diamond_batch_controller_action_metrics(request_body=request_body)
    except Exception as e:
        print("Exception when calling ConnectorsBlackDiamondBatchApi->black_diamond_batch_controller_action_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, BlackDiamondBatchControllerActionMetricsRequestValue]**](BlackDiamondBatchControllerActionMetricsRequestValue.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Black Diamond metrics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **black_diamond_batch_controller_action_object**
> List[LabelValueResponseInner] black_diamond_batch_controller_action_object(black_diamond_batch_controller_action_object_request=black_diamond_batch_controller_action_object_request)

List of objects

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
    api_instance = openapi_client.ConnectorsBlackDiamondBatchApi(api_client)
    black_diamond_batch_controller_action_object_request = openapi_client.BlackDiamondBatchControllerActionObjectRequest() # BlackDiamondBatchControllerActionObjectRequest |  (optional)

    try:
        # List of objects
        api_response = api_instance.black_diamond_batch_controller_action_object(black_diamond_batch_controller_action_object_request=black_diamond_batch_controller_action_object_request)
        print("The response of ConnectorsBlackDiamondBatchApi->black_diamond_batch_controller_action_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsBlackDiamondBatchApi->black_diamond_batch_controller_action_object: %s\n" % e)
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
**200** | List of all available objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **black_diamond_batch_controller_action_preview**
> SuccessResponse black_diamond_batch_controller_action_preview(black_diamond_batch_connector_form=black_diamond_batch_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.black_diamond_batch_connector_form import BlackDiamondBatchConnectorForm
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
    api_instance = openapi_client.ConnectorsBlackDiamondBatchApi(api_client)
    black_diamond_batch_connector_form = openapi_client.BlackDiamondBatchConnectorForm() # BlackDiamondBatchConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.black_diamond_batch_controller_action_preview(black_diamond_batch_connector_form=black_diamond_batch_connector_form)
        print("The response of ConnectorsBlackDiamondBatchApi->black_diamond_batch_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsBlackDiamondBatchApi->black_diamond_batch_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **black_diamond_batch_connector_form** | [**BlackDiamondBatchConnectorForm**](BlackDiamondBatchConnectorForm.md)|  | [optional] 

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

