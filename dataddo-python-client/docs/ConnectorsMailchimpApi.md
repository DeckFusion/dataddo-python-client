# openapi_client.ConnectorsMailchimpApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mailchimp_controller_action_authorization**](ConnectorsMailchimpApi.md#mailchimp_controller_action_authorization) | **GET** /connectors/mailchimp/actions/authorization | List of authorization objects
[**mailchimp_controller_action_dc**](ConnectorsMailchimpApi.md#mailchimp_controller_action_dc) | **POST** /connectors/mailchimp/actions/dc | List of data centers
[**mailchimp_controller_action_list**](ConnectorsMailchimpApi.md#mailchimp_controller_action_list) | **POST** /connectors/mailchimp/actions/list | List of contacts
[**mailchimp_controller_action_load**](ConnectorsMailchimpApi.md#mailchimp_controller_action_load) | **POST** /connectors/mailchimp/create-source | Create Mailchimp User source
[**mailchimp_controller_action_preview**](ConnectorsMailchimpApi.md#mailchimp_controller_action_preview) | **POST** /connectors/mailchimp/preview | Preview the data
[**mailchimp_controller_action_template**](ConnectorsMailchimpApi.md#mailchimp_controller_action_template) | **GET** /connectors/mailchimp/templates/{id} | List details of dataset template
[**mailchimp_controller_action_templates**](ConnectorsMailchimpApi.md#mailchimp_controller_action_templates) | **GET** /connectors/mailchimp/templates | List all Mailchimp dataset templates


# **mailchimp_controller_action_authorization**
> List[ActionAuthorizationResponseInner] mailchimp_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsMailchimpApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.mailchimp_controller_action_authorization()
        print("The response of ConnectorsMailchimpApi->mailchimp_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMailchimpApi->mailchimp_controller_action_authorization: %s\n" % e)
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

# **mailchimp_controller_action_dc**
> List[MailchimpControllerActionDc200ResponseInner] mailchimp_controller_action_dc()

List of data centers

### Example


```python
import openapi_client
from openapi_client.models.mailchimp_controller_action_dc200_response_inner import MailchimpControllerActionDc200ResponseInner
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
    api_instance = openapi_client.ConnectorsMailchimpApi(api_client)

    try:
        # List of data centers
        api_response = api_instance.mailchimp_controller_action_dc()
        print("The response of ConnectorsMailchimpApi->mailchimp_controller_action_dc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMailchimpApi->mailchimp_controller_action_dc: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MailchimpControllerActionDc200ResponseInner]**](MailchimpControllerActionDc200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of data centers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mailchimp_controller_action_list**
> List[LabelValueResponseInner] mailchimp_controller_action_list(mailchimp_controller_action_list_request=mailchimp_controller_action_list_request)

List of contacts

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.mailchimp_controller_action_list_request import MailchimpControllerActionListRequest
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
    api_instance = openapi_client.ConnectorsMailchimpApi(api_client)
    mailchimp_controller_action_list_request = openapi_client.MailchimpControllerActionListRequest() # MailchimpControllerActionListRequest |  (optional)

    try:
        # List of contacts
        api_response = api_instance.mailchimp_controller_action_list(mailchimp_controller_action_list_request=mailchimp_controller_action_list_request)
        print("The response of ConnectorsMailchimpApi->mailchimp_controller_action_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMailchimpApi->mailchimp_controller_action_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailchimp_controller_action_list_request** | [**MailchimpControllerActionListRequest**](MailchimpControllerActionListRequest.md)|  | [optional] 

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
**200** | List of contacts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mailchimp_controller_action_load**
> Source mailchimp_controller_action_load(mailchimp_connector_form=mailchimp_connector_form)

Create Mailchimp User source

### Example


```python
import openapi_client
from openapi_client.models.mailchimp_connector_form import MailchimpConnectorForm
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
    api_instance = openapi_client.ConnectorsMailchimpApi(api_client)
    mailchimp_connector_form = openapi_client.MailchimpConnectorForm() # MailchimpConnectorForm |  (optional)

    try:
        # Create Mailchimp User source
        api_response = api_instance.mailchimp_controller_action_load(mailchimp_connector_form=mailchimp_connector_form)
        print("The response of ConnectorsMailchimpApi->mailchimp_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMailchimpApi->mailchimp_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailchimp_connector_form** | [**MailchimpConnectorForm**](MailchimpConnectorForm.md)|  | [optional] 

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

# **mailchimp_controller_action_preview**
> SuccessResponse mailchimp_controller_action_preview(mailchimp_connector_form=mailchimp_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.mailchimp_connector_form import MailchimpConnectorForm
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
    api_instance = openapi_client.ConnectorsMailchimpApi(api_client)
    mailchimp_connector_form = openapi_client.MailchimpConnectorForm() # MailchimpConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.mailchimp_controller_action_preview(mailchimp_connector_form=mailchimp_connector_form)
        print("The response of ConnectorsMailchimpApi->mailchimp_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMailchimpApi->mailchimp_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailchimp_connector_form** | [**MailchimpConnectorForm**](MailchimpConnectorForm.md)|  | [optional] 

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

# **mailchimp_controller_action_template**
> object mailchimp_controller_action_template(id)

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
    api_instance = openapi_client.ConnectorsMailchimpApi(api_client)
    id = 'id_example' # str | The id of the template to retrieve

    try:
        # List details of dataset template
        api_response = api_instance.mailchimp_controller_action_template(id)
        print("The response of ConnectorsMailchimpApi->mailchimp_controller_action_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMailchimpApi->mailchimp_controller_action_template: %s\n" % e)
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

# **mailchimp_controller_action_templates**
> ConnectorTemplateResponse mailchimp_controller_action_templates()

List all Mailchimp dataset templates

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
    api_instance = openapi_client.ConnectorsMailchimpApi(api_client)

    try:
        # List all Mailchimp dataset templates
        api_response = api_instance.mailchimp_controller_action_templates()
        print("The response of ConnectorsMailchimpApi->mailchimp_controller_action_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMailchimpApi->mailchimp_controller_action_templates: %s\n" % e)
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
**200** | List all Mailchimp dataset templates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

