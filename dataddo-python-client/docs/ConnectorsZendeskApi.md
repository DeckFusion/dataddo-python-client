# openapi_client.ConnectorsZendeskApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zendesk_controller_action_authorization**](ConnectorsZendeskApi.md#zendesk_controller_action_authorization) | **GET** /connectors/zendesk/actions/authorization | List of authorization objects
[**zendesk_controller_action_date_range**](ConnectorsZendeskApi.md#zendesk_controller_action_date_range) | **GET** /connectors/zendesk/actions/dateRange | Method for listing date range
[**zendesk_controller_action_load**](ConnectorsZendeskApi.md#zendesk_controller_action_load) | **POST** /connectors/zendesk/create-source | Create Zendesk source
[**zendesk_controller_action_preview**](ConnectorsZendeskApi.md#zendesk_controller_action_preview) | **POST** /connectors/zendesk/preview | Preview the data
[**zendesk_controller_action_template**](ConnectorsZendeskApi.md#zendesk_controller_action_template) | **GET** /connectors/zendesk/templates/{id} | List details of dataset template
[**zendesk_controller_action_templates**](ConnectorsZendeskApi.md#zendesk_controller_action_templates) | **GET** /connectors/zendesk/templates | List all Zendesk dataset templates


# **zendesk_controller_action_authorization**
> List[ActionAuthorizationResponseInner] zendesk_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsZendeskApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.zendesk_controller_action_authorization()
        print("The response of ConnectorsZendeskApi->zendesk_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsZendeskApi->zendesk_controller_action_authorization: %s\n" % e)
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

# **zendesk_controller_action_date_range**
> List[LabelValueResponseInner] zendesk_controller_action_date_range()

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
    api_instance = openapi_client.ConnectorsZendeskApi(api_client)

    try:
        # Method for listing date range
        api_response = api_instance.zendesk_controller_action_date_range()
        print("The response of ConnectorsZendeskApi->zendesk_controller_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsZendeskApi->zendesk_controller_action_date_range: %s\n" % e)
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
**200** | List of Zendesk date ranges |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zendesk_controller_action_load**
> Source zendesk_controller_action_load(zendesk_connector_form=zendesk_connector_form)

Create Zendesk source

### Example


```python
import openapi_client
from openapi_client.models.source import Source
from openapi_client.models.zendesk_connector_form import ZendeskConnectorForm
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
    api_instance = openapi_client.ConnectorsZendeskApi(api_client)
    zendesk_connector_form = openapi_client.ZendeskConnectorForm() # ZendeskConnectorForm |  (optional)

    try:
        # Create Zendesk source
        api_response = api_instance.zendesk_controller_action_load(zendesk_connector_form=zendesk_connector_form)
        print("The response of ConnectorsZendeskApi->zendesk_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsZendeskApi->zendesk_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zendesk_connector_form** | [**ZendeskConnectorForm**](ZendeskConnectorForm.md)|  | [optional] 

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

# **zendesk_controller_action_preview**
> SuccessResponse zendesk_controller_action_preview(zendesk_connector_form=zendesk_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.success_response import SuccessResponse
from openapi_client.models.zendesk_connector_form import ZendeskConnectorForm
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
    api_instance = openapi_client.ConnectorsZendeskApi(api_client)
    zendesk_connector_form = openapi_client.ZendeskConnectorForm() # ZendeskConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.zendesk_controller_action_preview(zendesk_connector_form=zendesk_connector_form)
        print("The response of ConnectorsZendeskApi->zendesk_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsZendeskApi->zendesk_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zendesk_connector_form** | [**ZendeskConnectorForm**](ZendeskConnectorForm.md)|  | [optional] 

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

# **zendesk_controller_action_template**
> object zendesk_controller_action_template(id)

List details of dataset template

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
    api_instance = openapi_client.ConnectorsZendeskApi(api_client)
    id = 'id_example' # str | The id of the template to retrieve

    try:
        # List details of dataset template
        api_response = api_instance.zendesk_controller_action_template(id)
        print("The response of ConnectorsZendeskApi->zendesk_controller_action_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsZendeskApi->zendesk_controller_action_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the template to retrieve | 

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
**200** | List details of dataset template |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zendesk_controller_action_templates**
> ConnectorTemplateResponse zendesk_controller_action_templates()

List all Zendesk dataset templates

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
    api_instance = openapi_client.ConnectorsZendeskApi(api_client)

    try:
        # List all Zendesk dataset templates
        api_response = api_instance.zendesk_controller_action_templates()
        print("The response of ConnectorsZendeskApi->zendesk_controller_action_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsZendeskApi->zendesk_controller_action_templates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | List all Zendesk dataset templates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

