# openapi_client.ConnectorsZemantaApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_zemanta_zemanta_connector_action_account**](ConnectorsZemantaApi.md#app_connector_zemanta_zemanta_connector_action_account) | **GET** /connectors/zemanta/actions/account | List of Zemanta accounts
[**app_connector_zemanta_zemanta_connector_action_date_range**](ConnectorsZemantaApi.md#app_connector_zemanta_zemanta_connector_action_date_range) | **GET** /connectors/zemanta/actions/dateRange | Method for listing date range
[**app_connector_zemanta_zemanta_connector_action_entities**](ConnectorsZemantaApi.md#app_connector_zemanta_zemanta_connector_action_entities) | **GET** /connectors/zemanta/actions/entities | List of Zemanta common fields
[**app_connector_zemanta_zemanta_connector_action_filters**](ConnectorsZemantaApi.md#app_connector_zemanta_zemanta_connector_action_filters) | **GET** /connectors/zemanta/actions/filters | List of Zemanta common fields
[**app_connector_zemanta_zemanta_connector_action_metrics**](ConnectorsZemantaApi.md#app_connector_zemanta_zemanta_connector_action_metrics) | **GET** /connectors/zemanta/actions/metrics | List of Zemanta common fields
[**app_connector_zemanta_zemanta_connector_action_options**](ConnectorsZemantaApi.md#app_connector_zemanta_zemanta_connector_action_options) | **GET** /connectors/zemanta/actions/options | List of Zemanta common fields
[**app_connector_zemanta_zemanta_connector_preview**](ConnectorsZemantaApi.md#app_connector_zemanta_zemanta_connector_preview) | **POST** /connectors/zemanta/preview | Data preview


# **app_connector_zemanta_zemanta_connector_action_account**
> List[LabelValueResponseInner] app_connector_zemanta_zemanta_connector_action_account()

List of Zemanta accounts

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
    api_instance = openapi_client.ConnectorsZemantaApi(api_client)

    try:
        # List of Zemanta accounts
        api_response = api_instance.app_connector_zemanta_zemanta_connector_action_account()
        print("The response of ConnectorsZemantaApi->app_connector_zemanta_zemanta_connector_action_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsZemantaApi->app_connector_zemanta_zemanta_connector_action_account: %s\n" % e)
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
**200** | List of available advertisers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_zemanta_zemanta_connector_action_date_range**
> List[LabelValueResponseInner] app_connector_zemanta_zemanta_connector_action_date_range()

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
    api_instance = openapi_client.ConnectorsZemantaApi(api_client)

    try:
        # Method for listing date range
        api_response = api_instance.app_connector_zemanta_zemanta_connector_action_date_range()
        print("The response of ConnectorsZemantaApi->app_connector_zemanta_zemanta_connector_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsZemantaApi->app_connector_zemanta_zemanta_connector_action_date_range: %s\n" % e)
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
**200** | List of Zemanta date ranges |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_zemanta_zemanta_connector_action_entities**
> List[LabelValueResponseInner] app_connector_zemanta_zemanta_connector_action_entities()

List of Zemanta common fields

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
    api_instance = openapi_client.ConnectorsZemantaApi(api_client)

    try:
        # List of Zemanta common fields
        api_response = api_instance.app_connector_zemanta_zemanta_connector_action_entities()
        print("The response of ConnectorsZemantaApi->app_connector_zemanta_zemanta_connector_action_entities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsZemantaApi->app_connector_zemanta_zemanta_connector_action_entities: %s\n" % e)
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
**200** | List of available fields |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_zemanta_zemanta_connector_action_filters**
> List[LabelValueResponseInner] app_connector_zemanta_zemanta_connector_action_filters()

List of Zemanta common fields

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
    api_instance = openapi_client.ConnectorsZemantaApi(api_client)

    try:
        # List of Zemanta common fields
        api_response = api_instance.app_connector_zemanta_zemanta_connector_action_filters()
        print("The response of ConnectorsZemantaApi->app_connector_zemanta_zemanta_connector_action_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsZemantaApi->app_connector_zemanta_zemanta_connector_action_filters: %s\n" % e)
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
**200** | List of available fields |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_zemanta_zemanta_connector_action_metrics**
> List[LabelValueResponseInner] app_connector_zemanta_zemanta_connector_action_metrics()

List of Zemanta common fields

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
    api_instance = openapi_client.ConnectorsZemantaApi(api_client)

    try:
        # List of Zemanta common fields
        api_response = api_instance.app_connector_zemanta_zemanta_connector_action_metrics()
        print("The response of ConnectorsZemantaApi->app_connector_zemanta_zemanta_connector_action_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsZemantaApi->app_connector_zemanta_zemanta_connector_action_metrics: %s\n" % e)
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
**200** | List of available fields |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_zemanta_zemanta_connector_action_options**
> List[LabelValueResponseInner] app_connector_zemanta_zemanta_connector_action_options()

List of Zemanta common fields

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
    api_instance = openapi_client.ConnectorsZemantaApi(api_client)

    try:
        # List of Zemanta common fields
        api_response = api_instance.app_connector_zemanta_zemanta_connector_action_options()
        print("The response of ConnectorsZemantaApi->app_connector_zemanta_zemanta_connector_action_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsZemantaApi->app_connector_zemanta_zemanta_connector_action_options: %s\n" % e)
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
**200** | List of available fields |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_zemanta_zemanta_connector_preview**
> SuccessResponse app_connector_zemanta_zemanta_connector_preview(zemanta_dto=zemanta_dto)

Data preview

### Example


```python
import openapi_client
from openapi_client.models.success_response import SuccessResponse
from openapi_client.models.zemanta_dto import ZemantaDto
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
    api_instance = openapi_client.ConnectorsZemantaApi(api_client)
    zemanta_dto = openapi_client.ZemantaDto() # ZemantaDto |  (optional)

    try:
        # Data preview
        api_response = api_instance.app_connector_zemanta_zemanta_connector_preview(zemanta_dto=zemanta_dto)
        print("The response of ConnectorsZemantaApi->app_connector_zemanta_zemanta_connector_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsZemantaApi->app_connector_zemanta_zemanta_connector_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zemanta_dto** | [**ZemantaDto**](ZemantaDto.md)|  | [optional] 

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

