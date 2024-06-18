# openapi_client.ServicesZohoApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_authorizer_zoho_zoho_authorizer_action_country**](ServicesZohoApi.md#app_authorizer_zoho_zoho_authorizer_action_country) | **GET** /services/zoho/actions/country | List of countries


# **app_authorizer_zoho_zoho_authorizer_action_country**
> List[LabelValueResponseInner] app_authorizer_zoho_zoho_authorizer_action_country()

List of countries

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
    api_instance = openapi_client.ServicesZohoApi(api_client)

    try:
        # List of countries
        api_response = api_instance.app_authorizer_zoho_zoho_authorizer_action_country()
        print("The response of ServicesZohoApi->app_authorizer_zoho_zoho_authorizer_action_country:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesZohoApi->app_authorizer_zoho_zoho_authorizer_action_country: %s\n" % e)
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
**200** | List of countries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

