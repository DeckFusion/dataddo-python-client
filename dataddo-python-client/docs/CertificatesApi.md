# openapi_client.CertificatesApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificate_controller_create**](CertificatesApi.md#certificate_controller_create) | **POST** /certificates | 
[**certificate_controller_delete**](CertificatesApi.md#certificate_controller_delete) | **DELETE** /certificates/{id} | 
[**certificate_controller_detail**](CertificatesApi.md#certificate_controller_detail) | **GET** /certificates/{id} | 
[**certificate_controller_list**](CertificatesApi.md#certificate_controller_list) | **GET** /certificates | 


# **certificate_controller_create**
> Certificate certificate_controller_create(create_certificate_request)



### Example


```python
import openapi_client
from openapi_client.models.certificate import Certificate
from openapi_client.models.create_certificate_request import CreateCertificateRequest
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
    api_instance = openapi_client.CertificatesApi(api_client)
    create_certificate_request = openapi_client.CreateCertificateRequest() # CreateCertificateRequest | 

    try:
        api_response = api_instance.certificate_controller_create(create_certificate_request)
        print("The response of CertificatesApi->certificate_controller_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->certificate_controller_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_certificate_request** | [**CreateCertificateRequest**](CreateCertificateRequest.md)|  | 

### Return type

[**Certificate**](Certificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **certificate_controller_delete**
> certificate_controller_delete(id)



### Example


```python
import openapi_client
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
    api_instance = openapi_client.CertificatesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.certificate_controller_delete(id)
    except Exception as e:
        print("Exception when calling CertificatesApi->certificate_controller_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **certificate_controller_detail**
> Certificate certificate_controller_detail(id)



### Example


```python
import openapi_client
from openapi_client.models.certificate import Certificate
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
    api_instance = openapi_client.CertificatesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.certificate_controller_detail(id)
        print("The response of CertificatesApi->certificate_controller_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->certificate_controller_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Certificate**](Certificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get certificate detail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **certificate_controller_list**
> Certificate certificate_controller_list()



### Example


```python
import openapi_client
from openapi_client.models.certificate import Certificate
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
    api_instance = openapi_client.CertificatesApi(api_client)

    try:
        api_response = api_instance.certificate_controller_list()
        print("The response of CertificatesApi->certificate_controller_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificatesApi->certificate_controller_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Certificate**](Certificate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get list of certificates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

