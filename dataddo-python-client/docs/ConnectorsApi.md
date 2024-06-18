# openapi_client.ConnectorsApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connector_controller_create_source**](ConnectorsApi.md#connector_controller_create_source) | **POST** /connectors/{connectorName}/create-source | 
[**connector_controller_get_action**](ConnectorsApi.md#connector_controller_get_action) | **GET** /connectors/{connectorName}/actions/{action} | 
[**connector_controller_list**](ConnectorsApi.md#connector_controller_list) | **GET** /connectors | 
[**connector_controller_post_action**](ConnectorsApi.md#connector_controller_post_action) | **POST** /connectors/{connectorName}/actions/{action} | 
[**connector_controller_preview**](ConnectorsApi.md#connector_controller_preview) | **POST** /connectors/{connectorName}/preview | 
[**connector_controller_template**](ConnectorsApi.md#connector_controller_template) | **GET** /connectors/{connectorName}/templates/{name} | 
[**connector_controller_templates**](ConnectorsApi.md#connector_controller_templates) | **GET** /connectors/{connectorName}/templates | 


# **connector_controller_create_source**
> object connector_controller_create_source(connector_name)



Creates the empty source with desired structure.

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
    api_instance = openapi_client.ConnectorsApi(api_client)
    connector_name = 'connector_name_example' # str | 

    try:
        api_response = api_instance.connector_controller_create_source(connector_name)
        print("The response of ConnectorsApi->connector_controller_create_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->connector_controller_create_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_name** | **str**|  | 

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
**200** | Description of the new source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connector_controller_get_action**
> List[object] connector_controller_get_action(connector_name, action)



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
    api_instance = openapi_client.ConnectorsApi(api_client)
    connector_name = 'connector_name_example' # str | 
    action = 'action_example' # str | 

    try:
        api_response = api_instance.connector_controller_get_action(connector_name, action)
        print("The response of ConnectorsApi->connector_controller_get_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->connector_controller_get_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_name** | **str**|  | 
 **action** | **str**|  | 

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
**200** | Authorization for connector |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connector_controller_list**
> List[ConnectorListResponse] connector_controller_list()



### Example


```python
import openapi_client
from openapi_client.models.connector_list_response import ConnectorListResponse
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
    api_instance = openapi_client.ConnectorsApi(api_client)

    try:
        api_response = api_instance.connector_controller_list()
        print("The response of ConnectorsApi->connector_controller_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->connector_controller_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ConnectorListResponse]**](ConnectorListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lists all available connectors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connector_controller_post_action**
> List[object] connector_controller_post_action(connector_name, action)



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
    api_instance = openapi_client.ConnectorsApi(api_client)
    connector_name = 'connector_name_example' # str | 
    action = 'action_example' # str | 

    try:
        api_response = api_instance.connector_controller_post_action(connector_name, action)
        print("The response of ConnectorsApi->connector_controller_post_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->connector_controller_post_action: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_name** | **str**|  | 
 **action** | **str**|  | 

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
**200** | Action of connector |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connector_controller_preview**
> List[object] connector_controller_preview(connector_name)



Loads the data and returns them for the data preview purpose

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
    api_instance = openapi_client.ConnectorsApi(api_client)
    connector_name = 'connector_name_example' # str | 

    try:
        api_response = api_instance.connector_controller_preview(connector_name)
        print("The response of ConnectorsApi->connector_controller_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->connector_controller_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_name** | **str**|  | 

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
**200** | Data preview |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connector_controller_template**
> object connector_controller_template(connector_name, name)



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
    api_instance = openapi_client.ConnectorsApi(api_client)
    connector_name = 'connector_name_example' # str | 
    name = 'name_example' # str | 

    try:
        api_response = api_instance.connector_controller_template(connector_name, name)
        print("The response of ConnectorsApi->connector_controller_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->connector_controller_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_name** | **str**|  | 
 **name** | **str**|  | 

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
**200** | Get template of connector |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connector_controller_templates**
> ConnectorTemplateResponse connector_controller_templates(connector_name)



### Example


```python
import openapi_client
from openapi_client.models.connector_template_response import ConnectorTemplateResponse
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
    api_instance = openapi_client.ConnectorsApi(api_client)
    connector_name = 'connector_name_example' # str | 

    try:
        api_response = api_instance.connector_controller_templates(connector_name)
        print("The response of ConnectorsApi->connector_controller_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsApi->connector_controller_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_name** | **str**|  | 

### Return type

[**ConnectorTemplateResponse**](ConnectorTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lists all available templates for connector |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

