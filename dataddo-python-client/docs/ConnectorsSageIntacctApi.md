# openapi_client.ConnectorsSageIntacctApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_sage_intacct_sage_intacct_connector_action_authorization**](ConnectorsSageIntacctApi.md#app_connector_sage_intacct_sage_intacct_connector_action_authorization) | **GET** /connectors/sage_intacct/actions/authorization | List of authorization objects
[**app_connector_sage_intacct_sage_intacct_connector_action_date_range**](ConnectorsSageIntacctApi.md#app_connector_sage_intacct_sage_intacct_connector_action_date_range) | **GET** /connectors/sage_intacct/actions/dateRange | List of dates
[**app_connector_sage_intacct_sage_intacct_connector_action_object**](ConnectorsSageIntacctApi.md#app_connector_sage_intacct_sage_intacct_connector_action_object) | **GET** /connectors/sage_intacct/actions/object | List of objects
[**app_connector_sage_intacct_sage_intacct_connector_action_property**](ConnectorsSageIntacctApi.md#app_connector_sage_intacct_sage_intacct_connector_action_property) | **GET** /connectors/sage_intacct/actions/property | List of properties
[**app_connector_sage_intacct_sage_intacct_connector_create_source**](ConnectorsSageIntacctApi.md#app_connector_sage_intacct_sage_intacct_connector_create_source) | **POST** /connectors/sage_intacct/create-source | Create Sage Intacct source
[**app_connector_sage_intacct_sage_intacct_connector_preview**](ConnectorsSageIntacctApi.md#app_connector_sage_intacct_sage_intacct_connector_preview) | **POST** /connectors/sage_intacct/preview | Data preview


# **app_connector_sage_intacct_sage_intacct_connector_action_authorization**
> List[ActionAuthorizationResponseInner] app_connector_sage_intacct_sage_intacct_connector_action_authorization()

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
    api_instance = openapi_client.ConnectorsSageIntacctApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_connector_sage_intacct_sage_intacct_connector_action_authorization()
        print("The response of ConnectorsSageIntacctApi->app_connector_sage_intacct_sage_intacct_connector_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSageIntacctApi->app_connector_sage_intacct_sage_intacct_connector_action_authorization: %s\n" % e)
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

# **app_connector_sage_intacct_sage_intacct_connector_action_date_range**
> List[LabelValueResponseInner] app_connector_sage_intacct_sage_intacct_connector_action_date_range()

List of dates

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
    api_instance = openapi_client.ConnectorsSageIntacctApi(api_client)

    try:
        # List of dates
        api_response = api_instance.app_connector_sage_intacct_sage_intacct_connector_action_date_range()
        print("The response of ConnectorsSageIntacctApi->app_connector_sage_intacct_sage_intacct_connector_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSageIntacctApi->app_connector_sage_intacct_sage_intacct_connector_action_date_range: %s\n" % e)
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
**200** | List of dates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_sage_intacct_sage_intacct_connector_action_object**
> List[LabelValueResponseInner] app_connector_sage_intacct_sage_intacct_connector_action_object()

List of objects

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
    api_instance = openapi_client.ConnectorsSageIntacctApi(api_client)

    try:
        # List of objects
        api_response = api_instance.app_connector_sage_intacct_sage_intacct_connector_action_object()
        print("The response of ConnectorsSageIntacctApi->app_connector_sage_intacct_sage_intacct_connector_action_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSageIntacctApi->app_connector_sage_intacct_sage_intacct_connector_action_object: %s\n" % e)
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
**200** | List of objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_sage_intacct_sage_intacct_connector_action_property**
> List[LabelValueResponseInner] app_connector_sage_intacct_sage_intacct_connector_action_property()

List of properties

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
    api_instance = openapi_client.ConnectorsSageIntacctApi(api_client)

    try:
        # List of properties
        api_response = api_instance.app_connector_sage_intacct_sage_intacct_connector_action_property()
        print("The response of ConnectorsSageIntacctApi->app_connector_sage_intacct_sage_intacct_connector_action_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSageIntacctApi->app_connector_sage_intacct_sage_intacct_connector_action_property: %s\n" % e)
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
**200** | List of properties |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_sage_intacct_sage_intacct_connector_create_source**
> Source app_connector_sage_intacct_sage_intacct_connector_create_source(sage_intacct_dto=sage_intacct_dto)

Create Sage Intacct source

### Example


```python
import openapi_client
from openapi_client.models.sage_intacct_dto import SageIntacctDto
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
    api_instance = openapi_client.ConnectorsSageIntacctApi(api_client)
    sage_intacct_dto = openapi_client.SageIntacctDto() # SageIntacctDto |  (optional)

    try:
        # Create Sage Intacct source
        api_response = api_instance.app_connector_sage_intacct_sage_intacct_connector_create_source(sage_intacct_dto=sage_intacct_dto)
        print("The response of ConnectorsSageIntacctApi->app_connector_sage_intacct_sage_intacct_connector_create_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSageIntacctApi->app_connector_sage_intacct_sage_intacct_connector_create_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sage_intacct_dto** | [**SageIntacctDto**](SageIntacctDto.md)|  | [optional] 

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
**200** | Created source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_sage_intacct_sage_intacct_connector_preview**
> SuccessResponse app_connector_sage_intacct_sage_intacct_connector_preview(sage_intacct_dto=sage_intacct_dto)

Data preview

### Example


```python
import openapi_client
from openapi_client.models.sage_intacct_dto import SageIntacctDto
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
    api_instance = openapi_client.ConnectorsSageIntacctApi(api_client)
    sage_intacct_dto = openapi_client.SageIntacctDto() # SageIntacctDto |  (optional)

    try:
        # Data preview
        api_response = api_instance.app_connector_sage_intacct_sage_intacct_connector_preview(sage_intacct_dto=sage_intacct_dto)
        print("The response of ConnectorsSageIntacctApi->app_connector_sage_intacct_sage_intacct_connector_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSageIntacctApi->app_connector_sage_intacct_sage_intacct_connector_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sage_intacct_dto** | [**SageIntacctDto**](SageIntacctDto.md)|  | [optional] 

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

