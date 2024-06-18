# openapi_client.ConnectorsMercadoLibreApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_mercado_libre_mercado_libre_connector_action_brand_advertiser**](ConnectorsMercadoLibreApi.md#app_connector_mercado_libre_mercado_libre_connector_action_brand_advertiser) | **POST** /connectors/mercado_libre/actions/brandAdvertiser/ | List all Advertiser Ids
[**app_connector_mercado_libre_mercado_libre_connector_action_brand_campaign**](ConnectorsMercadoLibreApi.md#app_connector_mercado_libre_mercado_libre_connector_action_brand_campaign) | **POST** /connectors/mercado_libre/actions/brandCampaign | List all Advertiser Ids
[**app_connector_mercado_libre_mercado_libre_connector_action_display_advertiser**](ConnectorsMercadoLibreApi.md#app_connector_mercado_libre_mercado_libre_connector_action_display_advertiser) | **POST** /connectors/mercado_libre/actions/displayAdvertiser/ | List all Advertiser Ids
[**app_connector_mercado_libre_mercado_libre_connector_action_display_campaign**](ConnectorsMercadoLibreApi.md#app_connector_mercado_libre_mercado_libre_connector_action_display_campaign) | **POST** /connectors/mercado_libre/actions/displayCampaign | List all Advertiser Ids
[**app_connector_mercado_libre_mercado_libre_connector_action_product_advertiser**](ConnectorsMercadoLibreApi.md#app_connector_mercado_libre_mercado_libre_connector_action_product_advertiser) | **POST** /connectors/mercado_libre/actions/productAdvertiser/ | List all Advertiser Ids
[**app_connector_mercado_libre_mercado_libre_connector_action_product_campaign**](ConnectorsMercadoLibreApi.md#app_connector_mercado_libre_mercado_libre_connector_action_product_campaign) | **POST** /connectors/mercado_libre/actions/productCampaign | List all Advertiser Ids
[**app_connector_mercado_libre_mercado_libre_connector_action_seller**](ConnectorsMercadoLibreApi.md#app_connector_mercado_libre_mercado_libre_connector_action_seller) | **POST** /connectors/mercado_libre/actions/attributes | List all Seller Ids


# **app_connector_mercado_libre_mercado_libre_connector_action_brand_advertiser**
> List[LabelValueResponseInner] app_connector_mercado_libre_mercado_libre_connector_action_brand_advertiser(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List all Advertiser Ids

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
    api_instance = openapi_client.ConnectorsMercadoLibreApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List all Advertiser Ids
        api_response = api_instance.app_connector_mercado_libre_mercado_libre_connector_action_brand_advertiser(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsMercadoLibreApi->app_connector_mercado_libre_mercado_libre_connector_action_brand_advertiser:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMercadoLibreApi->app_connector_mercado_libre_mercado_libre_connector_action_brand_advertiser: %s\n" % e)
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
**200** | List of Mercado Libre advertiser Ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_mercado_libre_mercado_libre_connector_action_brand_campaign**
> List[LabelValueResponseInner] app_connector_mercado_libre_mercado_libre_connector_action_brand_campaign(app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request=app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request)

List all Advertiser Ids

### Example


```python
import openapi_client
from openapi_client.models.app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request import AppConnectorMercadoLibreMercadoLibreConnectorActionDisplayCampaignRequest
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
    api_instance = openapi_client.ConnectorsMercadoLibreApi(api_client)
    app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request = openapi_client.AppConnectorMercadoLibreMercadoLibreConnectorActionDisplayCampaignRequest() # AppConnectorMercadoLibreMercadoLibreConnectorActionDisplayCampaignRequest |  (optional)

    try:
        # List all Advertiser Ids
        api_response = api_instance.app_connector_mercado_libre_mercado_libre_connector_action_brand_campaign(app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request=app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request)
        print("The response of ConnectorsMercadoLibreApi->app_connector_mercado_libre_mercado_libre_connector_action_brand_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMercadoLibreApi->app_connector_mercado_libre_mercado_libre_connector_action_brand_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request** | [**AppConnectorMercadoLibreMercadoLibreConnectorActionDisplayCampaignRequest**](AppConnectorMercadoLibreMercadoLibreConnectorActionDisplayCampaignRequest.md)|  | [optional] 

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
**200** | List of Mercado Libre advertiser Ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_mercado_libre_mercado_libre_connector_action_display_advertiser**
> List[LabelValueResponseInner] app_connector_mercado_libre_mercado_libre_connector_action_display_advertiser(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List all Advertiser Ids

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
    api_instance = openapi_client.ConnectorsMercadoLibreApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List all Advertiser Ids
        api_response = api_instance.app_connector_mercado_libre_mercado_libre_connector_action_display_advertiser(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsMercadoLibreApi->app_connector_mercado_libre_mercado_libre_connector_action_display_advertiser:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMercadoLibreApi->app_connector_mercado_libre_mercado_libre_connector_action_display_advertiser: %s\n" % e)
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
**200** | List of Mercado Libre advertiser Ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_mercado_libre_mercado_libre_connector_action_display_campaign**
> List[LabelValueResponseInner] app_connector_mercado_libre_mercado_libre_connector_action_display_campaign(app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request=app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request)

List all Advertiser Ids

### Example


```python
import openapi_client
from openapi_client.models.app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request import AppConnectorMercadoLibreMercadoLibreConnectorActionDisplayCampaignRequest
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
    api_instance = openapi_client.ConnectorsMercadoLibreApi(api_client)
    app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request = openapi_client.AppConnectorMercadoLibreMercadoLibreConnectorActionDisplayCampaignRequest() # AppConnectorMercadoLibreMercadoLibreConnectorActionDisplayCampaignRequest |  (optional)

    try:
        # List all Advertiser Ids
        api_response = api_instance.app_connector_mercado_libre_mercado_libre_connector_action_display_campaign(app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request=app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request)
        print("The response of ConnectorsMercadoLibreApi->app_connector_mercado_libre_mercado_libre_connector_action_display_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMercadoLibreApi->app_connector_mercado_libre_mercado_libre_connector_action_display_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request** | [**AppConnectorMercadoLibreMercadoLibreConnectorActionDisplayCampaignRequest**](AppConnectorMercadoLibreMercadoLibreConnectorActionDisplayCampaignRequest.md)|  | [optional] 

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
**200** | List of Mercado Libre advertiser Ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_mercado_libre_mercado_libre_connector_action_product_advertiser**
> List[LabelValueResponseInner] app_connector_mercado_libre_mercado_libre_connector_action_product_advertiser(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List all Advertiser Ids

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
    api_instance = openapi_client.ConnectorsMercadoLibreApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List all Advertiser Ids
        api_response = api_instance.app_connector_mercado_libre_mercado_libre_connector_action_product_advertiser(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsMercadoLibreApi->app_connector_mercado_libre_mercado_libre_connector_action_product_advertiser:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMercadoLibreApi->app_connector_mercado_libre_mercado_libre_connector_action_product_advertiser: %s\n" % e)
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
**200** | List of Mercado Libre advertiser Ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_mercado_libre_mercado_libre_connector_action_product_campaign**
> List[LabelValueResponseInner] app_connector_mercado_libre_mercado_libre_connector_action_product_campaign(app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request=app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request)

List all Advertiser Ids

### Example


```python
import openapi_client
from openapi_client.models.app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request import AppConnectorMercadoLibreMercadoLibreConnectorActionDisplayCampaignRequest
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
    api_instance = openapi_client.ConnectorsMercadoLibreApi(api_client)
    app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request = openapi_client.AppConnectorMercadoLibreMercadoLibreConnectorActionDisplayCampaignRequest() # AppConnectorMercadoLibreMercadoLibreConnectorActionDisplayCampaignRequest |  (optional)

    try:
        # List all Advertiser Ids
        api_response = api_instance.app_connector_mercado_libre_mercado_libre_connector_action_product_campaign(app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request=app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request)
        print("The response of ConnectorsMercadoLibreApi->app_connector_mercado_libre_mercado_libre_connector_action_product_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMercadoLibreApi->app_connector_mercado_libre_mercado_libre_connector_action_product_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_connector_mercado_libre_mercado_libre_connector_action_display_campaign_request** | [**AppConnectorMercadoLibreMercadoLibreConnectorActionDisplayCampaignRequest**](AppConnectorMercadoLibreMercadoLibreConnectorActionDisplayCampaignRequest.md)|  | [optional] 

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
**200** | List of Mercado Libre advertiser Ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_mercado_libre_mercado_libre_connector_action_seller**
> List[LabelValueResponseInner] app_connector_mercado_libre_mercado_libre_connector_action_seller(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List all Seller Ids

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
    api_instance = openapi_client.ConnectorsMercadoLibreApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List all Seller Ids
        api_response = api_instance.app_connector_mercado_libre_mercado_libre_connector_action_seller(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsMercadoLibreApi->app_connector_mercado_libre_mercado_libre_connector_action_seller:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMercadoLibreApi->app_connector_mercado_libre_mercado_libre_connector_action_seller: %s\n" % e)
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
**200** | List of Mercado Libre seller Ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

