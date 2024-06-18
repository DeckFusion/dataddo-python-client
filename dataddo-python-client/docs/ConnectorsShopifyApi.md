# openapi_client.ConnectorsShopifyApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_shopify_shopify_connector_action_authorization**](ConnectorsShopifyApi.md#app_connector_shopify_shopify_connector_action_authorization) | **GET** /connectors/shopify/actions/authorization | List of authorization objects
[**app_connector_shopify_shopify_connector_action_date_range**](ConnectorsShopifyApi.md#app_connector_shopify_shopify_connector_action_date_range) | **GET** /connectors/shopify/actions/dateRange | Method for listing date range
[**app_connector_shopify_shopify_connector_action_shop**](ConnectorsShopifyApi.md#app_connector_shopify_shopify_connector_action_shop) | **POST** /connectors/shopify/actions/shop | List all Shopify shops
[**app_connector_shopify_shopify_connector_action_template**](ConnectorsShopifyApi.md#app_connector_shopify_shopify_connector_action_template) | **GET** /connectors/shopify/templates/{id} | List details of dataset template
[**app_connector_shopify_shopify_connector_action_templates**](ConnectorsShopifyApi.md#app_connector_shopify_shopify_connector_action_templates) | **GET** /connectors/shopify/templates | List all Shopify dataset templates
[**app_connector_shopify_shopify_connector_create_source**](ConnectorsShopifyApi.md#app_connector_shopify_shopify_connector_create_source) | **POST** /connectors/shopify/create-source | Create Shopify source
[**app_connector_shopify_shopify_connector_preview**](ConnectorsShopifyApi.md#app_connector_shopify_shopify_connector_preview) | **POST** /connectors/shopify/preview | Data preview


# **app_connector_shopify_shopify_connector_action_authorization**
> List[ActionAuthorizationResponseInner] app_connector_shopify_shopify_connector_action_authorization()

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
    api_instance = openapi_client.ConnectorsShopifyApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_connector_shopify_shopify_connector_action_authorization()
        print("The response of ConnectorsShopifyApi->app_connector_shopify_shopify_connector_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsShopifyApi->app_connector_shopify_shopify_connector_action_authorization: %s\n" % e)
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

# **app_connector_shopify_shopify_connector_action_date_range**
> List[LabelValueResponseInner] app_connector_shopify_shopify_connector_action_date_range()

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
    api_instance = openapi_client.ConnectorsShopifyApi(api_client)

    try:
        # Method for listing date range
        api_response = api_instance.app_connector_shopify_shopify_connector_action_date_range()
        print("The response of ConnectorsShopifyApi->app_connector_shopify_shopify_connector_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsShopifyApi->app_connector_shopify_shopify_connector_action_date_range: %s\n" % e)
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
**200** | List of Shopify date ranges |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_shopify_shopify_connector_action_shop**
> List[LabelValueResponseInner] app_connector_shopify_shopify_connector_action_shop(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List all Shopify shops

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
    api_instance = openapi_client.ConnectorsShopifyApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List all Shopify shops
        api_response = api_instance.app_connector_shopify_shopify_connector_action_shop(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsShopifyApi->app_connector_shopify_shopify_connector_action_shop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsShopifyApi->app_connector_shopify_shopify_connector_action_shop: %s\n" % e)
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
**200** | List of shops |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_shopify_shopify_connector_action_template**
> object app_connector_shopify_shopify_connector_action_template(id)

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
    api_instance = openapi_client.ConnectorsShopifyApi(api_client)
    id = 'id_example' # str | The id of the template to retrieve

    try:
        # List details of dataset template
        api_response = api_instance.app_connector_shopify_shopify_connector_action_template(id)
        print("The response of ConnectorsShopifyApi->app_connector_shopify_shopify_connector_action_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsShopifyApi->app_connector_shopify_shopify_connector_action_template: %s\n" % e)
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

# **app_connector_shopify_shopify_connector_action_templates**
> ConnectorTemplateResponse app_connector_shopify_shopify_connector_action_templates()

List all Shopify dataset templates

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
    api_instance = openapi_client.ConnectorsShopifyApi(api_client)

    try:
        # List all Shopify dataset templates
        api_response = api_instance.app_connector_shopify_shopify_connector_action_templates()
        print("The response of ConnectorsShopifyApi->app_connector_shopify_shopify_connector_action_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsShopifyApi->app_connector_shopify_shopify_connector_action_templates: %s\n" % e)
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
**200** | List all Shopify dataset templates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_shopify_shopify_connector_create_source**
> Source app_connector_shopify_shopify_connector_create_source(shopify_dto=shopify_dto)

Create Shopify source

### Example


```python
import openapi_client
from openapi_client.models.shopify_dto import ShopifyDto
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
    api_instance = openapi_client.ConnectorsShopifyApi(api_client)
    shopify_dto = openapi_client.ShopifyDto() # ShopifyDto |  (optional)

    try:
        # Create Shopify source
        api_response = api_instance.app_connector_shopify_shopify_connector_create_source(shopify_dto=shopify_dto)
        print("The response of ConnectorsShopifyApi->app_connector_shopify_shopify_connector_create_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsShopifyApi->app_connector_shopify_shopify_connector_create_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shopify_dto** | [**ShopifyDto**](ShopifyDto.md)|  | [optional] 

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

# **app_connector_shopify_shopify_connector_preview**
> SuccessResponse app_connector_shopify_shopify_connector_preview(shopify_dto=shopify_dto)

Data preview

### Example


```python
import openapi_client
from openapi_client.models.shopify_dto import ShopifyDto
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
    api_instance = openapi_client.ConnectorsShopifyApi(api_client)
    shopify_dto = openapi_client.ShopifyDto() # ShopifyDto |  (optional)

    try:
        # Data preview
        api_response = api_instance.app_connector_shopify_shopify_connector_preview(shopify_dto=shopify_dto)
        print("The response of ConnectorsShopifyApi->app_connector_shopify_shopify_connector_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsShopifyApi->app_connector_shopify_shopify_connector_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shopify_dto** | [**ShopifyDto**](ShopifyDto.md)|  | [optional] 

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

