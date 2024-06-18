# openapi_client.ConnectorsSalesforceApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesforce_controller_action_api_version**](ConnectorsSalesforceApi.md#salesforce_controller_action_api_version) | **POST** /connectors/salesforce/actions/apiVersion | List available API versions
[**salesforce_controller_action_attribute**](ConnectorsSalesforceApi.md#salesforce_controller_action_attribute) | **POST** /connectors/salesforce/actions/attribute | Gets all available data extensions attributes
[**salesforce_controller_action_authorization**](ConnectorsSalesforceApi.md#salesforce_controller_action_authorization) | **GET** /connectors/salesforce/actions/authorization | List of authorization objects
[**salesforce_controller_action_instance**](ConnectorsSalesforceApi.md#salesforce_controller_action_instance) | **POST** /connectors/salesforce/actions/instance | List all available instance It is possible to use centralized authentication server (login.salesforce.com) even if custom domain is used
[**salesforce_controller_action_load**](ConnectorsSalesforceApi.md#salesforce_controller_action_load) | **POST** /connectors/salesforce/create-source | Create Salesforce source
[**salesforce_controller_action_object**](ConnectorsSalesforceApi.md#salesforce_controller_action_object) | **POST** /connectors/salesforce/actions/object | Gets all Marketing cloud data extensions
[**salesforce_controller_action_preview**](ConnectorsSalesforceApi.md#salesforce_controller_action_preview) | **POST** /connectors/salesforce/preview | Preview the data


# **salesforce_controller_action_api_version**
> List[LabelValueResponseInner] salesforce_controller_action_api_version(salesforce_controller_action_api_version_request=salesforce_controller_action_api_version_request)

List available API versions

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.salesforce_controller_action_api_version_request import SalesforceControllerActionApiVersionRequest
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
    api_instance = openapi_client.ConnectorsSalesforceApi(api_client)
    salesforce_controller_action_api_version_request = openapi_client.SalesforceControllerActionApiVersionRequest() # SalesforceControllerActionApiVersionRequest |  (optional)

    try:
        # List available API versions
        api_response = api_instance.salesforce_controller_action_api_version(salesforce_controller_action_api_version_request=salesforce_controller_action_api_version_request)
        print("The response of ConnectorsSalesforceApi->salesforce_controller_action_api_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSalesforceApi->salesforce_controller_action_api_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **salesforce_controller_action_api_version_request** | [**SalesforceControllerActionApiVersionRequest**](SalesforceControllerActionApiVersionRequest.md)|  | [optional] 

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
**200** | List of Salesforce API Versions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **salesforce_controller_action_attribute**
> List[LabelValueResponseInner] salesforce_controller_action_attribute(salesforce_controller_action_attribute_request=salesforce_controller_action_attribute_request)

Gets all available data extensions attributes

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.salesforce_controller_action_attribute_request import SalesforceControllerActionAttributeRequest
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
    api_instance = openapi_client.ConnectorsSalesforceApi(api_client)
    salesforce_controller_action_attribute_request = openapi_client.SalesforceControllerActionAttributeRequest() # SalesforceControllerActionAttributeRequest |  (optional)

    try:
        # Gets all available data extensions attributes
        api_response = api_instance.salesforce_controller_action_attribute(salesforce_controller_action_attribute_request=salesforce_controller_action_attribute_request)
        print("The response of ConnectorsSalesforceApi->salesforce_controller_action_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSalesforceApi->salesforce_controller_action_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **salesforce_controller_action_attribute_request** | [**SalesforceControllerActionAttributeRequest**](SalesforceControllerActionAttributeRequest.md)|  | [optional] 

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
**200** | List of Salesforce attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **salesforce_controller_action_authorization**
> List[ActionAuthorizationResponseInner] salesforce_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsSalesforceApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.salesforce_controller_action_authorization()
        print("The response of ConnectorsSalesforceApi->salesforce_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSalesforceApi->salesforce_controller_action_authorization: %s\n" % e)
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

# **salesforce_controller_action_instance**
> List[LabelValueResponseInner] salesforce_controller_action_instance(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List all available instance It is possible to use centralized authentication server (login.salesforce.com) even if custom domain is used

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
    api_instance = openapi_client.ConnectorsSalesforceApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List all available instance It is possible to use centralized authentication server (login.salesforce.com) even if custom domain is used
        api_response = api_instance.salesforce_controller_action_instance(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsSalesforceApi->salesforce_controller_action_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSalesforceApi->salesforce_controller_action_instance: %s\n" % e)
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
**200** | List of Salesforce instances |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **salesforce_controller_action_load**
> Source salesforce_controller_action_load(salesforce_connector_form=salesforce_connector_form)

Create Salesforce source

### Example


```python
import openapi_client
from openapi_client.models.salesforce_connector_form import SalesforceConnectorForm
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
    api_instance = openapi_client.ConnectorsSalesforceApi(api_client)
    salesforce_connector_form = openapi_client.SalesforceConnectorForm() # SalesforceConnectorForm |  (optional)

    try:
        # Create Salesforce source
        api_response = api_instance.salesforce_controller_action_load(salesforce_connector_form=salesforce_connector_form)
        print("The response of ConnectorsSalesforceApi->salesforce_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSalesforceApi->salesforce_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **salesforce_connector_form** | [**SalesforceConnectorForm**](SalesforceConnectorForm.md)|  | [optional] 

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

# **salesforce_controller_action_object**
> List[LabelValueResponseInner] salesforce_controller_action_object(salesforce_controller_action_object_request=salesforce_controller_action_object_request)

Gets all Marketing cloud data extensions

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.salesforce_controller_action_object_request import SalesforceControllerActionObjectRequest
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
    api_instance = openapi_client.ConnectorsSalesforceApi(api_client)
    salesforce_controller_action_object_request = openapi_client.SalesforceControllerActionObjectRequest() # SalesforceControllerActionObjectRequest |  (optional)

    try:
        # Gets all Marketing cloud data extensions
        api_response = api_instance.salesforce_controller_action_object(salesforce_controller_action_object_request=salesforce_controller_action_object_request)
        print("The response of ConnectorsSalesforceApi->salesforce_controller_action_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSalesforceApi->salesforce_controller_action_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **salesforce_controller_action_object_request** | [**SalesforceControllerActionObjectRequest**](SalesforceControllerActionObjectRequest.md)|  | [optional] 

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
**200** | List of Salesforce objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **salesforce_controller_action_preview**
> SuccessResponse salesforce_controller_action_preview(salesforce_connector_form=salesforce_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.salesforce_connector_form import SalesforceConnectorForm
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
    api_instance = openapi_client.ConnectorsSalesforceApi(api_client)
    salesforce_connector_form = openapi_client.SalesforceConnectorForm() # SalesforceConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.salesforce_controller_action_preview(salesforce_connector_form=salesforce_connector_form)
        print("The response of ConnectorsSalesforceApi->salesforce_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSalesforceApi->salesforce_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **salesforce_connector_form** | [**SalesforceConnectorForm**](SalesforceConnectorForm.md)|  | [optional] 

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

