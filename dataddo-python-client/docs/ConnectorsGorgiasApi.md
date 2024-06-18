# openapi_client.ConnectorsGorgiasApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gorgias_controller_action_authorization**](ConnectorsGorgiasApi.md#gorgias_controller_action_authorization) | **GET** /connectors/gorgias/actions/authorization | List of authorization objects
[**gorgias_controller_action_load**](ConnectorsGorgiasApi.md#gorgias_controller_action_load) | **POST** /connectors/gorgias/create-source | Create Gorgias  source
[**gorgias_controller_action_preview**](ConnectorsGorgiasApi.md#gorgias_controller_action_preview) | **POST** /connectors/gorgias/preview | Preview the data
[**gorgias_controller_action_subdomain**](ConnectorsGorgiasApi.md#gorgias_controller_action_subdomain) | **POST** /connectors/gorgias/actions/subdomain | List of all subdomains
[**gorgias_controller_action_template**](ConnectorsGorgiasApi.md#gorgias_controller_action_template) | **GET** /connectors/gorgias/templates/{id} | List details of dataset template
[**gorgias_controller_action_templates**](ConnectorsGorgiasApi.md#gorgias_controller_action_templates) | **GET** /connectors/gorgias/templates | List all Gorgias dataset templates


# **gorgias_controller_action_authorization**
> List[ActionAuthorizationResponseInner] gorgias_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsGorgiasApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.gorgias_controller_action_authorization()
        print("The response of ConnectorsGorgiasApi->gorgias_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGorgiasApi->gorgias_controller_action_authorization: %s\n" % e)
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

# **gorgias_controller_action_load**
> Source gorgias_controller_action_load(gorgias_connector_form=gorgias_connector_form)

Create Gorgias  source

### Example


```python
import openapi_client
from openapi_client.models.gorgias_connector_form import GorgiasConnectorForm
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
    api_instance = openapi_client.ConnectorsGorgiasApi(api_client)
    gorgias_connector_form = openapi_client.GorgiasConnectorForm() # GorgiasConnectorForm |  (optional)

    try:
        # Create Gorgias  source
        api_response = api_instance.gorgias_controller_action_load(gorgias_connector_form=gorgias_connector_form)
        print("The response of ConnectorsGorgiasApi->gorgias_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGorgiasApi->gorgias_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gorgias_connector_form** | [**GorgiasConnectorForm**](GorgiasConnectorForm.md)|  | [optional] 

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

# **gorgias_controller_action_preview**
> SuccessResponse gorgias_controller_action_preview(gorgias_connector_form=gorgias_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.gorgias_connector_form import GorgiasConnectorForm
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
    api_instance = openapi_client.ConnectorsGorgiasApi(api_client)
    gorgias_connector_form = openapi_client.GorgiasConnectorForm() # GorgiasConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.gorgias_controller_action_preview(gorgias_connector_form=gorgias_connector_form)
        print("The response of ConnectorsGorgiasApi->gorgias_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGorgiasApi->gorgias_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gorgias_connector_form** | [**GorgiasConnectorForm**](GorgiasConnectorForm.md)|  | [optional] 

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

# **gorgias_controller_action_subdomain**
> List[LabelValueResponseInner] gorgias_controller_action_subdomain(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List of all subdomains

Method for listing Gorgias subdomain

### Example


```python
import openapi_client
from openapi_client.models.amazon_ads_controller_action_profile_request_value import AmazonAdsControllerActionProfileRequestValue
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
    api_instance = openapi_client.ConnectorsGorgiasApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List of all subdomains
        api_response = api_instance.gorgias_controller_action_subdomain(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsGorgiasApi->gorgias_controller_action_subdomain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGorgiasApi->gorgias_controller_action_subdomain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_ads_controller_action_profile_request_value** | [**AmazonAdsControllerActionProfileRequestValue**](AmazonAdsControllerActionProfileRequestValue.md)|  | [optional] 

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
**200** | List of subdomains |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gorgias_controller_action_template**
> object gorgias_controller_action_template(id)

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
    api_instance = openapi_client.ConnectorsGorgiasApi(api_client)
    id = 'id_example' # str | The id of the template to retrieve

    try:
        # List details of dataset template
        api_response = api_instance.gorgias_controller_action_template(id)
        print("The response of ConnectorsGorgiasApi->gorgias_controller_action_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGorgiasApi->gorgias_controller_action_template: %s\n" % e)
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

# **gorgias_controller_action_templates**
> ConnectorTemplateResponse gorgias_controller_action_templates()

List all Gorgias dataset templates

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
    api_instance = openapi_client.ConnectorsGorgiasApi(api_client)

    try:
        # List all Gorgias dataset templates
        api_response = api_instance.gorgias_controller_action_templates()
        print("The response of ConnectorsGorgiasApi->gorgias_controller_action_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGorgiasApi->gorgias_controller_action_templates: %s\n" % e)
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
**200** | List all Gorgias dataset templates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

