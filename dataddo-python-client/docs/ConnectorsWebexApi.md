# openapi_client.ConnectorsWebexApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_webex_webex_connector_action_meeting_site**](ConnectorsWebexApi.md#app_connector_webex_webex_connector_action_meeting_site) | **GET** /connector/webex/actions/meetingsSites | List of Webex meetings sites
[**app_connector_webex_webex_connector_action_meetings**](ConnectorsWebexApi.md#app_connector_webex_webex_connector_action_meetings) | **GET** /connector/webex/actions/meetings | List of Webex meetings
[**app_connector_webex_webex_connector_action_meetings_with_polls**](ConnectorsWebexApi.md#app_connector_webex_webex_connector_action_meetings_with_polls) | **GET** /connector/webex/actions/meetingsWithPolls | List of Webex meetings


# **app_connector_webex_webex_connector_action_meeting_site**
> List[LabelValueResponseInner] app_connector_webex_webex_connector_action_meeting_site()

List of Webex meetings sites

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
    api_instance = openapi_client.ConnectorsWebexApi(api_client)

    try:
        # List of Webex meetings sites
        api_response = api_instance.app_connector_webex_webex_connector_action_meeting_site()
        print("The response of ConnectorsWebexApi->app_connector_webex_webex_connector_action_meeting_site:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsWebexApi->app_connector_webex_webex_connector_action_meeting_site: %s\n" % e)
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
**200** | List of Webex meetings sites |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_webex_webex_connector_action_meetings**
> List[LabelValueResponseInner] app_connector_webex_webex_connector_action_meetings()

List of Webex meetings

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
    api_instance = openapi_client.ConnectorsWebexApi(api_client)

    try:
        # List of Webex meetings
        api_response = api_instance.app_connector_webex_webex_connector_action_meetings()
        print("The response of ConnectorsWebexApi->app_connector_webex_webex_connector_action_meetings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsWebexApi->app_connector_webex_webex_connector_action_meetings: %s\n" % e)
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
**200** | List of Webex meetings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_webex_webex_connector_action_meetings_with_polls**
> List[LabelValueResponseInner] app_connector_webex_webex_connector_action_meetings_with_polls()

List of Webex meetings

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
    api_instance = openapi_client.ConnectorsWebexApi(api_client)

    try:
        # List of Webex meetings
        api_response = api_instance.app_connector_webex_webex_connector_action_meetings_with_polls()
        print("The response of ConnectorsWebexApi->app_connector_webex_webex_connector_action_meetings_with_polls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsWebexApi->app_connector_webex_webex_connector_action_meetings_with_polls: %s\n" % e)
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
**200** | List of Webex meetings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

