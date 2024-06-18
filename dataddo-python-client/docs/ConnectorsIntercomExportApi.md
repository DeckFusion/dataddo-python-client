# openapi_client.ConnectorsIntercomExportApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_intercom_export_intercom_export_connector_action_date_range**](ConnectorsIntercomExportApi.md#app_connector_intercom_export_intercom_export_connector_action_date_range) | **GET** /connectors/intercom_export/actions/dateRange | Method for listing date range
[**app_connector_intercom_export_intercom_export_connector_preview**](ConnectorsIntercomExportApi.md#app_connector_intercom_export_intercom_export_connector_preview) | **POST** /connectors/intercom_export/preview | Data preview


# **app_connector_intercom_export_intercom_export_connector_action_date_range**
> List[LabelValueResponseInner] app_connector_intercom_export_intercom_export_connector_action_date_range()

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
    api_instance = openapi_client.ConnectorsIntercomExportApi(api_client)

    try:
        # Method for listing date range
        api_response = api_instance.app_connector_intercom_export_intercom_export_connector_action_date_range()
        print("The response of ConnectorsIntercomExportApi->app_connector_intercom_export_intercom_export_connector_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsIntercomExportApi->app_connector_intercom_export_intercom_export_connector_action_date_range: %s\n" % e)
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
**200** | List of Intercom date ranges |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_intercom_export_intercom_export_connector_preview**
> SuccessResponse app_connector_intercom_export_intercom_export_connector_preview(intercom_export_dto=intercom_export_dto)

Data preview

### Example


```python
import openapi_client
from openapi_client.models.intercom_export_dto import IntercomExportDto
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
    api_instance = openapi_client.ConnectorsIntercomExportApi(api_client)
    intercom_export_dto = openapi_client.IntercomExportDto() # IntercomExportDto |  (optional)

    try:
        # Data preview
        api_response = api_instance.app_connector_intercom_export_intercom_export_connector_preview(intercom_export_dto=intercom_export_dto)
        print("The response of ConnectorsIntercomExportApi->app_connector_intercom_export_intercom_export_connector_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsIntercomExportApi->app_connector_intercom_export_intercom_export_connector_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **intercom_export_dto** | [**IntercomExportDto**](IntercomExportDto.md)|  | [optional] 

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

