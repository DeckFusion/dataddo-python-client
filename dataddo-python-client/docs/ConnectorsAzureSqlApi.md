# openapi_client.ConnectorsAzureSqlApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_azure_sql_azure_sql_connector_action_generate_sql_queries**](ConnectorsAzureSqlApi.md#app_connector_azure_sql_azure_sql_connector_action_generate_sql_queries) | **GET** /connectors/azureSql/actions/generateSQLQueries | Get generated SQL queries
[**app_connector_azure_sql_azure_sql_connector_action_list_columns**](ConnectorsAzureSqlApi.md#app_connector_azure_sql_azure_sql_connector_action_list_columns) | **POST** /connectors/azureSql/actions/listColumns | List of table columns
[**app_connector_azure_sql_azure_sql_connector_action_list_tables**](ConnectorsAzureSqlApi.md#app_connector_azure_sql_azure_sql_connector_action_list_tables) | **POST** /connectors/azureSql/actions/listTables | List of database tables
[**app_connector_azure_sql_azure_sql_connector_action_sql**](ConnectorsAzureSqlApi.md#app_connector_azure_sql_azure_sql_connector_action_sql) | **POST** /connectors/azureSql/actions/sql | Get generated SQL


# **app_connector_azure_sql_azure_sql_connector_action_generate_sql_queries**
> List[LabelValueResponseInner] app_connector_azure_sql_azure_sql_connector_action_generate_sql_queries()

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
    api_instance = openapi_client.ConnectorsAzureSqlApi(api_client)

    try:
        # Get generated SQL queries
        api_response = api_instance.app_connector_azure_sql_azure_sql_connector_action_generate_sql_queries()
        print("The response of ConnectorsAzureSqlApi->app_connector_azure_sql_azure_sql_connector_action_generate_sql_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAzureSqlApi->app_connector_azure_sql_azure_sql_connector_action_generate_sql_queries: %s\n" % e)
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

# **app_connector_azure_sql_azure_sql_connector_action_list_columns**
> List[AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner] app_connector_azure_sql_azure_sql_connector_action_list_columns(app_connector_alloy_db_alloy_db_connector_action_list_columns_request=app_connector_alloy_db_alloy_db_connector_action_list_columns_request)

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
    api_instance = openapi_client.ConnectorsAzureSqlApi(api_client)
    app_connector_alloy_db_alloy_db_connector_action_list_columns_request = openapi_client.AppConnectorAlloyDbAlloyDbConnectorActionListColumnsRequest() # AppConnectorAlloyDbAlloyDbConnectorActionListColumnsRequest |  (optional)

    try:
        # List of table columns
        api_response = api_instance.app_connector_azure_sql_azure_sql_connector_action_list_columns(app_connector_alloy_db_alloy_db_connector_action_list_columns_request=app_connector_alloy_db_alloy_db_connector_action_list_columns_request)
        print("The response of ConnectorsAzureSqlApi->app_connector_azure_sql_azure_sql_connector_action_list_columns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAzureSqlApi->app_connector_azure_sql_azure_sql_connector_action_list_columns: %s\n" % e)
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

# **app_connector_azure_sql_azure_sql_connector_action_list_tables**
> List[AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner] app_connector_azure_sql_azure_sql_connector_action_list_tables(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

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
    api_instance = openapi_client.ConnectorsAzureSqlApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List of database tables
        api_response = api_instance.app_connector_azure_sql_azure_sql_connector_action_list_tables(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsAzureSqlApi->app_connector_azure_sql_azure_sql_connector_action_list_tables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAzureSqlApi->app_connector_azure_sql_azure_sql_connector_action_list_tables: %s\n" % e)
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

# **app_connector_azure_sql_azure_sql_connector_action_sql**
> List[LabelValueResponseInner] app_connector_azure_sql_azure_sql_connector_action_sql(app_connector_alloy_db_alloy_db_connector_action_sql_request=app_connector_alloy_db_alloy_db_connector_action_sql_request)

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
    api_instance = openapi_client.ConnectorsAzureSqlApi(api_client)
    app_connector_alloy_db_alloy_db_connector_action_sql_request = openapi_client.AppConnectorAlloyDbAlloyDbConnectorActionSQLRequest() # AppConnectorAlloyDbAlloyDbConnectorActionSQLRequest |  (optional)

    try:
        # Get generated SQL
        api_response = api_instance.app_connector_azure_sql_azure_sql_connector_action_sql(app_connector_alloy_db_alloy_db_connector_action_sql_request=app_connector_alloy_db_alloy_db_connector_action_sql_request)
        print("The response of ConnectorsAzureSqlApi->app_connector_azure_sql_azure_sql_connector_action_sql:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAzureSqlApi->app_connector_azure_sql_azure_sql_connector_action_sql: %s\n" % e)
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

