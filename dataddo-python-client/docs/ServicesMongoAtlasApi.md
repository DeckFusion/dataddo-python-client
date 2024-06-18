# openapi_client.ServicesMongoAtlasApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_authorizer_mongo_atlas_mongo_atlas_authorizer_create_service**](ServicesMongoAtlasApi.md#app_authorizer_mongo_atlas_mongo_atlas_authorizer_create_service) | **POST** /services/mongo_atlas | Create service


# **app_authorizer_mongo_atlas_mongo_atlas_authorizer_create_service**
> MongoAtlasUserAuth app_authorizer_mongo_atlas_mongo_atlas_authorizer_create_service(app_authorizer_mongo_atlas_mongo_atlas_authorizer_create_service_request)

Create service

### Example


```python
import openapi_client
from openapi_client.models.app_authorizer_mongo_atlas_mongo_atlas_authorizer_create_service_request import AppAuthorizerMongoAtlasMongoAtlasAuthorizerCreateServiceRequest
from openapi_client.models.mongo_atlas_user_auth import MongoAtlasUserAuth
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
    api_instance = openapi_client.ServicesMongoAtlasApi(api_client)
    app_authorizer_mongo_atlas_mongo_atlas_authorizer_create_service_request = openapi_client.AppAuthorizerMongoAtlasMongoAtlasAuthorizerCreateServiceRequest() # AppAuthorizerMongoAtlasMongoAtlasAuthorizerCreateServiceRequest | 

    try:
        # Create service
        api_response = api_instance.app_authorizer_mongo_atlas_mongo_atlas_authorizer_create_service(app_authorizer_mongo_atlas_mongo_atlas_authorizer_create_service_request)
        print("The response of ServicesMongoAtlasApi->app_authorizer_mongo_atlas_mongo_atlas_authorizer_create_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesMongoAtlasApi->app_authorizer_mongo_atlas_mongo_atlas_authorizer_create_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_authorizer_mongo_atlas_mongo_atlas_authorizer_create_service_request** | [**AppAuthorizerMongoAtlasMongoAtlasAuthorizerCreateServiceRequest**](AppAuthorizerMongoAtlasMongoAtlasAuthorizerCreateServiceRequest.md)|  | 

### Return type

[**MongoAtlasUserAuth**](MongoAtlasUserAuth.md)

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

