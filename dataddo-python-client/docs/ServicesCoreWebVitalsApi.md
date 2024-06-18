# openapi_client.ServicesCoreWebVitalsApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_authorizer_core_web_vitals_core_web_vitals_authorizer_create_service**](ServicesCoreWebVitalsApi.md#app_authorizer_core_web_vitals_core_web_vitals_authorizer_create_service) | **POST** /services/core_web_vitals | Create service


# **app_authorizer_core_web_vitals_core_web_vitals_authorizer_create_service**
> CoreWebVitalsUserAuth app_authorizer_core_web_vitals_core_web_vitals_authorizer_create_service(app_authorizer_core_web_vitals_core_web_vitals_authorizer_create_service_request)

Create service

### Example


```python
import openapi_client
from openapi_client.models.app_authorizer_core_web_vitals_core_web_vitals_authorizer_create_service_request import AppAuthorizerCoreWebVitalsCoreWebVitalsAuthorizerCreateServiceRequest
from openapi_client.models.core_web_vitals_user_auth import CoreWebVitalsUserAuth
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
    api_instance = openapi_client.ServicesCoreWebVitalsApi(api_client)
    app_authorizer_core_web_vitals_core_web_vitals_authorizer_create_service_request = openapi_client.AppAuthorizerCoreWebVitalsCoreWebVitalsAuthorizerCreateServiceRequest() # AppAuthorizerCoreWebVitalsCoreWebVitalsAuthorizerCreateServiceRequest | 

    try:
        # Create service
        api_response = api_instance.app_authorizer_core_web_vitals_core_web_vitals_authorizer_create_service(app_authorizer_core_web_vitals_core_web_vitals_authorizer_create_service_request)
        print("The response of ServicesCoreWebVitalsApi->app_authorizer_core_web_vitals_core_web_vitals_authorizer_create_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesCoreWebVitalsApi->app_authorizer_core_web_vitals_core_web_vitals_authorizer_create_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_authorizer_core_web_vitals_core_web_vitals_authorizer_create_service_request** | [**AppAuthorizerCoreWebVitalsCoreWebVitalsAuthorizerCreateServiceRequest**](AppAuthorizerCoreWebVitalsCoreWebVitalsAuthorizerCreateServiceRequest.md)|  | 

### Return type

[**CoreWebVitalsUserAuth**](CoreWebVitalsUserAuth.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

