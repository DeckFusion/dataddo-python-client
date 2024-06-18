# openapi_client.ServicesS3Api

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_authorizer_s3_s3_authorizer_create_service**](ServicesS3Api.md#app_authorizer_s3_s3_authorizer_create_service) | **POST** /services/s3 | Create service


# **app_authorizer_s3_s3_authorizer_create_service**
> S3UserAuth app_authorizer_s3_s3_authorizer_create_service(app_authorizer_s3_s3_authorizer_create_service_request)

Create service

### Example


```python
import openapi_client
from openapi_client.models.app_authorizer_s3_s3_authorizer_create_service_request import AppAuthorizerS3S3AuthorizerCreateServiceRequest
from openapi_client.models.s3_user_auth import S3UserAuth
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
    api_instance = openapi_client.ServicesS3Api(api_client)
    app_authorizer_s3_s3_authorizer_create_service_request = openapi_client.AppAuthorizerS3S3AuthorizerCreateServiceRequest() # AppAuthorizerS3S3AuthorizerCreateServiceRequest | 

    try:
        # Create service
        api_response = api_instance.app_authorizer_s3_s3_authorizer_create_service(app_authorizer_s3_s3_authorizer_create_service_request)
        print("The response of ServicesS3Api->app_authorizer_s3_s3_authorizer_create_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesS3Api->app_authorizer_s3_s3_authorizer_create_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_authorizer_s3_s3_authorizer_create_service_request** | [**AppAuthorizerS3S3AuthorizerCreateServiceRequest**](AppAuthorizerS3S3AuthorizerCreateServiceRequest.md)|  | 

### Return type

[**S3UserAuth**](S3UserAuth.md)

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

