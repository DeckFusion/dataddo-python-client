# openapi_client.ConnectorsGoogleCampaignManagerApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**google_campaign_manager_controller_action_authorization**](ConnectorsGoogleCampaignManagerApi.md#google_campaign_manager_controller_action_authorization) | **GET** /connectors/google_campaign_manager/actions/authorization | List of authorization objects
[**google_campaign_manager_controller_action_load**](ConnectorsGoogleCampaignManagerApi.md#google_campaign_manager_controller_action_load) | **POST** /connectors/google_campaign_manager/create-source | Create Google Campaign Manager source
[**google_campaign_manager_controller_action_preview**](ConnectorsGoogleCampaignManagerApi.md#google_campaign_manager_controller_action_preview) | **POST** /connectors/google_campaign_manager/preview | Preview the data
[**google_campaign_manager_controller_action_profile**](ConnectorsGoogleCampaignManagerApi.md#google_campaign_manager_controller_action_profile) | **POST** /connectors/google_campaign_manager/actions/profile | List of profile ids
[**google_campaign_manager_controller_action_report_type**](ConnectorsGoogleCampaignManagerApi.md#google_campaign_manager_controller_action_report_type) | **POST** /connectors/google_campaign_manager/actions/reportType | List Google Campaign Manager report types


# **google_campaign_manager_controller_action_authorization**
> List[ActionAuthorizationResponseInner] google_campaign_manager_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsGoogleCampaignManagerApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.google_campaign_manager_controller_action_authorization()
        print("The response of ConnectorsGoogleCampaignManagerApi->google_campaign_manager_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleCampaignManagerApi->google_campaign_manager_controller_action_authorization: %s\n" % e)
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

# **google_campaign_manager_controller_action_load**
> Source google_campaign_manager_controller_action_load(google_campaign_manager_connector_form=google_campaign_manager_connector_form)

Create Google Campaign Manager source

### Example


```python
import openapi_client
from openapi_client.models.google_campaign_manager_connector_form import GoogleCampaignManagerConnectorForm
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
    api_instance = openapi_client.ConnectorsGoogleCampaignManagerApi(api_client)
    google_campaign_manager_connector_form = openapi_client.GoogleCampaignManagerConnectorForm() # GoogleCampaignManagerConnectorForm |  (optional)

    try:
        # Create Google Campaign Manager source
        api_response = api_instance.google_campaign_manager_controller_action_load(google_campaign_manager_connector_form=google_campaign_manager_connector_form)
        print("The response of ConnectorsGoogleCampaignManagerApi->google_campaign_manager_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleCampaignManagerApi->google_campaign_manager_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_campaign_manager_connector_form** | [**GoogleCampaignManagerConnectorForm**](GoogleCampaignManagerConnectorForm.md)|  | [optional] 

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

# **google_campaign_manager_controller_action_preview**
> SuccessResponse google_campaign_manager_controller_action_preview(google_campaign_manager_connector_form=google_campaign_manager_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.google_campaign_manager_connector_form import GoogleCampaignManagerConnectorForm
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
    api_instance = openapi_client.ConnectorsGoogleCampaignManagerApi(api_client)
    google_campaign_manager_connector_form = openapi_client.GoogleCampaignManagerConnectorForm() # GoogleCampaignManagerConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.google_campaign_manager_controller_action_preview(google_campaign_manager_connector_form=google_campaign_manager_connector_form)
        print("The response of ConnectorsGoogleCampaignManagerApi->google_campaign_manager_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleCampaignManagerApi->google_campaign_manager_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_campaign_manager_connector_form** | [**GoogleCampaignManagerConnectorForm**](GoogleCampaignManagerConnectorForm.md)|  | [optional] 

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

# **google_campaign_manager_controller_action_profile**
> List[LabelValueResponseInner] google_campaign_manager_controller_action_profile(request_body=request_body)

List of profile ids

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
    api_instance = openapi_client.ConnectorsGoogleCampaignManagerApi(api_client)
    request_body = {'key': openapi_client.AmazonAdsControllerActionProfileRequestValue()} # Dict[str, AmazonAdsControllerActionProfileRequestValue] |  (optional)

    try:
        # List of profile ids
        api_response = api_instance.google_campaign_manager_controller_action_profile(request_body=request_body)
        print("The response of ConnectorsGoogleCampaignManagerApi->google_campaign_manager_controller_action_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleCampaignManagerApi->google_campaign_manager_controller_action_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, AmazonAdsControllerActionProfileRequestValue]**](AmazonAdsControllerActionProfileRequestValue.md)|  | [optional] 

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
**200** | List of Google Campaign Manager profiles |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_campaign_manager_controller_action_report_type**
> List[LabelValueResponseInner] google_campaign_manager_controller_action_report_type(request_body=request_body)

List Google Campaign Manager report types

### Example


```python
import openapi_client
from openapi_client.models.amazon_ads_controller_action_report_type_request_value import AmazonAdsControllerActionReportTypeRequestValue
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
    api_instance = openapi_client.ConnectorsGoogleCampaignManagerApi(api_client)
    request_body = {'key': openapi_client.AmazonAdsControllerActionReportTypeRequestValue()} # Dict[str, AmazonAdsControllerActionReportTypeRequestValue] |  (optional)

    try:
        # List Google Campaign Manager report types
        api_response = api_instance.google_campaign_manager_controller_action_report_type(request_body=request_body)
        print("The response of ConnectorsGoogleCampaignManagerApi->google_campaign_manager_controller_action_report_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleCampaignManagerApi->google_campaign_manager_controller_action_report_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, AmazonAdsControllerActionReportTypeRequestValue]**](AmazonAdsControllerActionReportTypeRequestValue.md)|  | [optional] 

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
**200** | List of Google Campaign Manager report types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

