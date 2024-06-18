# openapi_client.ConnectorsFacebookAdsApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_facebook_ads_facebook_ads_connector_action_account**](ConnectorsFacebookAdsApi.md#app_connector_facebook_ads_facebook_ads_connector_action_account) | **POST** /connectors/facebook_ads/actions/account | List of all accounts
[**app_connector_facebook_ads_facebook_ads_connector_action_ad_set**](ConnectorsFacebookAdsApi.md#app_connector_facebook_ads_facebook_ads_connector_action_ad_set) | **POST** /connectors/facebook_ads/actions/adSet | List of Ad sets
[**app_connector_facebook_ads_facebook_ads_connector_action_authorization**](ConnectorsFacebookAdsApi.md#app_connector_facebook_ads_facebook_ads_connector_action_authorization) | **GET** /connectors/facebook_ads/actions/authorization | List of authorization objects
[**app_connector_facebook_ads_facebook_ads_connector_action_campaign**](ConnectorsFacebookAdsApi.md#app_connector_facebook_ads_facebook_ads_connector_action_campaign) | **POST** /connectors/facebook_ads/actions/campaign | List of all campaigns
[**app_connector_facebook_ads_facebook_ads_connector_action_data_label**](ConnectorsFacebookAdsApi.md#app_connector_facebook_ads_facebook_ads_connector_action_data_label) | **GET** /connectors/facebook_ads/actions/dataLabel | List of all data labels
[**app_connector_facebook_ads_facebook_ads_connector_action_date_range**](ConnectorsFacebookAdsApi.md#app_connector_facebook_ads_facebook_ads_connector_action_date_range) | **GET** /connectors/facebook_ads/actions/dateRange | Method for listing date range
[**app_connector_facebook_ads_facebook_ads_connector_action_level**](ConnectorsFacebookAdsApi.md#app_connector_facebook_ads_facebook_ads_connector_action_level) | **GET** /connectors/facebook_ads/actions/level | List of all reporting levels
[**app_connector_facebook_ads_facebook_ads_connector_action_metric**](ConnectorsFacebookAdsApi.md#app_connector_facebook_ads_facebook_ads_connector_action_metric) | **GET** /connectors/facebook_ads/actions/metric | List of all metrics
[**app_connector_facebook_ads_facebook_ads_connector_action_optional_breakdown**](ConnectorsFacebookAdsApi.md#app_connector_facebook_ads_facebook_ads_connector_action_optional_breakdown) | **GET** /connectors/facebook_ads/actions/optionalBreakdown | List of all optional breakdowns
[**app_connector_facebook_ads_facebook_ads_connector_action_time_breakdown**](ConnectorsFacebookAdsApi.md#app_connector_facebook_ads_facebook_ads_connector_action_time_breakdown) | **GET** /connectors/facebook_ads/actions/timeBreakdown | List of all time breakdowns
[**app_connector_facebook_ads_facebook_ads_connector_create_source**](ConnectorsFacebookAdsApi.md#app_connector_facebook_ads_facebook_ads_connector_create_source) | **POST** /connectors/facebook_ads/create-source | Create FacebookAds source
[**app_connector_facebook_ads_facebook_ads_connector_preview**](ConnectorsFacebookAdsApi.md#app_connector_facebook_ads_facebook_ads_connector_preview) | **POST** /connectors/facebook_ads/preview | Data preview


# **app_connector_facebook_ads_facebook_ads_connector_action_account**
> List[LabelValueResponseInner] app_connector_facebook_ads_facebook_ads_connector_action_account(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List of all accounts

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
    api_instance = openapi_client.ConnectorsFacebookAdsApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List of all accounts
        api_response = api_instance.app_connector_facebook_ads_facebook_ads_connector_action_account(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_account: %s\n" % e)
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

# **app_connector_facebook_ads_facebook_ads_connector_action_ad_set**
> List[LabelValueResponseInner] app_connector_facebook_ads_facebook_ads_connector_action_ad_set(app_connector_facebook_ads_facebook_ads_connector_action_ad_set_request=app_connector_facebook_ads_facebook_ads_connector_action_ad_set_request)

List of Ad sets

### Example


```python
import openapi_client
from openapi_client.models.app_connector_facebook_ads_facebook_ads_connector_action_ad_set_request import AppConnectorFacebookAdsFacebookAdsConnectorActionAdSetRequest
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
    api_instance = openapi_client.ConnectorsFacebookAdsApi(api_client)
    app_connector_facebook_ads_facebook_ads_connector_action_ad_set_request = openapi_client.AppConnectorFacebookAdsFacebookAdsConnectorActionAdSetRequest() # AppConnectorFacebookAdsFacebookAdsConnectorActionAdSetRequest |  (optional)

    try:
        # List of Ad sets
        api_response = api_instance.app_connector_facebook_ads_facebook_ads_connector_action_ad_set(app_connector_facebook_ads_facebook_ads_connector_action_ad_set_request=app_connector_facebook_ads_facebook_ads_connector_action_ad_set_request)
        print("The response of ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_ad_set:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_ad_set: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_connector_facebook_ads_facebook_ads_connector_action_ad_set_request** | [**AppConnectorFacebookAdsFacebookAdsConnectorActionAdSetRequest**](AppConnectorFacebookAdsFacebookAdsConnectorActionAdSetRequest.md)|  | [optional] 

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
**200** | List of Ad sets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_facebook_ads_facebook_ads_connector_action_authorization**
> List[ActionAuthorizationResponseInner] app_connector_facebook_ads_facebook_ads_connector_action_authorization()

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
    api_instance = openapi_client.ConnectorsFacebookAdsApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_connector_facebook_ads_facebook_ads_connector_action_authorization()
        print("The response of ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_authorization: %s\n" % e)
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

# **app_connector_facebook_ads_facebook_ads_connector_action_campaign**
> List[LabelValueResponseInner] app_connector_facebook_ads_facebook_ads_connector_action_campaign(app_connector_facebook_ads_facebook_ads_connector_action_campaign_request=app_connector_facebook_ads_facebook_ads_connector_action_campaign_request)

List of all campaigns

### Example


```python
import openapi_client
from openapi_client.models.app_connector_facebook_ads_facebook_ads_connector_action_campaign_request import AppConnectorFacebookAdsFacebookAdsConnectorActionCampaignRequest
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
    api_instance = openapi_client.ConnectorsFacebookAdsApi(api_client)
    app_connector_facebook_ads_facebook_ads_connector_action_campaign_request = openapi_client.AppConnectorFacebookAdsFacebookAdsConnectorActionCampaignRequest() # AppConnectorFacebookAdsFacebookAdsConnectorActionCampaignRequest |  (optional)

    try:
        # List of all campaigns
        api_response = api_instance.app_connector_facebook_ads_facebook_ads_connector_action_campaign(app_connector_facebook_ads_facebook_ads_connector_action_campaign_request=app_connector_facebook_ads_facebook_ads_connector_action_campaign_request)
        print("The response of ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_connector_facebook_ads_facebook_ads_connector_action_campaign_request** | [**AppConnectorFacebookAdsFacebookAdsConnectorActionCampaignRequest**](AppConnectorFacebookAdsFacebookAdsConnectorActionCampaignRequest.md)|  | [optional] 

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
**200** | List of campaigns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_facebook_ads_facebook_ads_connector_action_data_label**
> List[LabelValueResponseInner] app_connector_facebook_ads_facebook_ads_connector_action_data_label()

List of all data labels

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
    api_instance = openapi_client.ConnectorsFacebookAdsApi(api_client)

    try:
        # List of all data labels
        api_response = api_instance.app_connector_facebook_ads_facebook_ads_connector_action_data_label()
        print("The response of ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_data_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_data_label: %s\n" % e)
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
**200** | List of data label objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_facebook_ads_facebook_ads_connector_action_date_range**
> List[LabelValueResponseInner] app_connector_facebook_ads_facebook_ads_connector_action_date_range()

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
    api_instance = openapi_client.ConnectorsFacebookAdsApi(api_client)

    try:
        # Method for listing date range
        api_response = api_instance.app_connector_facebook_ads_facebook_ads_connector_action_date_range()
        print("The response of ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_date_range: %s\n" % e)
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
**200** | List of Facebook Ads date ranges |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_facebook_ads_facebook_ads_connector_action_level**
> List[LabelValueResponseInner] app_connector_facebook_ads_facebook_ads_connector_action_level()

List of all reporting levels

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
    api_instance = openapi_client.ConnectorsFacebookAdsApi(api_client)

    try:
        # List of all reporting levels
        api_response = api_instance.app_connector_facebook_ads_facebook_ads_connector_action_level()
        print("The response of ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_level:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_level: %s\n" % e)
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
**200** | List of reporting level objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_facebook_ads_facebook_ads_connector_action_metric**
> List[LabelValueResponseInner] app_connector_facebook_ads_facebook_ads_connector_action_metric()

List of all metrics

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
    api_instance = openapi_client.ConnectorsFacebookAdsApi(api_client)

    try:
        # List of all metrics
        api_response = api_instance.app_connector_facebook_ads_facebook_ads_connector_action_metric()
        print("The response of ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_metric: %s\n" % e)
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
**200** | List of metric objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_facebook_ads_facebook_ads_connector_action_optional_breakdown**
> List[LabelValueResponseInner] app_connector_facebook_ads_facebook_ads_connector_action_optional_breakdown()

List of all optional breakdowns

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
    api_instance = openapi_client.ConnectorsFacebookAdsApi(api_client)

    try:
        # List of all optional breakdowns
        api_response = api_instance.app_connector_facebook_ads_facebook_ads_connector_action_optional_breakdown()
        print("The response of ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_optional_breakdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_optional_breakdown: %s\n" % e)
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
**200** | List of optional breakdown objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_facebook_ads_facebook_ads_connector_action_time_breakdown**
> List[LabelValueResponseInner] app_connector_facebook_ads_facebook_ads_connector_action_time_breakdown()

List of all time breakdowns

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
    api_instance = openapi_client.ConnectorsFacebookAdsApi(api_client)

    try:
        # List of all time breakdowns
        api_response = api_instance.app_connector_facebook_ads_facebook_ads_connector_action_time_breakdown()
        print("The response of ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_time_breakdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_action_time_breakdown: %s\n" % e)
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
**200** | List of time breakdown objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_facebook_ads_facebook_ads_connector_create_source**
> Source app_connector_facebook_ads_facebook_ads_connector_create_source(facebook_ads_connector_form=facebook_ads_connector_form)

Create FacebookAds source

### Example


```python
import openapi_client
from openapi_client.models.facebook_ads_connector_form import FacebookAdsConnectorForm
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
    api_instance = openapi_client.ConnectorsFacebookAdsApi(api_client)
    facebook_ads_connector_form = openapi_client.FacebookAdsConnectorForm() # FacebookAdsConnectorForm |  (optional)

    try:
        # Create FacebookAds source
        api_response = api_instance.app_connector_facebook_ads_facebook_ads_connector_create_source(facebook_ads_connector_form=facebook_ads_connector_form)
        print("The response of ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_create_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_create_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facebook_ads_connector_form** | [**FacebookAdsConnectorForm**](FacebookAdsConnectorForm.md)|  | [optional] 

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

# **app_connector_facebook_ads_facebook_ads_connector_preview**
> SuccessResponse app_connector_facebook_ads_facebook_ads_connector_preview(facebook_ads_connector_form=facebook_ads_connector_form)

Data preview

### Example


```python
import openapi_client
from openapi_client.models.facebook_ads_connector_form import FacebookAdsConnectorForm
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
    api_instance = openapi_client.ConnectorsFacebookAdsApi(api_client)
    facebook_ads_connector_form = openapi_client.FacebookAdsConnectorForm() # FacebookAdsConnectorForm |  (optional)

    try:
        # Data preview
        api_response = api_instance.app_connector_facebook_ads_facebook_ads_connector_preview(facebook_ads_connector_form=facebook_ads_connector_form)
        print("The response of ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsFacebookAdsApi->app_connector_facebook_ads_facebook_ads_connector_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facebook_ads_connector_form** | [**FacebookAdsConnectorForm**](FacebookAdsConnectorForm.md)|  | [optional] 

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

