# openapi_client.ConnectorsGoogleDisplayVideoApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_google_display_video_google_display_video_connector_action_advertiser**](ConnectorsGoogleDisplayVideoApi.md#app_connector_google_display_video_google_display_video_connector_action_advertiser) | **GET** /connectors/google_display_video/actions/advertiser | List of Google Display &amp; Video advertisers
[**app_connector_google_display_video_google_display_video_connector_action_authorization**](ConnectorsGoogleDisplayVideoApi.md#app_connector_google_display_video_google_display_video_connector_action_authorization) | **GET** /connectors/google_display_video/actions/authorization | List of authorization objects
[**app_connector_google_display_video_google_display_video_connector_action_dimensions**](ConnectorsGoogleDisplayVideoApi.md#app_connector_google_display_video_google_display_video_connector_action_dimensions) | **GET** /connectors/google_display_video/actions/dimensions | List of Google Display &amp; Video dimensions
[**app_connector_google_display_video_google_display_video_connector_action_metrics**](ConnectorsGoogleDisplayVideoApi.md#app_connector_google_display_video_google_display_video_connector_action_metrics) | **GET** /connectors/google_display_video/actions/metrics | List of Google Display &amp; Video metrics
[**app_connector_google_display_video_google_display_video_connector_action_partner**](ConnectorsGoogleDisplayVideoApi.md#app_connector_google_display_video_google_display_video_connector_action_partner) | **GET** /connectors/google_display_video/actions/partner | List of Google Display &amp; Video partners


# **app_connector_google_display_video_google_display_video_connector_action_advertiser**
> List[LabelValueResponseInner] app_connector_google_display_video_google_display_video_connector_action_advertiser()

List of Google Display & Video advertisers

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
    api_instance = openapi_client.ConnectorsGoogleDisplayVideoApi(api_client)

    try:
        # List of Google Display & Video advertisers
        api_response = api_instance.app_connector_google_display_video_google_display_video_connector_action_advertiser()
        print("The response of ConnectorsGoogleDisplayVideoApi->app_connector_google_display_video_google_display_video_connector_action_advertiser:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleDisplayVideoApi->app_connector_google_display_video_google_display_video_connector_action_advertiser: %s\n" % e)
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
**200** | List of available advertisers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_google_display_video_google_display_video_connector_action_authorization**
> List[ActionAuthorizationResponseInner] app_connector_google_display_video_google_display_video_connector_action_authorization()

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
    api_instance = openapi_client.ConnectorsGoogleDisplayVideoApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_connector_google_display_video_google_display_video_connector_action_authorization()
        print("The response of ConnectorsGoogleDisplayVideoApi->app_connector_google_display_video_google_display_video_connector_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleDisplayVideoApi->app_connector_google_display_video_google_display_video_connector_action_authorization: %s\n" % e)
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

# **app_connector_google_display_video_google_display_video_connector_action_dimensions**
> List[LabelValueResponseInner] app_connector_google_display_video_google_display_video_connector_action_dimensions()

List of Google Display & Video dimensions

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
    api_instance = openapi_client.ConnectorsGoogleDisplayVideoApi(api_client)

    try:
        # List of Google Display & Video dimensions
        api_response = api_instance.app_connector_google_display_video_google_display_video_connector_action_dimensions()
        print("The response of ConnectorsGoogleDisplayVideoApi->app_connector_google_display_video_google_display_video_connector_action_dimensions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleDisplayVideoApi->app_connector_google_display_video_google_display_video_connector_action_dimensions: %s\n" % e)
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
**200** | List of available dimensions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_google_display_video_google_display_video_connector_action_metrics**
> List[LabelValueResponseInner] app_connector_google_display_video_google_display_video_connector_action_metrics()

List of Google Display & Video metrics

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
    api_instance = openapi_client.ConnectorsGoogleDisplayVideoApi(api_client)

    try:
        # List of Google Display & Video metrics
        api_response = api_instance.app_connector_google_display_video_google_display_video_connector_action_metrics()
        print("The response of ConnectorsGoogleDisplayVideoApi->app_connector_google_display_video_google_display_video_connector_action_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleDisplayVideoApi->app_connector_google_display_video_google_display_video_connector_action_metrics: %s\n" % e)
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
**200** | List of available metrics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_google_display_video_google_display_video_connector_action_partner**
> List[LabelValueResponseInner] app_connector_google_display_video_google_display_video_connector_action_partner()

List of Google Display & Video partners

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
    api_instance = openapi_client.ConnectorsGoogleDisplayVideoApi(api_client)

    try:
        # List of Google Display & Video partners
        api_response = api_instance.app_connector_google_display_video_google_display_video_connector_action_partner()
        print("The response of ConnectorsGoogleDisplayVideoApi->app_connector_google_display_video_google_display_video_connector_action_partner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleDisplayVideoApi->app_connector_google_display_video_google_display_video_connector_action_partner: %s\n" % e)
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
**200** | List of available partners |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

