# openapi_client.SourceApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**source_controller_action_log**](SourceApi.md#source_controller_action_log) | **GET** /sources/{id}/action/log | 
[**source_controller_deactivate_source**](SourceApi.md#source_controller_deactivate_source) | **POST** /sources/{id}/extraction/deactivate | 
[**source_controller_delete**](SourceApi.md#source_controller_delete) | **DELETE** /sources/{id} | 
[**source_controller_detail**](SourceApi.md#source_controller_detail) | **GET** /sources/{id} | 
[**source_controller_detect**](SourceApi.md#source_controller_detect) | **GET** /sources/{id}/detect | 
[**source_controller_enqueue_extraction**](SourceApi.md#source_controller_enqueue_extraction) | **POST** /sources/{id}/extraction/enqueue | 
[**source_controller_extraction_debug**](SourceApi.md#source_controller_extraction_debug) | **GET** /sources/{id}/extraction/debug | 
[**source_controller_extraction_detail**](SourceApi.md#source_controller_extraction_detail) | **GET** /sources/{id}/extraction | 
[**source_controller_extraction_schedule**](SourceApi.md#source_controller_extraction_schedule) | **GET** /sources/{id}/extraction/schedule | 
[**source_controller_list**](SourceApi.md#source_controller_list) | **GET** /sources | 
[**source_controller_metadata**](SourceApi.md#source_controller_metadata) | **GET** /sources/{id}/metadata | 
[**source_controller_preview**](SourceApi.md#source_controller_preview) | **GET** /sources/{id}/preview | 
[**source_controller_source_request**](SourceApi.md#source_controller_source_request) | **GET** /sources/{id}/request | 
[**source_controller_source_status**](SourceApi.md#source_controller_source_status) | **GET** /sources/{id}/status | 
[**source_controller_update**](SourceApi.md#source_controller_update) | **PUT** /sources/{id} | 
[**source_controller_update_extraction**](SourceApi.md#source_controller_update_extraction) | **PUT** /sources/{id}/extraction | 
[**source_controller_update_extraction_schedule**](SourceApi.md#source_controller_update_extraction_schedule) | **PUT** /sources/{id}/extraction/schedule | 
[**source_controller_update_source_request**](SourceApi.md#source_controller_update_source_request) | **PUT** /sources/{id}/request | 


# **source_controller_action_log**
> List[object] source_controller_action_log(id)



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
    api_instance = openapi_client.SourceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.source_controller_action_log(id)
        print("The response of SourceApi->source_controller_action_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_controller_action_log: %s\n" % e)
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
**200** | Get latest log entries related to source action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_controller_deactivate_source**
> ExtractionAction source_controller_deactivate_source(id, extraction_action)



### Example


```python
import openapi_client
from openapi_client.models.extraction_action import ExtractionAction
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
    api_instance = openapi_client.SourceApi(api_client)
    id = 'id_example' # str | 
    extraction_action = openapi_client.ExtractionAction() # ExtractionAction | 

    try:
        api_response = api_instance.source_controller_deactivate_source(id, extraction_action)
        print("The response of SourceApi->source_controller_deactivate_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_controller_deactivate_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **extraction_action** | [**ExtractionAction**](ExtractionAction.md)|  | 

### Return type

[**ExtractionAction**](ExtractionAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates extraction action settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_controller_delete**
> source_controller_delete(id)



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
    api_instance = openapi_client.SourceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.source_controller_delete(id)
    except Exception as e:
        print("Exception when calling SourceApi->source_controller_delete: %s\n" % e)
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
**204** | Deletes source and all other related documents |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_controller_detail**
> SourceDTO source_controller_detail(id)



### Example


```python
import openapi_client
from openapi_client.models.source_dto import SourceDTO
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
    api_instance = openapi_client.SourceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.source_controller_detail(id)
        print("The response of SourceApi->source_controller_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_controller_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SourceDTO**](SourceDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get source detail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_controller_detect**
> List[object] source_controller_detect(id)



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
    api_instance = openapi_client.SourceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.source_controller_detect(id)
        print("The response of SourceApi->source_controller_detect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_controller_detect: %s\n" % e)
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
**200** | Detector service endpoint |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_controller_enqueue_extraction**
> source_controller_enqueue_extraction(id, run_extraction_request=run_extraction_request)



### Example


```python
import openapi_client
from openapi_client.models.run_extraction_request import RunExtractionRequest
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
    api_instance = openapi_client.SourceApi(api_client)
    id = 'id_example' # str | 
    run_extraction_request = openapi_client.RunExtractionRequest() # RunExtractionRequest |  (optional)

    try:
        api_instance.source_controller_enqueue_extraction(id, run_extraction_request=run_extraction_request)
    except Exception as e:
        print("Exception when calling SourceApi->source_controller_enqueue_extraction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **run_extraction_request** | [**RunExtractionRequest**](RunExtractionRequest.md)|  | [optional] 

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
**202** | Enqueues the source action to be processed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_controller_extraction_debug**
> ExtractionDebugResponse source_controller_extraction_debug(id)



### Example


```python
import openapi_client
from openapi_client.models.extraction_debug_response import ExtractionDebugResponse
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
    api_instance = openapi_client.SourceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.source_controller_extraction_debug(id)
        print("The response of SourceApi->source_controller_extraction_debug:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_controller_extraction_debug: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ExtractionDebugResponse**](ExtractionDebugResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Checks whether the extraction is operable and logs the results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_controller_extraction_detail**
> ExtractionAction source_controller_extraction_detail(id)



### Example


```python
import openapi_client
from openapi_client.models.extraction_action import ExtractionAction
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
    api_instance = openapi_client.SourceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.source_controller_extraction_detail(id)
        print("The response of SourceApi->source_controller_extraction_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_controller_extraction_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ExtractionAction**](ExtractionAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the detail of extraction associated to the source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_controller_extraction_schedule**
> Schedule source_controller_extraction_schedule(id)



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
    api_instance = openapi_client.SourceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.source_controller_extraction_schedule(id)
        print("The response of SourceApi->source_controller_extraction_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_controller_extraction_schedule: %s\n" % e)
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
**200** | Get the schedule of extraction action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_controller_list**
> List[Source] source_controller_list()



### Example


```python
import openapi_client
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
    api_instance = openapi_client.SourceApi(api_client)

    try:
        api_response = api_instance.source_controller_list()
        print("The response of SourceApi->source_controller_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_controller_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Source]**](Source.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An example resource |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_controller_metadata**
> object source_controller_metadata(id)



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
    api_instance = openapi_client.SourceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.source_controller_metadata(id)
        print("The response of SourceApi->source_controller_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_controller_metadata: %s\n" % e)
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
**200** | Get source params used when the source was created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_controller_preview**
> List[object] source_controller_preview(id, limit=limit)



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
    api_instance = openapi_client.SourceApi(api_client)
    id = 'id_example' # str | 
    limit = 56 # int |  (optional)

    try:
        api_response = api_instance.source_controller_preview(id, limit=limit)
        print("The response of SourceApi->source_controller_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_controller_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] 

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
**200** | Preview the source data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_controller_source_request**
> object source_controller_source_request(id)



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
    api_instance = openapi_client.SourceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.source_controller_source_request(id)
        print("The response of SourceApi->source_controller_source_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_controller_source_request: %s\n" % e)
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
**200** | Get the request metadata used for source extraction |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_controller_source_status**
> ActionCurrentState source_controller_source_status(id)



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
    api_instance = openapi_client.SourceApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.source_controller_source_status(id)
        print("The response of SourceApi->source_controller_source_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_controller_source_status: %s\n" % e)
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
**200** | Get the source current status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_controller_update**
> Source source_controller_update(id, body)



### Example


```python
import openapi_client
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
    api_instance = openapi_client.SourceApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.source_controller_update(id, body)
        print("The response of SourceApi->source_controller_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_controller_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

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
**200** | Updates the source basic information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_controller_update_extraction**
> ExtractionAction source_controller_update_extraction(id, body)



### Example


```python
import openapi_client
from openapi_client.models.extraction_action import ExtractionAction
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
    api_instance = openapi_client.SourceApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.source_controller_update_extraction(id, body)
        print("The response of SourceApi->source_controller_update_extraction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_controller_update_extraction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**ExtractionAction**](ExtractionAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates extraction action settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **source_controller_update_extraction_schedule**
> Schedule source_controller_update_extraction_schedule(id, update_schedule_request)



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
    api_instance = openapi_client.SourceApi(api_client)
    id = 'id_example' # str | 
    update_schedule_request = openapi_client.UpdateScheduleRequest() # UpdateScheduleRequest | 

    try:
        api_response = api_instance.source_controller_update_extraction_schedule(id, update_schedule_request)
        print("The response of SourceApi->source_controller_update_extraction_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_controller_update_extraction_schedule: %s\n" % e)
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

# **source_controller_update_source_request**
> object source_controller_update_source_request(id, body)



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
    api_instance = openapi_client.SourceApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        api_response = api_instance.source_controller_update_source_request(id, body)
        print("The response of SourceApi->source_controller_update_source_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourceApi->source_controller_update_source_request: %s\n" % e)
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
**200** | Updates request settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

