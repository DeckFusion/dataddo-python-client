# openapi_client.AccountsApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_controller_delete_customer_member**](AccountsApi.md#account_controller_delete_customer_member) | **DELETE** /customers/{id}/members/{memberId} | 
[**account_controller_delete_invited_member**](AccountsApi.md#account_controller_delete_invited_member) | **DELETE** /invite-member/{base64Email} | 
[**account_controller_delete_invited_member_by_id**](AccountsApi.md#account_controller_delete_invited_member_by_id) | **DELETE** /invite-member-by-id/{invitedRequestId} | 
[**account_controller_get_customer_invited_members**](AccountsApi.md#account_controller_get_customer_invited_members) | **GET** /customers/{id}/invited-members | 
[**account_controller_get_customer_members**](AccountsApi.md#account_controller_get_customer_members) | **GET** /customers/{id}/members | 
[**account_controller_invite_member**](AccountsApi.md#account_controller_invite_member) | **POST** /invite-member | 


# **account_controller_delete_customer_member**
> account_controller_delete_customer_member(id, member_id)



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
    api_instance = openapi_client.AccountsApi(api_client)
    id = 'id_example' # str | 
    member_id = 'member_id_example' # str | 

    try:
        api_instance.account_controller_delete_customer_member(id, member_id)
    except Exception as e:
        print("Exception when calling AccountsApi->account_controller_delete_customer_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **member_id** | **str**|  | 

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

# **account_controller_delete_invited_member**
> account_controller_delete_invited_member(base64_email)



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
    api_instance = openapi_client.AccountsApi(api_client)
    base64_email = 'base64_email_example' # str | 

    try:
        api_instance.account_controller_delete_invited_member(base64_email)
    except Exception as e:
        print("Exception when calling AccountsApi->account_controller_delete_invited_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base64_email** | **str**|  | 

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
**204** | Cancels member invitation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_controller_delete_invited_member_by_id**
> account_controller_delete_invited_member_by_id(invited_request_id)



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
    api_instance = openapi_client.AccountsApi(api_client)
    invited_request_id = 'invited_request_id_example' # str | 

    try:
        api_instance.account_controller_delete_invited_member_by_id(invited_request_id)
    except Exception as e:
        print("Exception when calling AccountsApi->account_controller_delete_invited_member_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invited_request_id** | **str**|  | 

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
**204** | Cancels member invitation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_controller_get_customer_invited_members**
> MemberRequest account_controller_get_customer_invited_members(id)



### Example


```python
import openapi_client
from openapi_client.models.member_request import MemberRequest
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
    api_instance = openapi_client.AccountsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.account_controller_get_customer_invited_members(id)
        print("The response of AccountsApi->account_controller_get_customer_invited_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->account_controller_get_customer_invited_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**MemberRequest**](MemberRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get list of invited members |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_controller_get_customer_members**
> List[Member] account_controller_get_customer_members(id)



### Example


```python
import openapi_client
from openapi_client.models.member import Member
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
    api_instance = openapi_client.AccountsApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.account_controller_get_customer_members(id)
        print("The response of AccountsApi->account_controller_get_customer_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->account_controller_get_customer_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[Member]**](Member.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get customer members |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_controller_invite_member**
> account_controller_invite_member(create_member_request)



### Example


```python
import openapi_client
from openapi_client.models.create_member_request import CreateMemberRequest
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
    api_instance = openapi_client.AccountsApi(api_client)
    create_member_request = openapi_client.CreateMemberRequest() # CreateMemberRequest | 

    try:
        api_instance.account_controller_invite_member(create_member_request)
    except Exception as e:
        print("Exception when calling AccountsApi->account_controller_invite_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_member_request** | [**CreateMemberRequest**](CreateMemberRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Create user/member |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

