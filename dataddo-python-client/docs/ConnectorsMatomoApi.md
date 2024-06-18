# openapi_client.ConnectorsMatomoApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matomo_controller_action_site_id**](ConnectorsMatomoApi.md#matomo_controller_action_site_id) | **GET** /connectors/matomo/actions/siteId | List of Site Id&#39;s


# **matomo_controller_action_site_id**
> List[LabelValueResponseInner] matomo_controller_action_site_id()

List of Site Id's

Method for listing site id

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
    api_instance = openapi_client.ConnectorsMatomoApi(api_client)

    try:
        # List of Site Id's
        api_response = api_instance.matomo_controller_action_site_id()
        print("The response of ConnectorsMatomoApi->matomo_controller_action_site_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMatomoApi->matomo_controller_action_site_id: %s\n" % e)
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
**200** | List of Site Id&#39;s |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

