# openapi_client.ConnectorsNetsuiteApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_netsuite_netsuite_connector_action_attributes**](ConnectorsNetsuiteApi.md#app_connector_netsuite_netsuite_connector_action_attributes) | **POST** /connectors/netsuite/actions/attributes | List all attributes for the given object
[**app_connector_netsuite_netsuite_connector_action_authorization**](ConnectorsNetsuiteApi.md#app_connector_netsuite_netsuite_connector_action_authorization) | **GET** /connectors/netsuite/actions/authorization | List of authorization objects
[**app_connector_netsuite_netsuite_connector_action_object**](ConnectorsNetsuiteApi.md#app_connector_netsuite_netsuite_connector_action_object) | **POST** /connectors/netsuite/actions/object | Get Netsuite objects
[**app_connector_netsuite_netsuite_connector_create_source**](ConnectorsNetsuiteApi.md#app_connector_netsuite_netsuite_connector_create_source) | **POST** /connectors/netsuite/create-source | Create Netsuite source
[**app_connector_netsuite_netsuite_connector_preview**](ConnectorsNetsuiteApi.md#app_connector_netsuite_netsuite_connector_preview) | **POST** /connectors/netsuite/preview | Data preview


# **app_connector_netsuite_netsuite_connector_action_attributes**
> List[LabelValueResponseInner] app_connector_netsuite_netsuite_connector_action_attributes(app_connector_netsuite_netsuite_connector_action_attributes_request=app_connector_netsuite_netsuite_connector_action_attributes_request)

List all attributes for the given object

### Example


```python
import openapi_client
from openapi_client.models.app_connector_netsuite_netsuite_connector_action_attributes_request import AppConnectorNetsuiteNetsuiteConnectorActionAttributesRequest
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
    api_instance = openapi_client.ConnectorsNetsuiteApi(api_client)
    app_connector_netsuite_netsuite_connector_action_attributes_request = openapi_client.AppConnectorNetsuiteNetsuiteConnectorActionAttributesRequest() # AppConnectorNetsuiteNetsuiteConnectorActionAttributesRequest |  (optional)

    try:
        # List all attributes for the given object
        api_response = api_instance.app_connector_netsuite_netsuite_connector_action_attributes(app_connector_netsuite_netsuite_connector_action_attributes_request=app_connector_netsuite_netsuite_connector_action_attributes_request)
        print("The response of ConnectorsNetsuiteApi->app_connector_netsuite_netsuite_connector_action_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsNetsuiteApi->app_connector_netsuite_netsuite_connector_action_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_connector_netsuite_netsuite_connector_action_attributes_request** | [**AppConnectorNetsuiteNetsuiteConnectorActionAttributesRequest**](AppConnectorNetsuiteNetsuiteConnectorActionAttributesRequest.md)|  | [optional] 

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
**200** | List of Netsuite attributes for a given object |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_netsuite_netsuite_connector_action_authorization**
> List[ActionAuthorizationResponseInner] app_connector_netsuite_netsuite_connector_action_authorization()

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
    api_instance = openapi_client.ConnectorsNetsuiteApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_connector_netsuite_netsuite_connector_action_authorization()
        print("The response of ConnectorsNetsuiteApi->app_connector_netsuite_netsuite_connector_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsNetsuiteApi->app_connector_netsuite_netsuite_connector_action_authorization: %s\n" % e)
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

# **app_connector_netsuite_netsuite_connector_action_object**
> List[LabelValueResponseInner] app_connector_netsuite_netsuite_connector_action_object(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

Get Netsuite objects

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
    api_instance = openapi_client.ConnectorsNetsuiteApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # Get Netsuite objects
        api_response = api_instance.app_connector_netsuite_netsuite_connector_action_object(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsNetsuiteApi->app_connector_netsuite_netsuite_connector_action_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsNetsuiteApi->app_connector_netsuite_netsuite_connector_action_object: %s\n" % e)
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
**200** | List of Netsuite reporting objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_netsuite_netsuite_connector_create_source**
> Source app_connector_netsuite_netsuite_connector_create_source(netsuite_dto=netsuite_dto)

Create Netsuite source

### Example


```python
import openapi_client
from openapi_client.models.netsuite_dto import NetsuiteDto
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
    api_instance = openapi_client.ConnectorsNetsuiteApi(api_client)
    netsuite_dto = openapi_client.NetsuiteDto() # NetsuiteDto |  (optional)

    try:
        # Create Netsuite source
        api_response = api_instance.app_connector_netsuite_netsuite_connector_create_source(netsuite_dto=netsuite_dto)
        print("The response of ConnectorsNetsuiteApi->app_connector_netsuite_netsuite_connector_create_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsNetsuiteApi->app_connector_netsuite_netsuite_connector_create_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **netsuite_dto** | [**NetsuiteDto**](NetsuiteDto.md)|  | [optional] 

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

# **app_connector_netsuite_netsuite_connector_preview**
> SuccessResponse app_connector_netsuite_netsuite_connector_preview(netsuite_dto=netsuite_dto)

Data preview

### Example


```python
import openapi_client
from openapi_client.models.netsuite_dto import NetsuiteDto
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
    api_instance = openapi_client.ConnectorsNetsuiteApi(api_client)
    netsuite_dto = openapi_client.NetsuiteDto() # NetsuiteDto |  (optional)

    try:
        # Data preview
        api_response = api_instance.app_connector_netsuite_netsuite_connector_preview(netsuite_dto=netsuite_dto)
        print("The response of ConnectorsNetsuiteApi->app_connector_netsuite_netsuite_connector_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsNetsuiteApi->app_connector_netsuite_netsuite_connector_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **netsuite_dto** | [**NetsuiteDto**](NetsuiteDto.md)|  | [optional] 

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

