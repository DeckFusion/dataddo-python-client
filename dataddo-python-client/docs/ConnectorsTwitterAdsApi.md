# openapi_client.ConnectorsTwitterAdsApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**twitter_ads_controller_action_account**](ConnectorsTwitterAdsApi.md#twitter_ads_controller_action_account) | **POST** /connectors/twitter_ads/actions/account | List of all Twitter accounts
[**twitter_ads_controller_action_authorization**](ConnectorsTwitterAdsApi.md#twitter_ads_controller_action_authorization) | **GET** /connectors/twitter_ads/actions/authorization | List of authorization objects
[**twitter_ads_controller_action_campaign**](ConnectorsTwitterAdsApi.md#twitter_ads_controller_action_campaign) | **POST** /connectors/twitter_ads/actions/campaign | List of all Twitter Ads campaign IDs
[**twitter_ads_controller_action_date_range**](ConnectorsTwitterAdsApi.md#twitter_ads_controller_action_date_range) | **GET** /connectors/twitter_ads/actions/dateRange | List of date ranges
[**twitter_ads_controller_action_load**](ConnectorsTwitterAdsApi.md#twitter_ads_controller_action_load) | **POST** /connectors/twitter_ads/create-source | Create Twitter Ads source
[**twitter_ads_controller_action_preview**](ConnectorsTwitterAdsApi.md#twitter_ads_controller_action_preview) | **POST** /connectors/twitter_ads/preview | Preview the data
[**twitter_ads_controller_action_template**](ConnectorsTwitterAdsApi.md#twitter_ads_controller_action_template) | **GET** /connectors/twitter_ads/templates/{id} | List details of dataset template
[**twitter_ads_controller_action_templates**](ConnectorsTwitterAdsApi.md#twitter_ads_controller_action_templates) | **GET** /connectors/twitter_ads/templates | List all Twitter Ads dataset templates


# **twitter_ads_controller_action_account**
> List[LabelValueResponseInner] twitter_ads_controller_action_account(snapchat_controller_action_organization_request=snapchat_controller_action_organization_request)

List of all Twitter accounts

Method for listing Twitter accounts

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.snapchat_controller_action_organization_request import SnapchatControllerActionOrganizationRequest
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
    api_instance = openapi_client.ConnectorsTwitterAdsApi(api_client)
    snapchat_controller_action_organization_request = openapi_client.SnapchatControllerActionOrganizationRequest() # SnapchatControllerActionOrganizationRequest |  (optional)

    try:
        # List of all Twitter accounts
        api_response = api_instance.twitter_ads_controller_action_account(snapchat_controller_action_organization_request=snapchat_controller_action_organization_request)
        print("The response of ConnectorsTwitterAdsApi->twitter_ads_controller_action_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTwitterAdsApi->twitter_ads_controller_action_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapchat_controller_action_organization_request** | [**SnapchatControllerActionOrganizationRequest**](SnapchatControllerActionOrganizationRequest.md)|  | [optional] 

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
**200** | List of all Twitter accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **twitter_ads_controller_action_authorization**
> List[ActionAuthorizationResponseInner] twitter_ads_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsTwitterAdsApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.twitter_ads_controller_action_authorization()
        print("The response of ConnectorsTwitterAdsApi->twitter_ads_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTwitterAdsApi->twitter_ads_controller_action_authorization: %s\n" % e)
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

# **twitter_ads_controller_action_campaign**
> List[LabelValueResponseInner] twitter_ads_controller_action_campaign(snapchat_controller_action_campaign_request=snapchat_controller_action_campaign_request)

List of all Twitter Ads campaign IDs

Method for listing Twitter campaigns

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.snapchat_controller_action_campaign_request import SnapchatControllerActionCampaignRequest
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
    api_instance = openapi_client.ConnectorsTwitterAdsApi(api_client)
    snapchat_controller_action_campaign_request = openapi_client.SnapchatControllerActionCampaignRequest() # SnapchatControllerActionCampaignRequest |  (optional)

    try:
        # List of all Twitter Ads campaign IDs
        api_response = api_instance.twitter_ads_controller_action_campaign(snapchat_controller_action_campaign_request=snapchat_controller_action_campaign_request)
        print("The response of ConnectorsTwitterAdsApi->twitter_ads_controller_action_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTwitterAdsApi->twitter_ads_controller_action_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapchat_controller_action_campaign_request** | [**SnapchatControllerActionCampaignRequest**](SnapchatControllerActionCampaignRequest.md)|  | [optional] 

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
**200** | List of all Twitter Ads campaign IDs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **twitter_ads_controller_action_date_range**
> List[LabelValueResponseInner] twitter_ads_controller_action_date_range()

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
    api_instance = openapi_client.ConnectorsTwitterAdsApi(api_client)

    try:
        # List of date ranges
        api_response = api_instance.twitter_ads_controller_action_date_range()
        print("The response of ConnectorsTwitterAdsApi->twitter_ads_controller_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTwitterAdsApi->twitter_ads_controller_action_date_range: %s\n" % e)
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

# **twitter_ads_controller_action_load**
> Source twitter_ads_controller_action_load(twitter_ads_connector_form=twitter_ads_connector_form)

Create Twitter Ads source

### Example


```python
import openapi_client
from openapi_client.models.source import Source
from openapi_client.models.twitter_ads_connector_form import TwitterAdsConnectorForm
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
    api_instance = openapi_client.ConnectorsTwitterAdsApi(api_client)
    twitter_ads_connector_form = openapi_client.TwitterAdsConnectorForm() # TwitterAdsConnectorForm |  (optional)

    try:
        # Create Twitter Ads source
        api_response = api_instance.twitter_ads_controller_action_load(twitter_ads_connector_form=twitter_ads_connector_form)
        print("The response of ConnectorsTwitterAdsApi->twitter_ads_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTwitterAdsApi->twitter_ads_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **twitter_ads_connector_form** | [**TwitterAdsConnectorForm**](TwitterAdsConnectorForm.md)|  | [optional] 

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

# **twitter_ads_controller_action_preview**
> SuccessResponse twitter_ads_controller_action_preview(twitter_ads_connector_form=twitter_ads_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.success_response import SuccessResponse
from openapi_client.models.twitter_ads_connector_form import TwitterAdsConnectorForm
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
    api_instance = openapi_client.ConnectorsTwitterAdsApi(api_client)
    twitter_ads_connector_form = openapi_client.TwitterAdsConnectorForm() # TwitterAdsConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.twitter_ads_controller_action_preview(twitter_ads_connector_form=twitter_ads_connector_form)
        print("The response of ConnectorsTwitterAdsApi->twitter_ads_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTwitterAdsApi->twitter_ads_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **twitter_ads_connector_form** | [**TwitterAdsConnectorForm**](TwitterAdsConnectorForm.md)|  | [optional] 

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

# **twitter_ads_controller_action_template**
> object twitter_ads_controller_action_template(id)

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
    api_instance = openapi_client.ConnectorsTwitterAdsApi(api_client)
    id = 'id_example' # str | The id of the template to retrieve

    try:
        # List details of dataset template
        api_response = api_instance.twitter_ads_controller_action_template(id)
        print("The response of ConnectorsTwitterAdsApi->twitter_ads_controller_action_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTwitterAdsApi->twitter_ads_controller_action_template: %s\n" % e)
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

# **twitter_ads_controller_action_templates**
> ConnectorTemplateResponse twitter_ads_controller_action_templates()

List all Twitter Ads dataset templates

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
    api_instance = openapi_client.ConnectorsTwitterAdsApi(api_client)

    try:
        # List all Twitter Ads dataset templates
        api_response = api_instance.twitter_ads_controller_action_templates()
        print("The response of ConnectorsTwitterAdsApi->twitter_ads_controller_action_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsTwitterAdsApi->twitter_ads_controller_action_templates: %s\n" % e)
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
**200** | List all Twitter Ads dataset templates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

