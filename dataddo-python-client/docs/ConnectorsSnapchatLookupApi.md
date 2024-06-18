# openapi_client.ConnectorsSnapchatLookupApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**snapchat_lookup_controller_action_account**](ConnectorsSnapchatLookupApi.md#snapchat_lookup_controller_action_account) | **POST** /connectors/snapchat_lookup/actions/account | List of accounts
[**snapchat_lookup_controller_action_attribute**](ConnectorsSnapchatLookupApi.md#snapchat_lookup_controller_action_attribute) | **POST** /connectors/snapchat_lookup/actions/attribute | List of attributes
[**snapchat_lookup_controller_action_authorization**](ConnectorsSnapchatLookupApi.md#snapchat_lookup_controller_action_authorization) | **GET** /connectors/snapchat_lookup/actions/authorization | List of authorization objects
[**snapchat_lookup_controller_action_level**](ConnectorsSnapchatLookupApi.md#snapchat_lookup_controller_action_level) | **GET** /connectors/snapchat_lookup/actions/level | List of levels
[**snapchat_lookup_controller_action_load**](ConnectorsSnapchatLookupApi.md#snapchat_lookup_controller_action_load) | **POST** /connectors/snapchat_lookup/create-source | Create Snapchat Lookup source
[**snapchat_lookup_controller_action_organization**](ConnectorsSnapchatLookupApi.md#snapchat_lookup_controller_action_organization) | **POST** /connectors/snapchat_lookup/actions/organization | List of organizations
[**snapchat_lookup_controller_action_preview**](ConnectorsSnapchatLookupApi.md#snapchat_lookup_controller_action_preview) | **POST** /connectors/snapchat_lookup/preview | Preview the data


# **snapchat_lookup_controller_action_account**
> List[LabelValueResponseInner] snapchat_lookup_controller_action_account(snapchat_lookup_controller_action_account_request=snapchat_lookup_controller_action_account_request)

List of accounts

List all AdAccount IDs

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.snapchat_lookup_controller_action_account_request import SnapchatLookupControllerActionAccountRequest
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
    api_instance = openapi_client.ConnectorsSnapchatLookupApi(api_client)
    snapchat_lookup_controller_action_account_request = openapi_client.SnapchatLookupControllerActionAccountRequest() # SnapchatLookupControllerActionAccountRequest |  (optional)

    try:
        # List of accounts
        api_response = api_instance.snapchat_lookup_controller_action_account(snapchat_lookup_controller_action_account_request=snapchat_lookup_controller_action_account_request)
        print("The response of ConnectorsSnapchatLookupApi->snapchat_lookup_controller_action_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSnapchatLookupApi->snapchat_lookup_controller_action_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapchat_lookup_controller_action_account_request** | [**SnapchatLookupControllerActionAccountRequest**](SnapchatLookupControllerActionAccountRequest.md)|  | [optional] 

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
**200** | List of accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapchat_lookup_controller_action_attribute**
> List[LabelValueResponseInner] snapchat_lookup_controller_action_attribute(snapchat_lookup_controller_action_attribute_request=snapchat_lookup_controller_action_attribute_request)

List of attributes

Method for listing attributes

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.snapchat_lookup_controller_action_attribute_request import SnapchatLookupControllerActionAttributeRequest
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
    api_instance = openapi_client.ConnectorsSnapchatLookupApi(api_client)
    snapchat_lookup_controller_action_attribute_request = openapi_client.SnapchatLookupControllerActionAttributeRequest() # SnapchatLookupControllerActionAttributeRequest |  (optional)

    try:
        # List of attributes
        api_response = api_instance.snapchat_lookup_controller_action_attribute(snapchat_lookup_controller_action_attribute_request=snapchat_lookup_controller_action_attribute_request)
        print("The response of ConnectorsSnapchatLookupApi->snapchat_lookup_controller_action_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSnapchatLookupApi->snapchat_lookup_controller_action_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapchat_lookup_controller_action_attribute_request** | [**SnapchatLookupControllerActionAttributeRequest**](SnapchatLookupControllerActionAttributeRequest.md)|  | [optional] 

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
**200** | List of accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapchat_lookup_controller_action_authorization**
> List[ActionAuthorizationResponseInner] snapchat_lookup_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsSnapchatLookupApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.snapchat_lookup_controller_action_authorization()
        print("The response of ConnectorsSnapchatLookupApi->snapchat_lookup_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSnapchatLookupApi->snapchat_lookup_controller_action_authorization: %s\n" % e)
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

# **snapchat_lookup_controller_action_level**
> List[LabelValueResponseInner] snapchat_lookup_controller_action_level()

List of levels

Method for listing levels

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
    api_instance = openapi_client.ConnectorsSnapchatLookupApi(api_client)

    try:
        # List of levels
        api_response = api_instance.snapchat_lookup_controller_action_level()
        print("The response of ConnectorsSnapchatLookupApi->snapchat_lookup_controller_action_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSnapchatLookupApi->snapchat_lookup_controller_action_level: %s\n" % e)
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
**200** | List of level objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapchat_lookup_controller_action_load**
> Source snapchat_lookup_controller_action_load(snapchat_lookup_connector_form=snapchat_lookup_connector_form)

Create Snapchat Lookup source

### Example


```python
import openapi_client
from openapi_client.models.snapchat_lookup_connector_form import SnapchatLookupConnectorForm
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
    api_instance = openapi_client.ConnectorsSnapchatLookupApi(api_client)
    snapchat_lookup_connector_form = openapi_client.SnapchatLookupConnectorForm() # SnapchatLookupConnectorForm |  (optional)

    try:
        # Create Snapchat Lookup source
        api_response = api_instance.snapchat_lookup_controller_action_load(snapchat_lookup_connector_form=snapchat_lookup_connector_form)
        print("The response of ConnectorsSnapchatLookupApi->snapchat_lookup_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSnapchatLookupApi->snapchat_lookup_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapchat_lookup_connector_form** | [**SnapchatLookupConnectorForm**](SnapchatLookupConnectorForm.md)|  | [optional] 

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

# **snapchat_lookup_controller_action_organization**
> List[LabelValueResponseInner] snapchat_lookup_controller_action_organization(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List of organizations

List all the Organization IDs

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
    api_instance = openapi_client.ConnectorsSnapchatLookupApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List of organizations
        api_response = api_instance.snapchat_lookup_controller_action_organization(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsSnapchatLookupApi->snapchat_lookup_controller_action_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSnapchatLookupApi->snapchat_lookup_controller_action_organization: %s\n" % e)
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
**200** | List of organizations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapchat_lookup_controller_action_preview**
> SuccessResponse snapchat_lookup_controller_action_preview(snapchat_lookup_connector_form=snapchat_lookup_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.snapchat_lookup_connector_form import SnapchatLookupConnectorForm
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
    api_instance = openapi_client.ConnectorsSnapchatLookupApi(api_client)
    snapchat_lookup_connector_form = openapi_client.SnapchatLookupConnectorForm() # SnapchatLookupConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.snapchat_lookup_controller_action_preview(snapchat_lookup_connector_form=snapchat_lookup_connector_form)
        print("The response of ConnectorsSnapchatLookupApi->snapchat_lookup_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSnapchatLookupApi->snapchat_lookup_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapchat_lookup_connector_form** | [**SnapchatLookupConnectorForm**](SnapchatLookupConnectorForm.md)|  | [optional] 

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

