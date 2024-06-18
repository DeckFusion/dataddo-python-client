# openapi_client.ConnectorsFacebookLeadsApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**facebook_leads_controller_action_attribute**](ConnectorsFacebookLeadsApi.md#facebook_leads_controller_action_attribute) | **GET** /connectors/facebook_leads/actions/attribute | List of attributes
[**facebook_leads_controller_action_authorization**](ConnectorsFacebookLeadsApi.md#facebook_leads_controller_action_authorization) | **GET** /connectors/facebook_leads/actions/authorization | List of authorization objects
[**facebook_leads_controller_action_date_range**](ConnectorsFacebookLeadsApi.md#facebook_leads_controller_action_date_range) | **GET** /connectors/facebook_leads/actions/dateRange | Method for listing date range
[**facebook_leads_controller_action_form**](ConnectorsFacebookLeadsApi.md#facebook_leads_controller_action_form) | **POST** /connectors/facebook_leads/actions/form | List of lead forms
[**facebook_leads_controller_action_limit**](ConnectorsFacebookLeadsApi.md#facebook_leads_controller_action_limit) | **GET** /connectors/facebook_leads/actions/limit | List of lead limit options
[**facebook_leads_controller_action_load**](ConnectorsFacebookLeadsApi.md#facebook_leads_controller_action_load) | **POST** /connectors/facebook_leads/create-source | Create Facebook Leads source
[**facebook_leads_controller_action_page**](ConnectorsFacebookLeadsApi.md#facebook_leads_controller_action_page) | **POST** /connectors/facebook_leads/actions/page | List of pages
[**facebook_leads_controller_action_preview**](ConnectorsFacebookLeadsApi.md#facebook_leads_controller_action_preview) | **POST** /connectors/facebook_leads/preview | Preview the data


# **facebook_leads_controller_action_attribute**
> List[LabelValueResponseInner] facebook_leads_controller_action_attribute()

List of attributes

List all data labels

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
    api_instance = openapi_client.ConnectorsFacebookLeadsApi(api_client)

    try:
        # List of attributes
        api_response = api_instance.facebook_leads_controller_action_attribute()
        print("The response of ConnectorsFacebookLeadsApi->facebook_leads_controller_action_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookLeadsApi->facebook_leads_controller_action_attribute: %s\n" % e)
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
**200** | List of attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facebook_leads_controller_action_authorization**
> List[ActionAuthorizationResponseInner] facebook_leads_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsFacebookLeadsApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.facebook_leads_controller_action_authorization()
        print("The response of ConnectorsFacebookLeadsApi->facebook_leads_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookLeadsApi->facebook_leads_controller_action_authorization: %s\n" % e)
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

# **facebook_leads_controller_action_date_range**
> List[LabelValueResponseInner] facebook_leads_controller_action_date_range()

Method for listing date range

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
    api_instance = openapi_client.ConnectorsFacebookLeadsApi(api_client)

    try:
        # Method for listing date range
        api_response = api_instance.facebook_leads_controller_action_date_range()
        print("The response of ConnectorsFacebookLeadsApi->facebook_leads_controller_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookLeadsApi->facebook_leads_controller_action_date_range: %s\n" % e)
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
**200** | List of Facebook Leads date ranges |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facebook_leads_controller_action_form**
> List[LabelValueResponseInner] facebook_leads_controller_action_form(facebook_leads_controller_action_form_request=facebook_leads_controller_action_form_request)

List of lead forms

Prints all Facebook lead-collection forms associated with a particular page

### Example


```python
import openapi_client
from openapi_client.models.facebook_leads_controller_action_form_request import FacebookLeadsControllerActionFormRequest
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
    api_instance = openapi_client.ConnectorsFacebookLeadsApi(api_client)
    facebook_leads_controller_action_form_request = openapi_client.FacebookLeadsControllerActionFormRequest() # FacebookLeadsControllerActionFormRequest |  (optional)

    try:
        # List of lead forms
        api_response = api_instance.facebook_leads_controller_action_form(facebook_leads_controller_action_form_request=facebook_leads_controller_action_form_request)
        print("The response of ConnectorsFacebookLeadsApi->facebook_leads_controller_action_form:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookLeadsApi->facebook_leads_controller_action_form: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facebook_leads_controller_action_form_request** | [**FacebookLeadsControllerActionFormRequest**](FacebookLeadsControllerActionFormRequest.md)|  | [optional] 

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
**200** | List of lead forms |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facebook_leads_controller_action_limit**
> List[LabelValueResponseInner] facebook_leads_controller_action_limit()

List of lead limit options

List all post limit options

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
    api_instance = openapi_client.ConnectorsFacebookLeadsApi(api_client)

    try:
        # List of lead limit options
        api_response = api_instance.facebook_leads_controller_action_limit()
        print("The response of ConnectorsFacebookLeadsApi->facebook_leads_controller_action_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookLeadsApi->facebook_leads_controller_action_limit: %s\n" % e)
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
**200** | List of lead limit options |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facebook_leads_controller_action_load**
> Source facebook_leads_controller_action_load(facebook_leads_connector_form=facebook_leads_connector_form)

Create Facebook Leads source

### Example


```python
import openapi_client
from openapi_client.models.facebook_leads_connector_form import FacebookLeadsConnectorForm
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
    api_instance = openapi_client.ConnectorsFacebookLeadsApi(api_client)
    facebook_leads_connector_form = openapi_client.FacebookLeadsConnectorForm() # FacebookLeadsConnectorForm |  (optional)

    try:
        # Create Facebook Leads source
        api_response = api_instance.facebook_leads_controller_action_load(facebook_leads_connector_form=facebook_leads_connector_form)
        print("The response of ConnectorsFacebookLeadsApi->facebook_leads_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookLeadsApi->facebook_leads_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facebook_leads_connector_form** | [**FacebookLeadsConnectorForm**](FacebookLeadsConnectorForm.md)|  | [optional] 

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

# **facebook_leads_controller_action_page**
> List[LabelValueResponseInner] facebook_leads_controller_action_page(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List of pages

Prints all Facebook pages

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
    api_instance = openapi_client.ConnectorsFacebookLeadsApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List of pages
        api_response = api_instance.facebook_leads_controller_action_page(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsFacebookLeadsApi->facebook_leads_controller_action_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookLeadsApi->facebook_leads_controller_action_page: %s\n" % e)
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
**200** | List of pages |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **facebook_leads_controller_action_preview**
> SuccessResponse facebook_leads_controller_action_preview(facebook_leads_connector_form=facebook_leads_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.facebook_leads_connector_form import FacebookLeadsConnectorForm
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
    api_instance = openapi_client.ConnectorsFacebookLeadsApi(api_client)
    facebook_leads_connector_form = openapi_client.FacebookLeadsConnectorForm() # FacebookLeadsConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.facebook_leads_controller_action_preview(facebook_leads_connector_form=facebook_leads_connector_form)
        print("The response of ConnectorsFacebookLeadsApi->facebook_leads_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookLeadsApi->facebook_leads_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facebook_leads_connector_form** | [**FacebookLeadsConnectorForm**](FacebookLeadsConnectorForm.md)|  | [optional] 

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

