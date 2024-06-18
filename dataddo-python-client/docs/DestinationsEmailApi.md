# openapi_client.DestinationsEmailApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_destination_email_email_destination_action_attachment_formats**](DestinationsEmailApi.md#app_destination_email_email_destination_action_attachment_formats) | **POST** /destinations/email/actions/attachmentFormats | List email attachment formats
[**app_destination_email_email_destination_action_write_modes**](DestinationsEmailApi.md#app_destination_email_email_destination_action_write_modes) | **POST** /destinations/email/actions/writeModes | List of write modes


# **app_destination_email_email_destination_action_attachment_formats**
> List[LabelValueResponseInner] app_destination_email_email_destination_action_attachment_formats(app_destination_email_email_destination_action_attachment_formats_request=app_destination_email_email_destination_action_attachment_formats_request)

List email attachment formats

### Example


```python
import openapi_client
from openapi_client.models.app_destination_email_email_destination_action_attachment_formats_request import AppDestinationEmailEmailDestinationActionAttachmentFormatsRequest
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
    api_instance = openapi_client.DestinationsEmailApi(api_client)
    app_destination_email_email_destination_action_attachment_formats_request = openapi_client.AppDestinationEmailEmailDestinationActionAttachmentFormatsRequest() # AppDestinationEmailEmailDestinationActionAttachmentFormatsRequest |  (optional)

    try:
        # List email attachment formats
        api_response = api_instance.app_destination_email_email_destination_action_attachment_formats(app_destination_email_email_destination_action_attachment_formats_request=app_destination_email_email_destination_action_attachment_formats_request)
        print("The response of DestinationsEmailApi->app_destination_email_email_destination_action_attachment_formats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsEmailApi->app_destination_email_email_destination_action_attachment_formats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_destination_email_email_destination_action_attachment_formats_request** | [**AppDestinationEmailEmailDestinationActionAttachmentFormatsRequest**](AppDestinationEmailEmailDestinationActionAttachmentFormatsRequest.md)|  | [optional] 

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
**200** | List email attachment formats |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_destination_email_email_destination_action_write_modes**
> List[LabelValueResponseInner] app_destination_email_email_destination_action_write_modes(app_destination_alloy_db_alloy_db_destination_action_write_modes_request=app_destination_alloy_db_alloy_db_destination_action_write_modes_request)

List of write modes

### Example


```python
import openapi_client
from openapi_client.models.app_destination_alloy_db_alloy_db_destination_action_write_modes_request import AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest
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
    api_instance = openapi_client.DestinationsEmailApi(api_client)
    app_destination_alloy_db_alloy_db_destination_action_write_modes_request = openapi_client.AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest() # AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest |  (optional)

    try:
        # List of write modes
        api_response = api_instance.app_destination_email_email_destination_action_write_modes(app_destination_alloy_db_alloy_db_destination_action_write_modes_request=app_destination_alloy_db_alloy_db_destination_action_write_modes_request)
        print("The response of DestinationsEmailApi->app_destination_email_email_destination_action_write_modes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsEmailApi->app_destination_email_email_destination_action_write_modes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_destination_alloy_db_alloy_db_destination_action_write_modes_request** | [**AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest**](AppDestinationAlloyDbAlloyDbDestinationActionWriteModesRequest.md)|  | [optional] 

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
**200** | List of write modes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

