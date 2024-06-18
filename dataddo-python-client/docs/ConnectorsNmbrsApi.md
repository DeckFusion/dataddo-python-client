# openapi_client.ConnectorsNmbrsApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_nmbrs_nmbrs_connector_action_authorization**](ConnectorsNmbrsApi.md#app_connector_nmbrs_nmbrs_connector_action_authorization) | **GET** /connectors/nmbrs/actions/authorization | List of authorization objects
[**app_connector_nmbrs_nmbrs_connector_action_company**](ConnectorsNmbrsApi.md#app_connector_nmbrs_nmbrs_connector_action_company) | **POST** /connectors/nmbrs/actions/company | List of companies
[**app_connector_nmbrs_nmbrs_connector_action_date_range**](ConnectorsNmbrsApi.md#app_connector_nmbrs_nmbrs_connector_action_date_range) | **GET** /connectors/nmbrs/actions/dateRange | List of dates
[**app_connector_nmbrs_nmbrs_connector_action_domain**](ConnectorsNmbrsApi.md#app_connector_nmbrs_nmbrs_connector_action_domain) | **POST** /connectors/nmbrs/actions/domain | List of domains
[**app_connector_nmbrs_nmbrs_connector_create_source**](ConnectorsNmbrsApi.md#app_connector_nmbrs_nmbrs_connector_create_source) | **POST** /connectors/nmbrs/create-source | Create Nmbrs source
[**app_connector_nmbrs_nmbrs_connector_preview**](ConnectorsNmbrsApi.md#app_connector_nmbrs_nmbrs_connector_preview) | **POST** /connectors/nmbrs/preview | Data preview


# **app_connector_nmbrs_nmbrs_connector_action_authorization**
> List[ActionAuthorizationResponseInner] app_connector_nmbrs_nmbrs_connector_action_authorization()

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
    api_instance = openapi_client.ConnectorsNmbrsApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_connector_nmbrs_nmbrs_connector_action_authorization()
        print("The response of ConnectorsNmbrsApi->app_connector_nmbrs_nmbrs_connector_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsNmbrsApi->app_connector_nmbrs_nmbrs_connector_action_authorization: %s\n" % e)
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

# **app_connector_nmbrs_nmbrs_connector_action_company**
> List[LabelValueResponseInner] app_connector_nmbrs_nmbrs_connector_action_company()

List of companies

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
    api_instance = openapi_client.ConnectorsNmbrsApi(api_client)

    try:
        # List of companies
        api_response = api_instance.app_connector_nmbrs_nmbrs_connector_action_company()
        print("The response of ConnectorsNmbrsApi->app_connector_nmbrs_nmbrs_connector_action_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsNmbrsApi->app_connector_nmbrs_nmbrs_connector_action_company: %s\n" % e)
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
**200** | List of companies |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_nmbrs_nmbrs_connector_action_date_range**
> List[LabelValueResponseInner] app_connector_nmbrs_nmbrs_connector_action_date_range()

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
    api_instance = openapi_client.ConnectorsNmbrsApi(api_client)

    try:
        # List of dates
        api_response = api_instance.app_connector_nmbrs_nmbrs_connector_action_date_range()
        print("The response of ConnectorsNmbrsApi->app_connector_nmbrs_nmbrs_connector_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsNmbrsApi->app_connector_nmbrs_nmbrs_connector_action_date_range: %s\n" % e)
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

# **app_connector_nmbrs_nmbrs_connector_action_domain**
> List[LabelValueResponseInner] app_connector_nmbrs_nmbrs_connector_action_domain()

List of domains

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
    api_instance = openapi_client.ConnectorsNmbrsApi(api_client)

    try:
        # List of domains
        api_response = api_instance.app_connector_nmbrs_nmbrs_connector_action_domain()
        print("The response of ConnectorsNmbrsApi->app_connector_nmbrs_nmbrs_connector_action_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsNmbrsApi->app_connector_nmbrs_nmbrs_connector_action_domain: %s\n" % e)
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
**200** | List of domains |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_nmbrs_nmbrs_connector_create_source**
> Source app_connector_nmbrs_nmbrs_connector_create_source(nmbrs_dto=nmbrs_dto)

Create Nmbrs source

### Example


```python
import openapi_client
from openapi_client.models.nmbrs_dto import NmbrsDto
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
    api_instance = openapi_client.ConnectorsNmbrsApi(api_client)
    nmbrs_dto = openapi_client.NmbrsDto() # NmbrsDto |  (optional)

    try:
        # Create Nmbrs source
        api_response = api_instance.app_connector_nmbrs_nmbrs_connector_create_source(nmbrs_dto=nmbrs_dto)
        print("The response of ConnectorsNmbrsApi->app_connector_nmbrs_nmbrs_connector_create_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsNmbrsApi->app_connector_nmbrs_nmbrs_connector_create_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nmbrs_dto** | [**NmbrsDto**](NmbrsDto.md)|  | [optional] 

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

# **app_connector_nmbrs_nmbrs_connector_preview**
> SuccessResponse app_connector_nmbrs_nmbrs_connector_preview(nmbrs_dto=nmbrs_dto)

Data preview

### Example


```python
import openapi_client
from openapi_client.models.nmbrs_dto import NmbrsDto
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
    api_instance = openapi_client.ConnectorsNmbrsApi(api_client)
    nmbrs_dto = openapi_client.NmbrsDto() # NmbrsDto |  (optional)

    try:
        # Data preview
        api_response = api_instance.app_connector_nmbrs_nmbrs_connector_preview(nmbrs_dto=nmbrs_dto)
        print("The response of ConnectorsNmbrsApi->app_connector_nmbrs_nmbrs_connector_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsNmbrsApi->app_connector_nmbrs_nmbrs_connector_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nmbrs_dto** | [**NmbrsDto**](NmbrsDto.md)|  | [optional] 

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

