# openapi_client.ConnectorsYoutubeVideoApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**youtube_video_controller_action_attribute**](ConnectorsYoutubeVideoApi.md#youtube_video_controller_action_attribute) | **GET** /connectors/youtube_video/actions/attribute | List of attributes
[**youtube_video_controller_action_authorization**](ConnectorsYoutubeVideoApi.md#youtube_video_controller_action_authorization) | **GET** /connectors/youtube_video/actions/authorization | List of authorization objects
[**youtube_video_controller_action_channel**](ConnectorsYoutubeVideoApi.md#youtube_video_controller_action_channel) | **POST** /connectors/youtube_video/actions/channel | List of channels
[**youtube_video_controller_action_date_range**](ConnectorsYoutubeVideoApi.md#youtube_video_controller_action_date_range) | **GET** /connectors/youtube_video/actions/dateRange | List of date ranges
[**youtube_video_controller_action_default_attribute**](ConnectorsYoutubeVideoApi.md#youtube_video_controller_action_default_attribute) | **GET** /connectors/youtube_video/actions/defaultAttribute | List of attributes
[**youtube_video_controller_action_load**](ConnectorsYoutubeVideoApi.md#youtube_video_controller_action_load) | **POST** /connectors/youtube_video/create-source | Create Youtube Video source
[**youtube_video_controller_action_playlist**](ConnectorsYoutubeVideoApi.md#youtube_video_controller_action_playlist) | **POST** /connectors/youtube_video/actions/playlist | List of playlists
[**youtube_video_controller_action_preview**](ConnectorsYoutubeVideoApi.md#youtube_video_controller_action_preview) | **POST** /connectors/youtube_video/preview | Preview the data


# **youtube_video_controller_action_attribute**
> List[LabelValueResponseInner] youtube_video_controller_action_attribute()

List of attributes

List all attributes

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
    api_instance = openapi_client.ConnectorsYoutubeVideoApi(api_client)

    try:
        # List of attributes
        api_response = api_instance.youtube_video_controller_action_attribute()
        print("The response of ConnectorsYoutubeVideoApi->youtube_video_controller_action_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsYoutubeVideoApi->youtube_video_controller_action_attribute: %s\n" % e)
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

# **youtube_video_controller_action_authorization**
> List[ActionAuthorizationResponseInner] youtube_video_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsYoutubeVideoApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.youtube_video_controller_action_authorization()
        print("The response of ConnectorsYoutubeVideoApi->youtube_video_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsYoutubeVideoApi->youtube_video_controller_action_authorization: %s\n" % e)
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

# **youtube_video_controller_action_channel**
> List[LabelValueResponseInner] youtube_video_controller_action_channel(youtube_analytics_controller_action_channel_request=youtube_analytics_controller_action_channel_request)

List of channels

Method for listing YT Channels

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.youtube_analytics_controller_action_channel_request import YoutubeAnalyticsControllerActionChannelRequest
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
    api_instance = openapi_client.ConnectorsYoutubeVideoApi(api_client)
    youtube_analytics_controller_action_channel_request = openapi_client.YoutubeAnalyticsControllerActionChannelRequest() # YoutubeAnalyticsControllerActionChannelRequest |  (optional)

    try:
        # List of channels
        api_response = api_instance.youtube_video_controller_action_channel(youtube_analytics_controller_action_channel_request=youtube_analytics_controller_action_channel_request)
        print("The response of ConnectorsYoutubeVideoApi->youtube_video_controller_action_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsYoutubeVideoApi->youtube_video_controller_action_channel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **youtube_analytics_controller_action_channel_request** | [**YoutubeAnalyticsControllerActionChannelRequest**](YoutubeAnalyticsControllerActionChannelRequest.md)|  | [optional] 

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
**200** | List of channels |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **youtube_video_controller_action_date_range**
> List[LabelValueResponseInner] youtube_video_controller_action_date_range()

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
    api_instance = openapi_client.ConnectorsYoutubeVideoApi(api_client)

    try:
        # List of date ranges
        api_response = api_instance.youtube_video_controller_action_date_range()
        print("The response of ConnectorsYoutubeVideoApi->youtube_video_controller_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsYoutubeVideoApi->youtube_video_controller_action_date_range: %s\n" % e)
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

# **youtube_video_controller_action_default_attribute**
> List[LabelValueResponseInner] youtube_video_controller_action_default_attribute()

List of attributes

List all attributes

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
    api_instance = openapi_client.ConnectorsYoutubeVideoApi(api_client)

    try:
        # List of attributes
        api_response = api_instance.youtube_video_controller_action_default_attribute()
        print("The response of ConnectorsYoutubeVideoApi->youtube_video_controller_action_default_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsYoutubeVideoApi->youtube_video_controller_action_default_attribute: %s\n" % e)
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
**200** | List of default attribute objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **youtube_video_controller_action_load**
> Source youtube_video_controller_action_load(youtube_video_connector_form=youtube_video_connector_form)

Create Youtube Video source

### Example


```python
import openapi_client
from openapi_client.models.source import Source
from openapi_client.models.youtube_video_connector_form import YoutubeVideoConnectorForm
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
    api_instance = openapi_client.ConnectorsYoutubeVideoApi(api_client)
    youtube_video_connector_form = openapi_client.YoutubeVideoConnectorForm() # YoutubeVideoConnectorForm |  (optional)

    try:
        # Create Youtube Video source
        api_response = api_instance.youtube_video_controller_action_load(youtube_video_connector_form=youtube_video_connector_form)
        print("The response of ConnectorsYoutubeVideoApi->youtube_video_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsYoutubeVideoApi->youtube_video_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **youtube_video_connector_form** | [**YoutubeVideoConnectorForm**](YoutubeVideoConnectorForm.md)|  | [optional] 

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

# **youtube_video_controller_action_playlist**
> List[LabelValueResponseInner] youtube_video_controller_action_playlist(youtube_analytics_controller_action_playlist_request=youtube_analytics_controller_action_playlist_request)

List of playlists

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.youtube_analytics_controller_action_playlist_request import YoutubeAnalyticsControllerActionPlaylistRequest
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
    api_instance = openapi_client.ConnectorsYoutubeVideoApi(api_client)
    youtube_analytics_controller_action_playlist_request = openapi_client.YoutubeAnalyticsControllerActionPlaylistRequest() # YoutubeAnalyticsControllerActionPlaylistRequest |  (optional)

    try:
        # List of playlists
        api_response = api_instance.youtube_video_controller_action_playlist(youtube_analytics_controller_action_playlist_request=youtube_analytics_controller_action_playlist_request)
        print("The response of ConnectorsYoutubeVideoApi->youtube_video_controller_action_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsYoutubeVideoApi->youtube_video_controller_action_playlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **youtube_analytics_controller_action_playlist_request** | [**YoutubeAnalyticsControllerActionPlaylistRequest**](YoutubeAnalyticsControllerActionPlaylistRequest.md)|  | [optional] 

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
**200** | List of playlists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **youtube_video_controller_action_preview**
> SuccessResponse youtube_video_controller_action_preview(youtube_video_connector_form=youtube_video_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.success_response import SuccessResponse
from openapi_client.models.youtube_video_connector_form import YoutubeVideoConnectorForm
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
    api_instance = openapi_client.ConnectorsYoutubeVideoApi(api_client)
    youtube_video_connector_form = openapi_client.YoutubeVideoConnectorForm() # YoutubeVideoConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.youtube_video_controller_action_preview(youtube_video_connector_form=youtube_video_connector_form)
        print("The response of ConnectorsYoutubeVideoApi->youtube_video_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsYoutubeVideoApi->youtube_video_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **youtube_video_connector_form** | [**YoutubeVideoConnectorForm**](YoutubeVideoConnectorForm.md)|  | [optional] 

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

