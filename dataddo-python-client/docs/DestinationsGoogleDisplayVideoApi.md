# openapi_client.DestinationsGoogleDisplayVideoApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_google_display_video_google_display_video_connector_action_date_range**](DestinationsGoogleDisplayVideoApi.md#app_connector_google_display_video_google_display_video_connector_action_date_range) | **GET** /destinations/google_display_video/actions/dateRange | List of Google Display &amp; Video date ranges
[**app_connector_google_display_video_google_display_video_connector_action_query**](DestinationsGoogleDisplayVideoApi.md#app_connector_google_display_video_google_display_video_connector_action_query) | **GET** /destinations/google_display_video/actions/query | List of Google Display &amp; Video queries


# **app_connector_google_display_video_google_display_video_connector_action_date_range**
> List[LabelValueResponseInner] app_connector_google_display_video_google_display_video_connector_action_date_range()

List of Google Display & Video date ranges

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
    api_instance = openapi_client.DestinationsGoogleDisplayVideoApi(api_client)

    try:
        # List of Google Display & Video date ranges
        api_response = api_instance.app_connector_google_display_video_google_display_video_connector_action_date_range()
        print("The response of DestinationsGoogleDisplayVideoApi->app_connector_google_display_video_google_display_video_connector_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsGoogleDisplayVideoApi->app_connector_google_display_video_google_display_video_connector_action_date_range: %s\n" % e)
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
**200** | List of available date ranges |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_google_display_video_google_display_video_connector_action_query**
> List[LabelValueResponseInner] app_connector_google_display_video_google_display_video_connector_action_query()

List of Google Display & Video queries

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
    api_instance = openapi_client.DestinationsGoogleDisplayVideoApi(api_client)

    try:
        # List of Google Display & Video queries
        api_response = api_instance.app_connector_google_display_video_google_display_video_connector_action_query()
        print("The response of DestinationsGoogleDisplayVideoApi->app_connector_google_display_video_google_display_video_connector_action_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsGoogleDisplayVideoApi->app_connector_google_display_video_google_display_video_connector_action_query: %s\n" % e)
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
**200** | List of DV 360 Queries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

