# openapi_client.ConnectorsBlackDiamondExtractorApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**black_diamond_extractor_controller_action_load**](ConnectorsBlackDiamondExtractorApi.md#black_diamond_extractor_controller_action_load) | **POST** /connectors/black_diamond_extractor/create-source | Create Black Diamond Extractor source
[**black_diamond_extractor_controller_action_preview**](ConnectorsBlackDiamondExtractorApi.md#black_diamond_extractor_controller_action_preview) | **POST** /connectors/black_diamond_extractor/preview | Preview the data


# **black_diamond_extractor_controller_action_load**
> Source black_diamond_extractor_controller_action_load(black_diamond_extractor_connector_form=black_diamond_extractor_connector_form)

Create Black Diamond Extractor source

### Example


```python
import openapi_client
from openapi_client.models.black_diamond_extractor_connector_form import BlackDiamondExtractorConnectorForm
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
    api_instance = openapi_client.ConnectorsBlackDiamondExtractorApi(api_client)
    black_diamond_extractor_connector_form = openapi_client.BlackDiamondExtractorConnectorForm() # BlackDiamondExtractorConnectorForm |  (optional)

    try:
        # Create Black Diamond Extractor source
        api_response = api_instance.black_diamond_extractor_controller_action_load(black_diamond_extractor_connector_form=black_diamond_extractor_connector_form)
        print("The response of ConnectorsBlackDiamondExtractorApi->black_diamond_extractor_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsBlackDiamondExtractorApi->black_diamond_extractor_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **black_diamond_extractor_connector_form** | [**BlackDiamondExtractorConnectorForm**](BlackDiamondExtractorConnectorForm.md)|  | [optional] 

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

# **black_diamond_extractor_controller_action_preview**
> SuccessResponse black_diamond_extractor_controller_action_preview(black_diamond_extractor_connector_form=black_diamond_extractor_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.black_diamond_extractor_connector_form import BlackDiamondExtractorConnectorForm
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
    api_instance = openapi_client.ConnectorsBlackDiamondExtractorApi(api_client)
    black_diamond_extractor_connector_form = openapi_client.BlackDiamondExtractorConnectorForm() # BlackDiamondExtractorConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.black_diamond_extractor_controller_action_preview(black_diamond_extractor_connector_form=black_diamond_extractor_connector_form)
        print("The response of ConnectorsBlackDiamondExtractorApi->black_diamond_extractor_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsBlackDiamondExtractorApi->black_diamond_extractor_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **black_diamond_extractor_connector_form** | [**BlackDiamondExtractorConnectorForm**](BlackDiamondExtractorConnectorForm.md)|  | [optional] 

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

