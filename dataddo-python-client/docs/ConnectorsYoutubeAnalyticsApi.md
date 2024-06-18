# openapi_client.ConnectorsYoutubeAnalyticsApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**youtube_analytics_controller_action_authorization**](ConnectorsYoutubeAnalyticsApi.md#youtube_analytics_controller_action_authorization) | **GET** /connectors/youtube_analytics/actions/authorization | List of authorization objects
[**youtube_analytics_controller_action_channel**](ConnectorsYoutubeAnalyticsApi.md#youtube_analytics_controller_action_channel) | **POST** /connectors/youtube_analytics/actions/channel | List of channels
[**youtube_analytics_controller_action_date_range**](ConnectorsYoutubeAnalyticsApi.md#youtube_analytics_controller_action_date_range) | **GET** /connectors/youtube_analytics/actions/dateRange | List of date ranges
[**youtube_analytics_controller_action_load**](ConnectorsYoutubeAnalyticsApi.md#youtube_analytics_controller_action_load) | **POST** /connectors/youtube_analytics/create-source | Create Youtube Analytics source
[**youtube_analytics_controller_action_playlist**](ConnectorsYoutubeAnalyticsApi.md#youtube_analytics_controller_action_playlist) | **POST** /connectors/youtube_analytics/actions/playlist | List of playlists
[**youtube_analytics_controller_action_preview**](ConnectorsYoutubeAnalyticsApi.md#youtube_analytics_controller_action_preview) | **POST** /connectors/youtube_analytics/preview | Preview the data
[**youtube_analytics_controller_action_template**](ConnectorsYoutubeAnalyticsApi.md#youtube_analytics_controller_action_template) | **GET** /connectors/youtube_analytics/templates/{id} | List Youtube Analytics of dataset template
[**youtube_analytics_controller_action_templates**](ConnectorsYoutubeAnalyticsApi.md#youtube_analytics_controller_action_templates) | **GET** /connectors/youtube_analytics/templates | List all Youtube Analytics dataset templates


# **youtube_analytics_controller_action_authorization**
> List[ActionAuthorizationResponseInner] youtube_analytics_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsYoutubeAnalyticsApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.youtube_analytics_controller_action_authorization()
        print("The response of ConnectorsYoutubeAnalyticsApi->youtube_analytics_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsYoutubeAnalyticsApi->youtube_analytics_controller_action_authorization: %s\n" % e)
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

# **youtube_analytics_controller_action_channel**
> List[LabelValueResponseInner] youtube_analytics_controller_action_channel(youtube_analytics_controller_action_channel_request=youtube_analytics_controller_action_channel_request)

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
    api_instance = openapi_client.ConnectorsYoutubeAnalyticsApi(api_client)
    youtube_analytics_controller_action_channel_request = openapi_client.YoutubeAnalyticsControllerActionChannelRequest() # YoutubeAnalyticsControllerActionChannelRequest |  (optional)

    try:
        # List of channels
        api_response = api_instance.youtube_analytics_controller_action_channel(youtube_analytics_controller_action_channel_request=youtube_analytics_controller_action_channel_request)
        print("The response of ConnectorsYoutubeAnalyticsApi->youtube_analytics_controller_action_channel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsYoutubeAnalyticsApi->youtube_analytics_controller_action_channel: %s\n" % e)
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

# **youtube_analytics_controller_action_date_range**
> List[LabelValueResponseInner] youtube_analytics_controller_action_date_range()

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
    api_instance = openapi_client.ConnectorsYoutubeAnalyticsApi(api_client)

    try:
        # List of date ranges
        api_response = api_instance.youtube_analytics_controller_action_date_range()
        print("The response of ConnectorsYoutubeAnalyticsApi->youtube_analytics_controller_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsYoutubeAnalyticsApi->youtube_analytics_controller_action_date_range: %s\n" % e)
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

# **youtube_analytics_controller_action_load**
> Source youtube_analytics_controller_action_load(youtube_analytics_connector_form=youtube_analytics_connector_form)

Create Youtube Analytics source

### Example


```python
import openapi_client
from openapi_client.models.source import Source
from openapi_client.models.youtube_analytics_connector_form import YoutubeAnalyticsConnectorForm
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
    api_instance = openapi_client.ConnectorsYoutubeAnalyticsApi(api_client)
    youtube_analytics_connector_form = openapi_client.YoutubeAnalyticsConnectorForm() # YoutubeAnalyticsConnectorForm |  (optional)

    try:
        # Create Youtube Analytics source
        api_response = api_instance.youtube_analytics_controller_action_load(youtube_analytics_connector_form=youtube_analytics_connector_form)
        print("The response of ConnectorsYoutubeAnalyticsApi->youtube_analytics_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsYoutubeAnalyticsApi->youtube_analytics_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **youtube_analytics_connector_form** | [**YoutubeAnalyticsConnectorForm**](YoutubeAnalyticsConnectorForm.md)|  | [optional] 

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

# **youtube_analytics_controller_action_playlist**
> List[LabelValueResponseInner] youtube_analytics_controller_action_playlist(youtube_analytics_controller_action_playlist_request=youtube_analytics_controller_action_playlist_request)

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
    api_instance = openapi_client.ConnectorsYoutubeAnalyticsApi(api_client)
    youtube_analytics_controller_action_playlist_request = openapi_client.YoutubeAnalyticsControllerActionPlaylistRequest() # YoutubeAnalyticsControllerActionPlaylistRequest |  (optional)

    try:
        # List of playlists
        api_response = api_instance.youtube_analytics_controller_action_playlist(youtube_analytics_controller_action_playlist_request=youtube_analytics_controller_action_playlist_request)
        print("The response of ConnectorsYoutubeAnalyticsApi->youtube_analytics_controller_action_playlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsYoutubeAnalyticsApi->youtube_analytics_controller_action_playlist: %s\n" % e)
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

# **youtube_analytics_controller_action_preview**
> SuccessResponse youtube_analytics_controller_action_preview(youtube_analytics_connector_form=youtube_analytics_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.success_response import SuccessResponse
from openapi_client.models.youtube_analytics_connector_form import YoutubeAnalyticsConnectorForm
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
    api_instance = openapi_client.ConnectorsYoutubeAnalyticsApi(api_client)
    youtube_analytics_connector_form = openapi_client.YoutubeAnalyticsConnectorForm() # YoutubeAnalyticsConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.youtube_analytics_controller_action_preview(youtube_analytics_connector_form=youtube_analytics_connector_form)
        print("The response of ConnectorsYoutubeAnalyticsApi->youtube_analytics_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsYoutubeAnalyticsApi->youtube_analytics_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **youtube_analytics_connector_form** | [**YoutubeAnalyticsConnectorForm**](YoutubeAnalyticsConnectorForm.md)|  | [optional] 

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

# **youtube_analytics_controller_action_template**
> object youtube_analytics_controller_action_template(id)

List Youtube Analytics of dataset template

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
    api_instance = openapi_client.ConnectorsYoutubeAnalyticsApi(api_client)
    id = 'id_example' # str | The id of the template to retrieve

    try:
        # List Youtube Analytics of dataset template
        api_response = api_instance.youtube_analytics_controller_action_template(id)
        print("The response of ConnectorsYoutubeAnalyticsApi->youtube_analytics_controller_action_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsYoutubeAnalyticsApi->youtube_analytics_controller_action_template: %s\n" % e)
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

# **youtube_analytics_controller_action_templates**
> ConnectorTemplateResponse youtube_analytics_controller_action_templates()

List all Youtube Analytics dataset templates

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
    api_instance = openapi_client.ConnectorsYoutubeAnalyticsApi(api_client)

    try:
        # List all Youtube Analytics dataset templates
        api_response = api_instance.youtube_analytics_controller_action_templates()
        print("The response of ConnectorsYoutubeAnalyticsApi->youtube_analytics_controller_action_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsYoutubeAnalyticsApi->youtube_analytics_controller_action_templates: %s\n" % e)
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
**200** | List all Youtube Analytics dataset templates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

