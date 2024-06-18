# openapi_client.WellKnownApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**well_known_controller_keys**](WellKnownApi.md#well_known_controller_keys) | **GET** /.well-known/jwks.json | 


# **well_known_controller_keys**
> WellKnownControllerKeys200Response well_known_controller_keys()



### Example


```python
import openapi_client
from openapi_client.models.well_known_controller_keys200_response import WellKnownControllerKeys200Response
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
    api_instance = openapi_client.WellKnownApi(api_client)

    try:
        api_response = api_instance.well_known_controller_keys()
        print("The response of WellKnownApi->well_known_controller_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WellKnownApi->well_known_controller_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WellKnownControllerKeys200Response**](WellKnownControllerKeys200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | keys |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

