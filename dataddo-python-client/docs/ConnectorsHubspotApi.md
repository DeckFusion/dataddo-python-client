# openapi_client.ConnectorsHubspotApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hubspot_controller_action_authorization**](ConnectorsHubspotApi.md#hubspot_controller_action_authorization) | **GET** /connectors/hubspot/actions/authorization | List of authorization objects
[**hubspot_controller_action_date_range**](ConnectorsHubspotApi.md#hubspot_controller_action_date_range) | **GET** /connectors/hubspot/actions/dateRange | List of date ranges
[**hubspot_controller_action_load**](ConnectorsHubspotApi.md#hubspot_controller_action_load) | **POST** /connectors/hubspot/create-source | Create a Hubspot source
[**hubspot_controller_action_object**](ConnectorsHubspotApi.md#hubspot_controller_action_object) | **POST** /connectors/hubspot/actions/object | List of objects
[**hubspot_controller_action_preview**](ConnectorsHubspotApi.md#hubspot_controller_action_preview) | **POST** /connectors/hubspot/preview | Preview the data
[**hubspot_controller_action_property**](ConnectorsHubspotApi.md#hubspot_controller_action_property) | **POST** /connectors/hubspot/actions/properties | List of properties


# **hubspot_controller_action_authorization**
> List[ActionAuthorizationResponseInner] hubspot_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsHubspotApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.hubspot_controller_action_authorization()
        print("The response of ConnectorsHubspotApi->hubspot_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsHubspotApi->hubspot_controller_action_authorization: %s\n" % e)
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

# **hubspot_controller_action_date_range**
> List[LabelValueResponseInner] hubspot_controller_action_date_range()

List of date ranges

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
    api_instance = openapi_client.ConnectorsHubspotApi(api_client)

    try:
        # List of date ranges
        api_response = api_instance.hubspot_controller_action_date_range()
        print("The response of ConnectorsHubspotApi->hubspot_controller_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsHubspotApi->hubspot_controller_action_date_range: %s\n" % e)
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
**200** | List of date range objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hubspot_controller_action_load**
> Source hubspot_controller_action_load(hubspot_connector_form=hubspot_connector_form)

Create a Hubspot source

### Example


```python
import openapi_client
from openapi_client.models.hubspot_connector_form import HubspotConnectorForm
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
    api_instance = openapi_client.ConnectorsHubspotApi(api_client)
    hubspot_connector_form = openapi_client.HubspotConnectorForm() # HubspotConnectorForm |  (optional)

    try:
        # Create a Hubspot source
        api_response = api_instance.hubspot_controller_action_load(hubspot_connector_form=hubspot_connector_form)
        print("The response of ConnectorsHubspotApi->hubspot_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsHubspotApi->hubspot_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hubspot_connector_form** | [**HubspotConnectorForm**](HubspotConnectorForm.md)|  | [optional] 

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

# **hubspot_controller_action_object**
> List[LabelValueResponseInner] hubspot_controller_action_object(black_diamond_batch_controller_action_object_request=black_diamond_batch_controller_action_object_request)

List of objects

List all available objects

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
    api_instance = openapi_client.ConnectorsHubspotApi(api_client)
    black_diamond_batch_controller_action_object_request = openapi_client.BlackDiamondBatchControllerActionObjectRequest() # BlackDiamondBatchControllerActionObjectRequest |  (optional)

    try:
        # List of objects
        api_response = api_instance.hubspot_controller_action_object(black_diamond_batch_controller_action_object_request=black_diamond_batch_controller_action_object_request)
        print("The response of ConnectorsHubspotApi->hubspot_controller_action_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsHubspotApi->hubspot_controller_action_object: %s\n" % e)
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

# **hubspot_controller_action_preview**
> SuccessResponse hubspot_controller_action_preview(hubspot_connector_form=hubspot_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.hubspot_connector_form import HubspotConnectorForm
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
    api_instance = openapi_client.ConnectorsHubspotApi(api_client)
    hubspot_connector_form = openapi_client.HubspotConnectorForm() # HubspotConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.hubspot_controller_action_preview(hubspot_connector_form=hubspot_connector_form)
        print("The response of ConnectorsHubspotApi->hubspot_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsHubspotApi->hubspot_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hubspot_connector_form** | [**HubspotConnectorForm**](HubspotConnectorForm.md)|  | [optional] 

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

# **hubspot_controller_action_property**
> List[LabelValueResponseInner] hubspot_controller_action_property(hubspot_controller_action_property_request=hubspot_controller_action_property_request)

List of properties

List available properties

### Example


```python
import openapi_client
from openapi_client.models.hubspot_controller_action_property_request import HubspotControllerActionPropertyRequest
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
    api_instance = openapi_client.ConnectorsHubspotApi(api_client)
    hubspot_controller_action_property_request = openapi_client.HubspotControllerActionPropertyRequest() # HubspotControllerActionPropertyRequest |  (optional)

    try:
        # List of properties
        api_response = api_instance.hubspot_controller_action_property(hubspot_controller_action_property_request=hubspot_controller_action_property_request)
        print("The response of ConnectorsHubspotApi->hubspot_controller_action_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsHubspotApi->hubspot_controller_action_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hubspot_controller_action_property_request** | [**HubspotControllerActionPropertyRequest**](HubspotControllerActionPropertyRequest.md)|  | [optional] 

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
**200** | List of all available properties |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

