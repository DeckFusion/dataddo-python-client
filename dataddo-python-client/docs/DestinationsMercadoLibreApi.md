# openapi_client.DestinationsMercadoLibreApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_mercado_libre_mercado_libre_connector_action_site_id**](DestinationsMercadoLibreApi.md#app_connector_mercado_libre_mercado_libre_connector_action_site_id) | **GET** /destinations/mercado_libre/actions/siteId | Mercado Libre Site Ids


# **app_connector_mercado_libre_mercado_libre_connector_action_site_id**
> List[LabelValueResponseInner] app_connector_mercado_libre_mercado_libre_connector_action_site_id()

Mercado Libre Site Ids

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
    api_instance = openapi_client.DestinationsMercadoLibreApi(api_client)

    try:
        # Mercado Libre Site Ids
        api_response = api_instance.app_connector_mercado_libre_mercado_libre_connector_action_site_id()
        print("The response of DestinationsMercadoLibreApi->app_connector_mercado_libre_mercado_libre_connector_action_site_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DestinationsMercadoLibreApi->app_connector_mercado_libre_mercado_libre_connector_action_site_id: %s\n" % e)
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
**200** | Mercado Libre Site Ids |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

