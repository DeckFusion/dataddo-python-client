# openapi_client.ConnectorsMssqlApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_mssql_mssql_connector_action_authorization**](ConnectorsMssqlApi.md#app_connector_mssql_mssql_connector_action_authorization) | **GET** /connectors/mssql/actions/authorization | List of authorization objects
[**app_connector_mssql_mssql_connector_action_generate_sql_queries**](ConnectorsMssqlApi.md#app_connector_mssql_mssql_connector_action_generate_sql_queries) | **GET** /connectors/mssql/actions/generateSQLQueries | Get generated SQL queries
[**app_connector_mssql_mssql_connector_action_list_columns**](ConnectorsMssqlApi.md#app_connector_mssql_mssql_connector_action_list_columns) | **POST** /connectors/mssql/actions/listColumns | List of table columns
[**app_connector_mssql_mssql_connector_action_list_tables**](ConnectorsMssqlApi.md#app_connector_mssql_mssql_connector_action_list_tables) | **POST** /connectors/mssql/actions/listTables | List of database tables
[**app_connector_mssql_mssql_connector_action_sql**](ConnectorsMssqlApi.md#app_connector_mssql_mssql_connector_action_sql) | **POST** /connectors/mssql/actions/sql | Get generated SQL
[**app_connector_mssql_mssql_connector_create_source**](ConnectorsMssqlApi.md#app_connector_mssql_mssql_connector_create_source) | **POST** /connectors/mssql/create-source | Create Mssql source
[**app_connector_mssql_mssql_connector_preview**](ConnectorsMssqlApi.md#app_connector_mssql_mssql_connector_preview) | **POST** /connectors/mssql/preview | Data preview


# **app_connector_mssql_mssql_connector_action_authorization**
> List[ActionAuthorizationResponseInner] app_connector_mssql_mssql_connector_action_authorization()

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
    api_instance = openapi_client.ConnectorsMssqlApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_connector_mssql_mssql_connector_action_authorization()
        print("The response of ConnectorsMssqlApi->app_connector_mssql_mssql_connector_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMssqlApi->app_connector_mssql_mssql_connector_action_authorization: %s\n" % e)
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

# **app_connector_mssql_mssql_connector_action_generate_sql_queries**
> List[LabelValueResponseInner] app_connector_mssql_mssql_connector_action_generate_sql_queries()

Get generated SQL queries

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
    api_instance = openapi_client.ConnectorsMssqlApi(api_client)

    try:
        # Get generated SQL queries
        api_response = api_instance.app_connector_mssql_mssql_connector_action_generate_sql_queries()
        print("The response of ConnectorsMssqlApi->app_connector_mssql_mssql_connector_action_generate_sql_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMssqlApi->app_connector_mssql_mssql_connector_action_generate_sql_queries: %s\n" % e)
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
**200** | Get generated SQL queries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_mssql_mssql_connector_action_list_columns**
> List[AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner] app_connector_mssql_mssql_connector_action_list_columns(app_connector_alloy_db_alloy_db_connector_action_list_columns_request=app_connector_alloy_db_alloy_db_connector_action_list_columns_request)

List of table columns

### Example


```python
import openapi_client
from openapi_client.models.app_connector_alloy_db_alloy_db_connector_action_list_columns_request import AppConnectorAlloyDbAlloyDbConnectorActionListColumnsRequest
from openapi_client.models.app_connector_alloy_db_alloy_db_connector_action_list_tables200_response_inner import AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner
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
    api_instance = openapi_client.ConnectorsMssqlApi(api_client)
    app_connector_alloy_db_alloy_db_connector_action_list_columns_request = openapi_client.AppConnectorAlloyDbAlloyDbConnectorActionListColumnsRequest() # AppConnectorAlloyDbAlloyDbConnectorActionListColumnsRequest |  (optional)

    try:
        # List of table columns
        api_response = api_instance.app_connector_mssql_mssql_connector_action_list_columns(app_connector_alloy_db_alloy_db_connector_action_list_columns_request=app_connector_alloy_db_alloy_db_connector_action_list_columns_request)
        print("The response of ConnectorsMssqlApi->app_connector_mssql_mssql_connector_action_list_columns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMssqlApi->app_connector_mssql_mssql_connector_action_list_columns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_connector_alloy_db_alloy_db_connector_action_list_columns_request** | [**AppConnectorAlloyDbAlloyDbConnectorActionListColumnsRequest**](AppConnectorAlloyDbAlloyDbConnectorActionListColumnsRequest.md)|  | [optional] 

### Return type

[**List[AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner]**](AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of table columns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_mssql_mssql_connector_action_list_tables**
> List[AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner] app_connector_mssql_mssql_connector_action_list_tables(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List of database tables

### Example


```python
import openapi_client
from openapi_client.models.amazon_ads_controller_action_profile_request_value import AmazonAdsControllerActionProfileRequestValue
from openapi_client.models.app_connector_alloy_db_alloy_db_connector_action_list_tables200_response_inner import AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner
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
    api_instance = openapi_client.ConnectorsMssqlApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List of database tables
        api_response = api_instance.app_connector_mssql_mssql_connector_action_list_tables(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsMssqlApi->app_connector_mssql_mssql_connector_action_list_tables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMssqlApi->app_connector_mssql_mssql_connector_action_list_tables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_ads_controller_action_profile_request_value** | [**AmazonAdsControllerActionProfileRequestValue**](AmazonAdsControllerActionProfileRequestValue.md)|  | [optional] 

### Return type

[**List[AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner]**](AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of database tables |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_mssql_mssql_connector_action_sql**
> List[LabelValueResponseInner] app_connector_mssql_mssql_connector_action_sql(app_connector_alloy_db_alloy_db_connector_action_sql_request=app_connector_alloy_db_alloy_db_connector_action_sql_request)

Get generated SQL

### Example


```python
import openapi_client
from openapi_client.models.app_connector_alloy_db_alloy_db_connector_action_sql_request import AppConnectorAlloyDbAlloyDbConnectorActionSQLRequest
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
    api_instance = openapi_client.ConnectorsMssqlApi(api_client)
    app_connector_alloy_db_alloy_db_connector_action_sql_request = openapi_client.AppConnectorAlloyDbAlloyDbConnectorActionSQLRequest() # AppConnectorAlloyDbAlloyDbConnectorActionSQLRequest |  (optional)

    try:
        # Get generated SQL
        api_response = api_instance.app_connector_mssql_mssql_connector_action_sql(app_connector_alloy_db_alloy_db_connector_action_sql_request=app_connector_alloy_db_alloy_db_connector_action_sql_request)
        print("The response of ConnectorsMssqlApi->app_connector_mssql_mssql_connector_action_sql:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMssqlApi->app_connector_mssql_mssql_connector_action_sql: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_connector_alloy_db_alloy_db_connector_action_sql_request** | [**AppConnectorAlloyDbAlloyDbConnectorActionSQLRequest**](AppConnectorAlloyDbAlloyDbConnectorActionSQLRequest.md)|  | [optional] 

### Return type

[**List[LabelValueResponseInner]**](LabelValueResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get generated SQL |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_mssql_mssql_connector_create_source**
> Source app_connector_mssql_mssql_connector_create_source(mssql_dto=mssql_dto)

Create Mssql source

### Example


```python
import openapi_client
from openapi_client.models.mssql_dto import MssqlDto
from openapi_client.models.source import Source
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
    api_instance = openapi_client.ConnectorsMssqlApi(api_client)
    mssql_dto = openapi_client.MssqlDto() # MssqlDto |  (optional)

    try:
        # Create Mssql source
        api_response = api_instance.app_connector_mssql_mssql_connector_create_source(mssql_dto=mssql_dto)
        print("The response of ConnectorsMssqlApi->app_connector_mssql_mssql_connector_create_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMssqlApi->app_connector_mssql_mssql_connector_create_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mssql_dto** | [**MssqlDto**](MssqlDto.md)|  | [optional] 

### Return type

[**Source**](Source.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_mssql_mssql_connector_preview**
> SuccessResponse app_connector_mssql_mssql_connector_preview(mssql_dto=mssql_dto)

Data preview

### Example


```python
import openapi_client
from openapi_client.models.mssql_dto import MssqlDto
from openapi_client.models.success_response import SuccessResponse
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
    api_instance = openapi_client.ConnectorsMssqlApi(api_client)
    mssql_dto = openapi_client.MssqlDto() # MssqlDto |  (optional)

    try:
        # Data preview
        api_response = api_instance.app_connector_mssql_mssql_connector_preview(mssql_dto=mssql_dto)
        print("The response of ConnectorsMssqlApi->app_connector_mssql_mssql_connector_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMssqlApi->app_connector_mssql_mssql_connector_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mssql_dto** | [**MssqlDto**](MssqlDto.md)|  | [optional] 

### Return type

[**SuccessResponse**](SuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Data preview |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

