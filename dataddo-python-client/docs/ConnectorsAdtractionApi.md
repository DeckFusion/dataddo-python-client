# openapi_client.ConnectorsAdtractionApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_adtraction_adtraction_connector_action_authorization**](ConnectorsAdtractionApi.md#app_connector_adtraction_adtraction_connector_action_authorization) | **GET** /connectors/adtraction/actions/authorization | List of authorization objects
[**app_connector_adtraction_adtraction_connector_action_date_range**](ConnectorsAdtractionApi.md#app_connector_adtraction_adtraction_connector_action_date_range) | **GET** /connectors/adtraction/actions/dateRange | Method for listing date range
[**app_connector_adtraction_adtraction_connector_create_source**](ConnectorsAdtractionApi.md#app_connector_adtraction_adtraction_connector_create_source) | **POST** /connectors/adtraction/create-source | Create Adtraction source
[**app_connector_adtraction_adtraction_connector_preview**](ConnectorsAdtractionApi.md#app_connector_adtraction_adtraction_connector_preview) | **POST** /connectors/adtraction/preview | Data preview


# **app_connector_adtraction_adtraction_connector_action_authorization**
> List[ActionAuthorizationResponseInner] app_connector_adtraction_adtraction_connector_action_authorization()

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
    api_instance = openapi_client.ConnectorsAdtractionApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_connector_adtraction_adtraction_connector_action_authorization()
        print("The response of ConnectorsAdtractionApi->app_connector_adtraction_adtraction_connector_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAdtractionApi->app_connector_adtraction_adtraction_connector_action_authorization: %s\n" % e)
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

# **app_connector_adtraction_adtraction_connector_action_date_range**
> List[LabelValueResponseInner] app_connector_adtraction_adtraction_connector_action_date_range()

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
    api_instance = openapi_client.ConnectorsAdtractionApi(api_client)

    try:
        # Method for listing date range
        api_response = api_instance.app_connector_adtraction_adtraction_connector_action_date_range()
        print("The response of ConnectorsAdtractionApi->app_connector_adtraction_adtraction_connector_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAdtractionApi->app_connector_adtraction_adtraction_connector_action_date_range: %s\n" % e)
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
**200** | List of Adtraction date ranges |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_adtraction_adtraction_connector_create_source**
> Source app_connector_adtraction_adtraction_connector_create_source(adtraction_connector_form=adtraction_connector_form)

Create Adtraction source

### Example


```python
import openapi_client
from openapi_client.models.adtraction_connector_form import AdtractionConnectorForm
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
    api_instance = openapi_client.ConnectorsAdtractionApi(api_client)
    adtraction_connector_form = openapi_client.AdtractionConnectorForm() # AdtractionConnectorForm |  (optional)

    try:
        # Create Adtraction source
        api_response = api_instance.app_connector_adtraction_adtraction_connector_create_source(adtraction_connector_form=adtraction_connector_form)
        print("The response of ConnectorsAdtractionApi->app_connector_adtraction_adtraction_connector_create_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAdtractionApi->app_connector_adtraction_adtraction_connector_create_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adtraction_connector_form** | [**AdtractionConnectorForm**](AdtractionConnectorForm.md)|  | [optional] 

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

# **app_connector_adtraction_adtraction_connector_preview**
> SuccessResponse app_connector_adtraction_adtraction_connector_preview(adtraction_connector_form=adtraction_connector_form)

Data preview

### Example


```python
import openapi_client
from openapi_client.models.adtraction_connector_form import AdtractionConnectorForm
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
    api_instance = openapi_client.ConnectorsAdtractionApi(api_client)
    adtraction_connector_form = openapi_client.AdtractionConnectorForm() # AdtractionConnectorForm |  (optional)

    try:
        # Data preview
        api_response = api_instance.app_connector_adtraction_adtraction_connector_preview(adtraction_connector_form=adtraction_connector_form)
        print("The response of ConnectorsAdtractionApi->app_connector_adtraction_adtraction_connector_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAdtractionApi->app_connector_adtraction_adtraction_connector_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adtraction_connector_form** | [**AdtractionConnectorForm**](AdtractionConnectorForm.md)|  | [optional] 

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

