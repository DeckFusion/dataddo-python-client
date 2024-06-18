# openapi_client.ConnectorsInstagramMediaApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instagram_media_controller_action_account**](ConnectorsInstagramMediaApi.md#instagram_media_controller_action_account) | **POST** /connectors/instagram_media/actions/account | List of accounts
[**instagram_media_controller_action_attribute**](ConnectorsInstagramMediaApi.md#instagram_media_controller_action_attribute) | **GET** /connectors/instagram_media/actions/attribute | List of attributes
[**instagram_media_controller_action_authorization**](ConnectorsInstagramMediaApi.md#instagram_media_controller_action_authorization) | **GET** /connectors/instagram_media/actions/authorization | List of authorization objects
[**instagram_media_controller_action_load**](ConnectorsInstagramMediaApi.md#instagram_media_controller_action_load) | **POST** /connectors/instagram_media/create-source | Create Instagram Media source
[**instagram_media_controller_action_preview**](ConnectorsInstagramMediaApi.md#instagram_media_controller_action_preview) | **POST** /connectors/instagram_media/preview | Preview the data


# **instagram_media_controller_action_account**
> List[LabelValueResponseInner] instagram_media_controller_action_account(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List of accounts

Prints all Instagram Media

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
    api_instance = openapi_client.ConnectorsInstagramMediaApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List of accounts
        api_response = api_instance.instagram_media_controller_action_account(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsInstagramMediaApi->instagram_media_controller_action_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsInstagramMediaApi->instagram_media_controller_action_account: %s\n" % e)
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
**200** | List of accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instagram_media_controller_action_attribute**
> List[LabelValueResponseInner] instagram_media_controller_action_attribute()

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
    api_instance = openapi_client.ConnectorsInstagramMediaApi(api_client)

    try:
        # List of attributes
        api_response = api_instance.instagram_media_controller_action_attribute()
        print("The response of ConnectorsInstagramMediaApi->instagram_media_controller_action_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsInstagramMediaApi->instagram_media_controller_action_attribute: %s\n" % e)
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
**200** | List of attribute objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instagram_media_controller_action_authorization**
> List[ActionAuthorizationResponseInner] instagram_media_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsInstagramMediaApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.instagram_media_controller_action_authorization()
        print("The response of ConnectorsInstagramMediaApi->instagram_media_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsInstagramMediaApi->instagram_media_controller_action_authorization: %s\n" % e)
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

# **instagram_media_controller_action_load**
> Source instagram_media_controller_action_load(instagram_media_connector_form=instagram_media_connector_form)

Create Instagram Media source

### Example


```python
import openapi_client
from openapi_client.models.instagram_media_connector_form import InstagramMediaConnectorForm
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
    api_instance = openapi_client.ConnectorsInstagramMediaApi(api_client)
    instagram_media_connector_form = openapi_client.InstagramMediaConnectorForm() # InstagramMediaConnectorForm |  (optional)

    try:
        # Create Instagram Media source
        api_response = api_instance.instagram_media_controller_action_load(instagram_media_connector_form=instagram_media_connector_form)
        print("The response of ConnectorsInstagramMediaApi->instagram_media_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsInstagramMediaApi->instagram_media_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instagram_media_connector_form** | [**InstagramMediaConnectorForm**](InstagramMediaConnectorForm.md)|  | [optional] 

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

# **instagram_media_controller_action_preview**
> SuccessResponse instagram_media_controller_action_preview(instagram_media_connector_form=instagram_media_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.instagram_media_connector_form import InstagramMediaConnectorForm
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
    api_instance = openapi_client.ConnectorsInstagramMediaApi(api_client)
    instagram_media_connector_form = openapi_client.InstagramMediaConnectorForm() # InstagramMediaConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.instagram_media_controller_action_preview(instagram_media_connector_form=instagram_media_connector_form)
        print("The response of ConnectorsInstagramMediaApi->instagram_media_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsInstagramMediaApi->instagram_media_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instagram_media_connector_form** | [**InstagramMediaConnectorForm**](InstagramMediaConnectorForm.md)|  | [optional] 

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

