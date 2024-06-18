# openapi_client.ConnectorsInstagramUserApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instagram_user_controller_action_account**](ConnectorsInstagramUserApi.md#instagram_user_controller_action_account) | **POST** /connectors/instagram_user/actions/account | List of accounts
[**instagram_user_controller_action_attribute**](ConnectorsInstagramUserApi.md#instagram_user_controller_action_attribute) | **GET** /connectors/instagram_user/actions/attribute | List of attributes
[**instagram_user_controller_action_authorization**](ConnectorsInstagramUserApi.md#instagram_user_controller_action_authorization) | **GET** /connectors/instagram_user/actions/authorization | List of authorization objects
[**instagram_user_controller_action_date_range**](ConnectorsInstagramUserApi.md#instagram_user_controller_action_date_range) | **GET** /connectors/instagram_user/actions/dateRange | List of date ranges
[**instagram_user_controller_action_load**](ConnectorsInstagramUserApi.md#instagram_user_controller_action_load) | **POST** /connectors/instagram_user/create-source | Create Instagram User source
[**instagram_user_controller_action_preview**](ConnectorsInstagramUserApi.md#instagram_user_controller_action_preview) | **POST** /connectors/instagram_user/preview | Preview the data


# **instagram_user_controller_action_account**
> List[LabelValueResponseInner] instagram_user_controller_action_account(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

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
    api_instance = openapi_client.ConnectorsInstagramUserApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List of accounts
        api_response = api_instance.instagram_user_controller_action_account(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsInstagramUserApi->instagram_user_controller_action_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsInstagramUserApi->instagram_user_controller_action_account: %s\n" % e)
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

# **instagram_user_controller_action_attribute**
> List[LabelValueResponseInner] instagram_user_controller_action_attribute()

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
    api_instance = openapi_client.ConnectorsInstagramUserApi(api_client)

    try:
        # List of attributes
        api_response = api_instance.instagram_user_controller_action_attribute()
        print("The response of ConnectorsInstagramUserApi->instagram_user_controller_action_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsInstagramUserApi->instagram_user_controller_action_attribute: %s\n" % e)
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

# **instagram_user_controller_action_authorization**
> List[ActionAuthorizationResponseInner] instagram_user_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsInstagramUserApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.instagram_user_controller_action_authorization()
        print("The response of ConnectorsInstagramUserApi->instagram_user_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsInstagramUserApi->instagram_user_controller_action_authorization: %s\n" % e)
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

# **instagram_user_controller_action_date_range**
> List[LabelValueResponseInner] instagram_user_controller_action_date_range()

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
    api_instance = openapi_client.ConnectorsInstagramUserApi(api_client)

    try:
        # List of date ranges
        api_response = api_instance.instagram_user_controller_action_date_range()
        print("The response of ConnectorsInstagramUserApi->instagram_user_controller_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsInstagramUserApi->instagram_user_controller_action_date_range: %s\n" % e)
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

# **instagram_user_controller_action_load**
> Source instagram_user_controller_action_load(instagram_user_connector_form=instagram_user_connector_form)

Create Instagram User source

### Example


```python
import openapi_client
from openapi_client.models.instagram_user_connector_form import InstagramUserConnectorForm
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
    api_instance = openapi_client.ConnectorsInstagramUserApi(api_client)
    instagram_user_connector_form = openapi_client.InstagramUserConnectorForm() # InstagramUserConnectorForm |  (optional)

    try:
        # Create Instagram User source
        api_response = api_instance.instagram_user_controller_action_load(instagram_user_connector_form=instagram_user_connector_form)
        print("The response of ConnectorsInstagramUserApi->instagram_user_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsInstagramUserApi->instagram_user_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instagram_user_connector_form** | [**InstagramUserConnectorForm**](InstagramUserConnectorForm.md)|  | [optional] 

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

# **instagram_user_controller_action_preview**
> SuccessResponse instagram_user_controller_action_preview(instagram_user_connector_form=instagram_user_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.instagram_user_connector_form import InstagramUserConnectorForm
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
    api_instance = openapi_client.ConnectorsInstagramUserApi(api_client)
    instagram_user_connector_form = openapi_client.InstagramUserConnectorForm() # InstagramUserConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.instagram_user_controller_action_preview(instagram_user_connector_form=instagram_user_connector_form)
        print("The response of ConnectorsInstagramUserApi->instagram_user_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsInstagramUserApi->instagram_user_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instagram_user_connector_form** | [**InstagramUserConnectorForm**](InstagramUserConnectorForm.md)|  | [optional] 

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

