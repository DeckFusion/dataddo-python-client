# openapi_client.ConnectorsOdooApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_odoo_odoo_connector_action_authorization**](ConnectorsOdooApi.md#app_connector_odoo_odoo_connector_action_authorization) | **GET** /connectors/odoo/actions/authorization | List of authorization objects
[**app_connector_odoo_odoo_connector_action_list_columns**](ConnectorsOdooApi.md#app_connector_odoo_odoo_connector_action_list_columns) | **GET** /connectors/odoo/actions/list-columns | List of columns
[**app_connector_odoo_odoo_connector_action_list_models**](ConnectorsOdooApi.md#app_connector_odoo_odoo_connector_action_list_models) | **GET** /connectors/odoo/actions/list-models | List of models


# **app_connector_odoo_odoo_connector_action_authorization**
> List[ActionAuthorizationResponseInner] app_connector_odoo_odoo_connector_action_authorization()

List of authorization objects

### Example


```python
import openapi_client
from openapi_client.models.action_authorization_response_inner import ActionAuthorizationResponseInner
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
    api_instance = openapi_client.ConnectorsOdooApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_connector_odoo_odoo_connector_action_authorization()
        print("The response of ConnectorsOdooApi->app_connector_odoo_odoo_connector_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsOdooApi->app_connector_odoo_odoo_connector_action_authorization: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ActionAuthorizationResponseInner]**](ActionAuthorizationResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of authorization objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_odoo_odoo_connector_action_list_columns**
> List[LabelValueResponseInner] app_connector_odoo_odoo_connector_action_list_columns()

List of columns

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
    api_instance = openapi_client.ConnectorsOdooApi(api_client)

    try:
        # List of columns
        api_response = api_instance.app_connector_odoo_odoo_connector_action_list_columns()
        print("The response of ConnectorsOdooApi->app_connector_odoo_odoo_connector_action_list_columns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsOdooApi->app_connector_odoo_odoo_connector_action_list_columns: %s\n" % e)
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
**200** | List of columns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_odoo_odoo_connector_action_list_models**
> List[LabelValueResponseInner] app_connector_odoo_odoo_connector_action_list_models()

List of models

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
    api_instance = openapi_client.ConnectorsOdooApi(api_client)

    try:
        # List of models
        api_response = api_instance.app_connector_odoo_odoo_connector_action_list_models()
        print("The response of ConnectorsOdooApi->app_connector_odoo_odoo_connector_action_list_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsOdooApi->app_connector_odoo_odoo_connector_action_list_models: %s\n" % e)
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
**200** | List of models |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

