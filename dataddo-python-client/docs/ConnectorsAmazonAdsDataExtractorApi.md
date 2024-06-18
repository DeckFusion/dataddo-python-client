# openapi_client.ConnectorsAmazonAdsDataExtractorApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**amazon_ads_data_extractor_controller_action_load**](ConnectorsAmazonAdsDataExtractorApi.md#amazon_ads_data_extractor_controller_action_load) | **POST** /connectors/amazon_ads_data_extractor/create-source | Create Amazon Ads Data Extractor source
[**amazon_ads_data_extractor_controller_action_preview**](ConnectorsAmazonAdsDataExtractorApi.md#amazon_ads_data_extractor_controller_action_preview) | **POST** /connectors/amazon_ads_data_extractor/preview | Preview the data


# **amazon_ads_data_extractor_controller_action_load**
> Source amazon_ads_data_extractor_controller_action_load(amazon_ads_data_extractor_connector_form=amazon_ads_data_extractor_connector_form)

Create Amazon Ads Data Extractor source

### Example


```python
import openapi_client
from openapi_client.models.amazon_ads_data_extractor_connector_form import AmazonAdsDataExtractorConnectorForm
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
    api_instance = openapi_client.ConnectorsAmazonAdsDataExtractorApi(api_client)
    amazon_ads_data_extractor_connector_form = openapi_client.AmazonAdsDataExtractorConnectorForm() # AmazonAdsDataExtractorConnectorForm |  (optional)

    try:
        # Create Amazon Ads Data Extractor source
        api_response = api_instance.amazon_ads_data_extractor_controller_action_load(amazon_ads_data_extractor_connector_form=amazon_ads_data_extractor_connector_form)
        print("The response of ConnectorsAmazonAdsDataExtractorApi->amazon_ads_data_extractor_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAmazonAdsDataExtractorApi->amazon_ads_data_extractor_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_ads_data_extractor_connector_form** | [**AmazonAdsDataExtractorConnectorForm**](AmazonAdsDataExtractorConnectorForm.md)|  | [optional] 

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

# **amazon_ads_data_extractor_controller_action_preview**
> SuccessResponse amazon_ads_data_extractor_controller_action_preview(amazon_ads_data_extractor_connector_form=amazon_ads_data_extractor_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.amazon_ads_data_extractor_connector_form import AmazonAdsDataExtractorConnectorForm
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
    api_instance = openapi_client.ConnectorsAmazonAdsDataExtractorApi(api_client)
    amazon_ads_data_extractor_connector_form = openapi_client.AmazonAdsDataExtractorConnectorForm() # AmazonAdsDataExtractorConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.amazon_ads_data_extractor_controller_action_preview(amazon_ads_data_extractor_connector_form=amazon_ads_data_extractor_connector_form)
        print("The response of ConnectorsAmazonAdsDataExtractorApi->amazon_ads_data_extractor_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAmazonAdsDataExtractorApi->amazon_ads_data_extractor_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_ads_data_extractor_connector_form** | [**AmazonAdsDataExtractorConnectorForm**](AmazonAdsDataExtractorConnectorForm.md)|  | [optional] 

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

