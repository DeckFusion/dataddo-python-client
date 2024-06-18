# openapi_client.ServicesSalesforceCustomDomainApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_authorizer_salesforce_custom_domain_salesforce_custom_domain_authorizer_new_o_auth_url**](ServicesSalesforceCustomDomainApi.md#app_authorizer_salesforce_custom_domain_salesforce_custom_domain_authorizer_new_o_auth_url) | **POST** /services/salesforce_custom_domain/oauth-request-url | Builds redirect URL


# **app_authorizer_salesforce_custom_domain_salesforce_custom_domain_authorizer_new_o_auth_url**
> OAuthRequestUrlResponse app_authorizer_salesforce_custom_domain_salesforce_custom_domain_authorizer_new_o_auth_url(app_authorizer_salesforce_custom_domain_salesforce_custom_domain_authorizer_new_o_auth_url_request)

Builds redirect URL

### Example


```python
import openapi_client
from openapi_client.models.app_authorizer_salesforce_custom_domain_salesforce_custom_domain_authorizer_new_o_auth_url_request import AppAuthorizerSalesforceCustomDomainSalesforceCustomDomainAuthorizerNewOAuthUrlRequest
from openapi_client.models.o_auth_request_url_response import OAuthRequestUrlResponse
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
    api_instance = openapi_client.ServicesSalesforceCustomDomainApi(api_client)
    app_authorizer_salesforce_custom_domain_salesforce_custom_domain_authorizer_new_o_auth_url_request = openapi_client.AppAuthorizerSalesforceCustomDomainSalesforceCustomDomainAuthorizerNewOAuthUrlRequest() # AppAuthorizerSalesforceCustomDomainSalesforceCustomDomainAuthorizerNewOAuthUrlRequest | 

    try:
        # Builds redirect URL
        api_response = api_instance.app_authorizer_salesforce_custom_domain_salesforce_custom_domain_authorizer_new_o_auth_url(app_authorizer_salesforce_custom_domain_salesforce_custom_domain_authorizer_new_o_auth_url_request)
        print("The response of ServicesSalesforceCustomDomainApi->app_authorizer_salesforce_custom_domain_salesforce_custom_domain_authorizer_new_o_auth_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesSalesforceCustomDomainApi->app_authorizer_salesforce_custom_domain_salesforce_custom_domain_authorizer_new_o_auth_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_authorizer_salesforce_custom_domain_salesforce_custom_domain_authorizer_new_o_auth_url_request** | [**AppAuthorizerSalesforceCustomDomainSalesforceCustomDomainAuthorizerNewOAuthUrlRequest**](AppAuthorizerSalesforceCustomDomainSalesforceCustomDomainAuthorizerNewOAuthUrlRequest.md)|  | 

### Return type

[**OAuthRequestUrlResponse**](OAuthRequestUrlResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the redirect URL |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

