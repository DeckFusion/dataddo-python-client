# openapi_client.ServicesAwsMssqlApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_authorizer_aws_mssql_aws_mssql_authorizer_create_service**](ServicesAwsMssqlApi.md#app_authorizer_aws_mssql_aws_mssql_authorizer_create_service) | **POST** /services/aws_mssql | Create service


# **app_authorizer_aws_mssql_aws_mssql_authorizer_create_service**
> AwsMssqlUserAuth app_authorizer_aws_mssql_aws_mssql_authorizer_create_service(app_authorizer_aws_mssql_aws_mssql_authorizer_create_service_request)

Create service

### Example


```python
import openapi_client
from openapi_client.models.app_authorizer_aws_mssql_aws_mssql_authorizer_create_service_request import AppAuthorizerAwsMssqlAwsMssqlAuthorizerCreateServiceRequest
from openapi_client.models.aws_mssql_user_auth import AwsMssqlUserAuth
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
    api_instance = openapi_client.ServicesAwsMssqlApi(api_client)
    app_authorizer_aws_mssql_aws_mssql_authorizer_create_service_request = openapi_client.AppAuthorizerAwsMssqlAwsMssqlAuthorizerCreateServiceRequest() # AppAuthorizerAwsMssqlAwsMssqlAuthorizerCreateServiceRequest | 

    try:
        # Create service
        api_response = api_instance.app_authorizer_aws_mssql_aws_mssql_authorizer_create_service(app_authorizer_aws_mssql_aws_mssql_authorizer_create_service_request)
        print("The response of ServicesAwsMssqlApi->app_authorizer_aws_mssql_aws_mssql_authorizer_create_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesAwsMssqlApi->app_authorizer_aws_mssql_aws_mssql_authorizer_create_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_authorizer_aws_mssql_aws_mssql_authorizer_create_service_request** | [**AppAuthorizerAwsMssqlAwsMssqlAuthorizerCreateServiceRequest**](AppAuthorizerAwsMssqlAwsMssqlAuthorizerCreateServiceRequest.md)|  | 

### Return type

[**AwsMssqlUserAuth**](AwsMssqlUserAuth.md)

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

