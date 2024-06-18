# openapi_client.ServicesGoogleMysqlApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_authorizer_google_mysql_google_mysql_authorizer_action_tls**](ServicesGoogleMysqlApi.md#app_authorizer_google_mysql_google_mysql_authorizer_action_tls) | **GET** /services/google_mysql/actions/tls | List of TLS options
[**app_authorizer_google_mysql_google_mysql_authorizer_create_service**](ServicesGoogleMysqlApi.md#app_authorizer_google_mysql_google_mysql_authorizer_create_service) | **POST** /services/google_mysql | Create service


# **app_authorizer_google_mysql_google_mysql_authorizer_action_tls**
> List[LabelValueResponseInner] app_authorizer_google_mysql_google_mysql_authorizer_action_tls()

List of TLS options

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
    api_instance = openapi_client.ServicesGoogleMysqlApi(api_client)

    try:
        # List of TLS options
        api_response = api_instance.app_authorizer_google_mysql_google_mysql_authorizer_action_tls()
        print("The response of ServicesGoogleMysqlApi->app_authorizer_google_mysql_google_mysql_authorizer_action_tls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesGoogleMysqlApi->app_authorizer_google_mysql_google_mysql_authorizer_action_tls: %s\n" % e)
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
**200** | List of TLS options |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_authorizer_google_mysql_google_mysql_authorizer_create_service**
> GoogleMysqlUserAuth app_authorizer_google_mysql_google_mysql_authorizer_create_service(app_authorizer_google_mysql_google_mysql_authorizer_create_service_request)

Create service

### Example


```python
import openapi_client
from openapi_client.models.app_authorizer_google_mysql_google_mysql_authorizer_create_service_request import AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest
from openapi_client.models.google_mysql_user_auth import GoogleMysqlUserAuth
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
    api_instance = openapi_client.ServicesGoogleMysqlApi(api_client)
    app_authorizer_google_mysql_google_mysql_authorizer_create_service_request = openapi_client.AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest() # AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest | 

    try:
        # Create service
        api_response = api_instance.app_authorizer_google_mysql_google_mysql_authorizer_create_service(app_authorizer_google_mysql_google_mysql_authorizer_create_service_request)
        print("The response of ServicesGoogleMysqlApi->app_authorizer_google_mysql_google_mysql_authorizer_create_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesGoogleMysqlApi->app_authorizer_google_mysql_google_mysql_authorizer_create_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_authorizer_google_mysql_google_mysql_authorizer_create_service_request** | [**AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest**](AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest.md)|  | 

### Return type

[**GoogleMysqlUserAuth**](GoogleMysqlUserAuth.md)

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

