# openapi_client.FlowApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**flow_controller_api_debug**](FlowApi.md#flow_controller_api_debug) | **GET** /flows/{id}/api/debug | 
[**flow_controller_api_detail**](FlowApi.md#flow_controller_api_detail) | **GET** /flows/{id}/api | 
[**flow_controller_api_log**](FlowApi.md#flow_controller_api_log) | **GET** /flows/{id}/api/log | 
[**flow_controller_clone**](FlowApi.md#flow_controller_clone) | **GET** /flows/{id}/clone | 
[**flow_controller_create_flow**](FlowApi.md#flow_controller_create_flow) | **POST** /flows | 
[**flow_controller_delete**](FlowApi.md#flow_controller_delete) | **DELETE** /flows/{id} | 
[**flow_controller_delete_write_action_schedule**](FlowApi.md#flow_controller_delete_write_action_schedule) | **DELETE** /flows/{id}/write/schedule | 
[**flow_controller_detail**](FlowApi.md#flow_controller_detail) | **GET** /flows/{id} | 
[**flow_controller_enqueue_write_action**](FlowApi.md#flow_controller_enqueue_write_action) | **POST** /flows/{id}/write/enqueue | 
[**flow_controller_flow_status**](FlowApi.md#flow_controller_flow_status) | **GET** /flows/{id}/status | 
[**flow_controller_get_flows_by_source**](FlowApi.md#flow_controller_get_flows_by_source) | **GET** /flows/by-source/{sourceId} | 
[**flow_controller_list**](FlowApi.md#flow_controller_list) | **GET** /flows | 
[**flow_controller_preview**](FlowApi.md#flow_controller_preview) | **POST** /flows/preview | 
[**flow_controller_status**](FlowApi.md#flow_controller_status) | **GET** /flows/{id}/write/status | 
[**flow_controller_update_flow**](FlowApi.md#flow_controller_update_flow) | **PUT** /flows/{id} | 
[**flow_controller_update_write_action_schedule**](FlowApi.md#flow_controller_update_write_action_schedule) | **PUT** /flows/{id}/write/schedule | 
[**flow_controller_update_write_action_settings**](FlowApi.md#flow_controller_update_write_action_settings) | **PUT** /flows/{id}/write/settings | 
[**flow_controller_update_write_action_status**](FlowApi.md#flow_controller_update_write_action_status) | **PUT** /flows/{id}/write/status | 
[**flow_controller_write_action_schedule**](FlowApi.md#flow_controller_write_action_schedule) | **GET** /flows/{id}/write/schedule | 
[**flow_controller_write_debug**](FlowApi.md#flow_controller_write_debug) | **GET** /flows/{id}/write/debug | 
[**flow_controller_write_detail**](FlowApi.md#flow_controller_write_detail) | **GET** /flows/{id}/write | 
[**flow_controller_write_log**](FlowApi.md#flow_controller_write_log) | **GET** /flows/{id}/write/log | 


# **flow_controller_api_debug**
> APIDebugResponse flow_controller_api_debug(id)



### Example


```python
import openapi_client
from openapi_client.models.api_debug_response import APIDebugResponse
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
    api_instance = openapi_client.FlowApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.flow_controller_api_debug(id)
        print("The response of FlowApi->flow_controller_api_debug:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_api_debug: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**APIDebugResponse**](APIDebugResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Checks whether the flow api endpoint is operable and logs the results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_api_detail**
> object flow_controller_api_detail(id)



### Example


```python
import openapi_client
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
    api_instance = openapi_client.FlowApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.flow_controller_api_detail(id)
        print("The response of FlowApi->flow_controller_api_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_api_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the detail of api endpoint associated to the flow |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_api_log**
> List[object] flow_controller_api_log(id)



### Example


```python
import openapi_client
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
    api_instance = openapi_client.FlowApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.flow_controller_api_log(id)
        print("The response of FlowApi->flow_controller_api_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_api_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**List[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get latest log entries related to api endpoint |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_clone**
> Flow flow_controller_clone(id)



### Example


```python
import openapi_client
from openapi_client.models.flow import Flow
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
    api_instance = openapi_client.FlowApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.flow_controller_clone(id)
        print("The response of FlowApi->flow_controller_clone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_clone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Flow**](Flow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Clones the existing flow |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_create_flow**
> Flow flow_controller_create_flow(body)



### Example


```python
import openapi_client
from openapi_client.models.flow import Flow
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
    api_instance = openapi_client.FlowApi(api_client)
    body = None # object | 

    try:
        api_response = api_instance.flow_controller_create_flow(body)
        print("The response of FlowApi->flow_controller_create_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_create_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

[**Flow**](Flow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Creates new flow |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_delete**
> flow_controller_delete(id)



### Example


```python
import openapi_client
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
    api_instance = openapi_client.FlowApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.flow_controller_delete(id)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deletes flow and all associated documents |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_delete_write_action_schedule**
> flow_controller_delete_write_action_schedule(id)



### Example


```python
import openapi_client
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
    api_instance = openapi_client.FlowApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.flow_controller_delete_write_action_schedule(id)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_delete_write_action_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Removes the flow write action schedule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_detail**
> Flow flow_controller_detail(id)



### Example


```python
import openapi_client
from openapi_client.models.flow import Flow
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
    api_instance = openapi_client.FlowApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.flow_controller_detail(id)
        print("The response of FlowApi->flow_controller_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Flow**](Flow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get flow detail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_enqueue_write_action**
> ActionEnqueuedDto flow_controller_enqueue_write_action(id, run_write_action_request=run_write_action_request)



### Example


```python
import openapi_client
from openapi_client.models.action_enqueued_dto import ActionEnqueuedDto
from openapi_client.models.run_write_action_request import RunWriteActionRequest
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
    api_instance = openapi_client.FlowApi(api_client)
    id = 'id_example' # str | 
    run_write_action_request = openapi_client.RunWriteActionRequest() # RunWriteActionRequest |  (optional)

    try:
        api_response = api_instance.flow_controller_enqueue_write_action(id, run_write_action_request=run_write_action_request)
        print("The response of FlowApi->flow_controller_enqueue_write_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_enqueue_write_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **run_write_action_request** | [**RunWriteActionRequest**](RunWriteActionRequest.md)|  | [optional] 

### Return type

[**ActionEnqueuedDto**](ActionEnqueuedDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Enqueues the write action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_flow_status**
> ActionCurrentState flow_controller_flow_status(id)



### Example


```python
import openapi_client
from openapi_client.models.action_current_state import ActionCurrentState
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
    api_instance = openapi_client.FlowApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.flow_controller_flow_status(id)
        print("The response of FlowApi->flow_controller_flow_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_flow_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ActionCurrentState**](ActionCurrentState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the current flow status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_get_flows_by_source**
> List[Flow] flow_controller_get_flows_by_source(source_id)



### Example


```python
import openapi_client
from openapi_client.models.flow import Flow
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
    api_instance = openapi_client.FlowApi(api_client)
    source_id = 'source_id_example' # str | 

    try:
        api_response = api_instance.flow_controller_get_flows_by_source(source_id)
        print("The response of FlowApi->flow_controller_get_flows_by_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_get_flows_by_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **str**|  | 

### Return type

[**List[Flow]**](Flow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get all flows that contain the given source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_list**
> List[Flow] flow_controller_list()



### Example


```python
import openapi_client
from openapi_client.models.flow import Flow
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
    api_instance = openapi_client.FlowApi(api_client)

    try:
        api_response = api_instance.flow_controller_list()
        print("The response of FlowApi->flow_controller_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Flow]**](Flow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all customer flows |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_preview**
> List[object] flow_controller_preview(body, limit=limit)



### Example


```python
import openapi_client
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
    api_instance = openapi_client.FlowApi(api_client)
    body = None # object | 
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.flow_controller_preview(body, limit=limit)
        print("The response of FlowApi->flow_controller_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 
 **limit** | **int**|  | [optional] 

### Return type

**List[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get flow data preview from DPI |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_status**
> ActionCurrentState flow_controller_status(id)



### Example


```python
import openapi_client
from openapi_client.models.action_current_state import ActionCurrentState
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
    api_instance = openapi_client.FlowApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.flow_controller_status(id)
        print("The response of FlowApi->flow_controller_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ActionCurrentState**](ActionCurrentState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the current flow write action status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_update_flow**
> Flow flow_controller_update_flow(id, body)



### Example


```python
import openapi_client
from openapi_client.models.flow import Flow
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
    api_instance = openapi_client.FlowApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.flow_controller_update_flow(id, body)
        print("The response of FlowApi->flow_controller_update_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_update_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**Flow**](Flow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates existing flow |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_update_write_action_schedule**
> Schedule flow_controller_update_write_action_schedule(id, update_schedule_request)



### Example


```python
import openapi_client
from openapi_client.models.schedule import Schedule
from openapi_client.models.update_schedule_request import UpdateScheduleRequest
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
    api_instance = openapi_client.FlowApi(api_client)
    id = 'id_example' # str | 
    update_schedule_request = openapi_client.UpdateScheduleRequest() # UpdateScheduleRequest | 

    try:
        api_response = api_instance.flow_controller_update_write_action_schedule(id, update_schedule_request)
        print("The response of FlowApi->flow_controller_update_write_action_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_update_write_action_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_schedule_request** | [**UpdateScheduleRequest**](UpdateScheduleRequest.md)|  | 

### Return type

[**Schedule**](Schedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates the schedule settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_update_write_action_settings**
> object flow_controller_update_write_action_settings(id, write_action_settings_request)



### Example


```python
import openapi_client
from openapi_client.models.write_action_settings_request import WriteActionSettingsRequest
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
    api_instance = openapi_client.FlowApi(api_client)
    id = 'id_example' # str | 
    write_action_settings_request = openapi_client.WriteActionSettingsRequest() # WriteActionSettingsRequest | 

    try:
        api_response = api_instance.flow_controller_update_write_action_settings(id, write_action_settings_request)
        print("The response of FlowApi->flow_controller_update_write_action_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_update_write_action_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **write_action_settings_request** | [**WriteActionSettingsRequest**](WriteActionSettingsRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates the write action settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_update_write_action_status**
> object flow_controller_update_write_action_status(id, body)



### Example


```python
import openapi_client
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
    api_instance = openapi_client.FlowApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.flow_controller_update_write_action_status(id, body)
        print("The response of FlowApi->flow_controller_update_write_action_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_update_write_action_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates the write action status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_write_action_schedule**
> Schedule flow_controller_write_action_schedule(id)



### Example


```python
import openapi_client
from openapi_client.models.schedule import Schedule
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
    api_instance = openapi_client.FlowApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.flow_controller_write_action_schedule(id)
        print("The response of FlowApi->flow_controller_write_action_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_write_action_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Schedule**](Schedule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the schedule of write action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_write_debug**
> WriterDebugResponse flow_controller_write_debug(id)



### Example


```python
import openapi_client
from openapi_client.models.writer_debug_response import WriterDebugResponse
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
    api_instance = openapi_client.FlowApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.flow_controller_write_debug(id)
        print("The response of FlowApi->flow_controller_write_debug:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_write_debug: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WriterDebugResponse**](WriterDebugResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Checks whether the write action is operable and logs the results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_write_detail**
> object flow_controller_write_detail(id)



### Example


```python
import openapi_client
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
    api_instance = openapi_client.FlowApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.flow_controller_write_detail(id)
        print("The response of FlowApi->flow_controller_write_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_write_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the detail of write action associated to the flow |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flow_controller_write_log**
> List[object] flow_controller_write_log(id)



### Example


```python
import openapi_client
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
    api_instance = openapi_client.FlowApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.flow_controller_write_log(id)
        print("The response of FlowApi->flow_controller_write_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowApi->flow_controller_write_log: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**List[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get latest log entries related to flow write actions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

