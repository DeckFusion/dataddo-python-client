# openapi_client.ConnectorsMysqlApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_mysql_mysql_connector_action_authorization**](ConnectorsMysqlApi.md#app_connector_mysql_mysql_connector_action_authorization) | **GET** /connectors/mysql/actions/authorization | List of authorization objects
[**app_connector_mysql_mysql_connector_action_generate_sql_queries**](ConnectorsMysqlApi.md#app_connector_mysql_mysql_connector_action_generate_sql_queries) | **GET** /connectors/mysql/actions/generateSQLQueries | Get generated SQL queries
[**app_connector_mysql_mysql_connector_action_list_columns**](ConnectorsMysqlApi.md#app_connector_mysql_mysql_connector_action_list_columns) | **POST** /connectors/mysql/actions/listColumns | List of table columns
[**app_connector_mysql_mysql_connector_action_list_tables**](ConnectorsMysqlApi.md#app_connector_mysql_mysql_connector_action_list_tables) | **POST** /connectors/mysql/actions/listTables | List of database tables
[**app_connector_mysql_mysql_connector_action_sql**](ConnectorsMysqlApi.md#app_connector_mysql_mysql_connector_action_sql) | **POST** /connectors/mysql/actions/sql | Get generated SQL
[**app_connector_mysql_mysql_connector_create_source**](ConnectorsMysqlApi.md#app_connector_mysql_mysql_connector_create_source) | **POST** /connectors/mysql/create-source | Create Mysql source
[**app_connector_mysql_mysql_connector_preview**](ConnectorsMysqlApi.md#app_connector_mysql_mysql_connector_preview) | **POST** /connectors/mysql/preview | Data preview


# **app_connector_mysql_mysql_connector_action_authorization**
> List[ActionAuthorizationResponseInner] app_connector_mysql_mysql_connector_action_authorization()

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
    api_instance = openapi_client.ConnectorsMysqlApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_connector_mysql_mysql_connector_action_authorization()
        print("The response of ConnectorsMysqlApi->app_connector_mysql_mysql_connector_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMysqlApi->app_connector_mysql_mysql_connector_action_authorization: %s\n" % e)
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

# **app_connector_mysql_mysql_connector_action_generate_sql_queries**
> List[LabelValueResponseInner] app_connector_mysql_mysql_connector_action_generate_sql_queries()

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
    api_instance = openapi_client.ConnectorsMysqlApi(api_client)

    try:
        # Get generated SQL queries
        api_response = api_instance.app_connector_mysql_mysql_connector_action_generate_sql_queries()
        print("The response of ConnectorsMysqlApi->app_connector_mysql_mysql_connector_action_generate_sql_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMysqlApi->app_connector_mysql_mysql_connector_action_generate_sql_queries: %s\n" % e)
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

# **app_connector_mysql_mysql_connector_action_list_columns**
> List[AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner] app_connector_mysql_mysql_connector_action_list_columns(app_connector_alloy_db_alloy_db_connector_action_list_columns_request=app_connector_alloy_db_alloy_db_connector_action_list_columns_request)

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
    api_instance = openapi_client.ConnectorsMysqlApi(api_client)
    app_connector_alloy_db_alloy_db_connector_action_list_columns_request = openapi_client.AppConnectorAlloyDbAlloyDbConnectorActionListColumnsRequest() # AppConnectorAlloyDbAlloyDbConnectorActionListColumnsRequest |  (optional)

    try:
        # List of table columns
        api_response = api_instance.app_connector_mysql_mysql_connector_action_list_columns(app_connector_alloy_db_alloy_db_connector_action_list_columns_request=app_connector_alloy_db_alloy_db_connector_action_list_columns_request)
        print("The response of ConnectorsMysqlApi->app_connector_mysql_mysql_connector_action_list_columns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMysqlApi->app_connector_mysql_mysql_connector_action_list_columns: %s\n" % e)
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

# **app_connector_mysql_mysql_connector_action_list_tables**
> List[AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner] app_connector_mysql_mysql_connector_action_list_tables(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

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
    api_instance = openapi_client.ConnectorsMysqlApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List of database tables
        api_response = api_instance.app_connector_mysql_mysql_connector_action_list_tables(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsMysqlApi->app_connector_mysql_mysql_connector_action_list_tables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMysqlApi->app_connector_mysql_mysql_connector_action_list_tables: %s\n" % e)
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

# **app_connector_mysql_mysql_connector_action_sql**
> List[LabelValueResponseInner] app_connector_mysql_mysql_connector_action_sql(app_connector_alloy_db_alloy_db_connector_action_sql_request=app_connector_alloy_db_alloy_db_connector_action_sql_request)

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
    api_instance = openapi_client.ConnectorsMysqlApi(api_client)
    app_connector_alloy_db_alloy_db_connector_action_sql_request = openapi_client.AppConnectorAlloyDbAlloyDbConnectorActionSQLRequest() # AppConnectorAlloyDbAlloyDbConnectorActionSQLRequest |  (optional)

    try:
        # Get generated SQL
        api_response = api_instance.app_connector_mysql_mysql_connector_action_sql(app_connector_alloy_db_alloy_db_connector_action_sql_request=app_connector_alloy_db_alloy_db_connector_action_sql_request)
        print("The response of ConnectorsMysqlApi->app_connector_mysql_mysql_connector_action_sql:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMysqlApi->app_connector_mysql_mysql_connector_action_sql: %s\n" % e)
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

# **app_connector_mysql_mysql_connector_create_source**
> Source app_connector_mysql_mysql_connector_create_source(mysql_dto=mysql_dto)

Create Mysql source

### Example


```python
import openapi_client
from openapi_client.models.mysql_dto import MysqlDto
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
    api_instance = openapi_client.ConnectorsMysqlApi(api_client)
    mysql_dto = openapi_client.MysqlDto() # MysqlDto |  (optional)

    try:
        # Create Mysql source
        api_response = api_instance.app_connector_mysql_mysql_connector_create_source(mysql_dto=mysql_dto)
        print("The response of ConnectorsMysqlApi->app_connector_mysql_mysql_connector_create_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMysqlApi->app_connector_mysql_mysql_connector_create_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mysql_dto** | [**MysqlDto**](MysqlDto.md)|  | [optional] 

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

# **app_connector_mysql_mysql_connector_preview**
> SuccessResponse app_connector_mysql_mysql_connector_preview(mysql_dto=mysql_dto)

Data preview

### Example


```python
import openapi_client
from openapi_client.models.mysql_dto import MysqlDto
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
    api_instance = openapi_client.ConnectorsMysqlApi(api_client)
    mysql_dto = openapi_client.MysqlDto() # MysqlDto |  (optional)

    try:
        # Data preview
        api_response = api_instance.app_connector_mysql_mysql_connector_preview(mysql_dto=mysql_dto)
        print("The response of ConnectorsMysqlApi->app_connector_mysql_mysql_connector_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsMysqlApi->app_connector_mysql_mysql_connector_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mysql_dto** | [**MysqlDto**](MysqlDto.md)|  | [optional] 

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

