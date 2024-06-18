# openapi_client.ConnectorsGoogleBigQueryApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_google_big_query_google_big_query_connector_action_authorization**](ConnectorsGoogleBigQueryApi.md#app_connector_google_big_query_google_big_query_connector_action_authorization) | **GET** /connectors/google_big_query/actions/authorization | List of authorization objects
[**app_connector_google_big_query_google_big_query_connector_action_dataset**](ConnectorsGoogleBigQueryApi.md#app_connector_google_big_query_google_big_query_connector_action_dataset) | **POST** /connectors/google_big_query/actions/dataset | List of database datasets
[**app_connector_google_big_query_google_big_query_connector_action_list_columns**](ConnectorsGoogleBigQueryApi.md#app_connector_google_big_query_google_big_query_connector_action_list_columns) | **POST** /connectors/google_big_query/actions/listColumns | List of table columns
[**app_connector_google_big_query_google_big_query_connector_action_list_tables**](ConnectorsGoogleBigQueryApi.md#app_connector_google_big_query_google_big_query_connector_action_list_tables) | **POST** /connectors/google_big_query/actions/listTables | List of database tables
[**app_connector_google_big_query_google_big_query_connector_action_project**](ConnectorsGoogleBigQueryApi.md#app_connector_google_big_query_google_big_query_connector_action_project) | **POST** /connectors/google_big_query/actions/project | List of database project
[**app_connector_google_big_query_google_big_query_connector_action_session_read**](ConnectorsGoogleBigQueryApi.md#app_connector_google_big_query_google_big_query_connector_action_session_read) | **POST** /connectors/google_big_query/actions/sessionRead | List of sessionRead options
[**app_connector_google_big_query_google_big_query_connector_action_sql**](ConnectorsGoogleBigQueryApi.md#app_connector_google_big_query_google_big_query_connector_action_sql) | **POST** /connectors/google_big_query/actions/sql | Get generated SQL
[**app_connector_google_big_query_google_big_query_connector_create_source**](ConnectorsGoogleBigQueryApi.md#app_connector_google_big_query_google_big_query_connector_create_source) | **POST** /connectors/google_big_query/create-source | Create Google Big Query source
[**app_connector_google_big_query_google_big_query_connector_preview**](ConnectorsGoogleBigQueryApi.md#app_connector_google_big_query_google_big_query_connector_preview) | **POST** /connectors/google_big_query/preview | Data preview


# **app_connector_google_big_query_google_big_query_connector_action_authorization**
> List[ActionAuthorizationResponseInner] app_connector_google_big_query_google_big_query_connector_action_authorization()

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
    api_instance = openapi_client.ConnectorsGoogleBigQueryApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_connector_google_big_query_google_big_query_connector_action_authorization()
        print("The response of ConnectorsGoogleBigQueryApi->app_connector_google_big_query_google_big_query_connector_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleBigQueryApi->app_connector_google_big_query_google_big_query_connector_action_authorization: %s\n" % e)
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

# **app_connector_google_big_query_google_big_query_connector_action_dataset**
> List[GoogleAnalyticsControllerActionAccount200ResponseInner] app_connector_google_big_query_google_big_query_connector_action_dataset(app_connector_google_big_query_google_big_query_connector_action_dataset_request=app_connector_google_big_query_google_big_query_connector_action_dataset_request)

List of database datasets

### Example


```python
import openapi_client
from openapi_client.models.app_connector_google_big_query_google_big_query_connector_action_dataset_request import AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionDatasetRequest
from openapi_client.models.google_analytics_controller_action_account200_response_inner import GoogleAnalyticsControllerActionAccount200ResponseInner
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
    api_instance = openapi_client.ConnectorsGoogleBigQueryApi(api_client)
    app_connector_google_big_query_google_big_query_connector_action_dataset_request = openapi_client.AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionDatasetRequest() # AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionDatasetRequest |  (optional)

    try:
        # List of database datasets
        api_response = api_instance.app_connector_google_big_query_google_big_query_connector_action_dataset(app_connector_google_big_query_google_big_query_connector_action_dataset_request=app_connector_google_big_query_google_big_query_connector_action_dataset_request)
        print("The response of ConnectorsGoogleBigQueryApi->app_connector_google_big_query_google_big_query_connector_action_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleBigQueryApi->app_connector_google_big_query_google_big_query_connector_action_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_connector_google_big_query_google_big_query_connector_action_dataset_request** | [**AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionDatasetRequest**](AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionDatasetRequest.md)|  | [optional] 

### Return type

[**List[GoogleAnalyticsControllerActionAccount200ResponseInner]**](GoogleAnalyticsControllerActionAccount200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of database datasets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_google_big_query_google_big_query_connector_action_list_columns**
> List[AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner] app_connector_google_big_query_google_big_query_connector_action_list_columns(app_connector_google_big_query_google_big_query_connector_action_list_columns_request=app_connector_google_big_query_google_big_query_connector_action_list_columns_request)

List of table columns

### Example


```python
import openapi_client
from openapi_client.models.app_connector_alloy_db_alloy_db_connector_action_list_tables200_response_inner import AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner
from openapi_client.models.app_connector_google_big_query_google_big_query_connector_action_list_columns_request import AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionListColumnsRequest
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
    api_instance = openapi_client.ConnectorsGoogleBigQueryApi(api_client)
    app_connector_google_big_query_google_big_query_connector_action_list_columns_request = openapi_client.AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionListColumnsRequest() # AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionListColumnsRequest |  (optional)

    try:
        # List of table columns
        api_response = api_instance.app_connector_google_big_query_google_big_query_connector_action_list_columns(app_connector_google_big_query_google_big_query_connector_action_list_columns_request=app_connector_google_big_query_google_big_query_connector_action_list_columns_request)
        print("The response of ConnectorsGoogleBigQueryApi->app_connector_google_big_query_google_big_query_connector_action_list_columns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleBigQueryApi->app_connector_google_big_query_google_big_query_connector_action_list_columns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_connector_google_big_query_google_big_query_connector_action_list_columns_request** | [**AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionListColumnsRequest**](AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionListColumnsRequest.md)|  | [optional] 

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

# **app_connector_google_big_query_google_big_query_connector_action_list_tables**
> List[AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner] app_connector_google_big_query_google_big_query_connector_action_list_tables(app_connector_google_big_query_google_big_query_connector_action_list_tables_request=app_connector_google_big_query_google_big_query_connector_action_list_tables_request)

List of database tables

### Example


```python
import openapi_client
from openapi_client.models.app_connector_alloy_db_alloy_db_connector_action_list_tables200_response_inner import AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner
from openapi_client.models.app_connector_google_big_query_google_big_query_connector_action_list_tables_request import AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionListTablesRequest
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
    api_instance = openapi_client.ConnectorsGoogleBigQueryApi(api_client)
    app_connector_google_big_query_google_big_query_connector_action_list_tables_request = openapi_client.AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionListTablesRequest() # AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionListTablesRequest |  (optional)

    try:
        # List of database tables
        api_response = api_instance.app_connector_google_big_query_google_big_query_connector_action_list_tables(app_connector_google_big_query_google_big_query_connector_action_list_tables_request=app_connector_google_big_query_google_big_query_connector_action_list_tables_request)
        print("The response of ConnectorsGoogleBigQueryApi->app_connector_google_big_query_google_big_query_connector_action_list_tables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleBigQueryApi->app_connector_google_big_query_google_big_query_connector_action_list_tables: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_connector_google_big_query_google_big_query_connector_action_list_tables_request** | [**AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionListTablesRequest**](AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionListTablesRequest.md)|  | [optional] 

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

# **app_connector_google_big_query_google_big_query_connector_action_project**
> List[GoogleAnalyticsControllerActionAccount200ResponseInner] app_connector_google_big_query_google_big_query_connector_action_project(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)

List of database project

### Example


```python
import openapi_client
from openapi_client.models.amazon_ads_controller_action_profile_request_value import AmazonAdsControllerActionProfileRequestValue
from openapi_client.models.google_analytics_controller_action_account200_response_inner import GoogleAnalyticsControllerActionAccount200ResponseInner
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
    api_instance = openapi_client.ConnectorsGoogleBigQueryApi(api_client)
    amazon_ads_controller_action_profile_request_value = openapi_client.AmazonAdsControllerActionProfileRequestValue() # AmazonAdsControllerActionProfileRequestValue |  (optional)

    try:
        # List of database project
        api_response = api_instance.app_connector_google_big_query_google_big_query_connector_action_project(amazon_ads_controller_action_profile_request_value=amazon_ads_controller_action_profile_request_value)
        print("The response of ConnectorsGoogleBigQueryApi->app_connector_google_big_query_google_big_query_connector_action_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleBigQueryApi->app_connector_google_big_query_google_big_query_connector_action_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_ads_controller_action_profile_request_value** | [**AmazonAdsControllerActionProfileRequestValue**](AmazonAdsControllerActionProfileRequestValue.md)|  | [optional] 

### Return type

[**List[GoogleAnalyticsControllerActionAccount200ResponseInner]**](GoogleAnalyticsControllerActionAccount200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of database projects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_google_big_query_google_big_query_connector_action_session_read**
> List[AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner] app_connector_google_big_query_google_big_query_connector_action_session_read(app_connector_google_big_query_google_big_query_connector_action_session_read_request=app_connector_google_big_query_google_big_query_connector_action_session_read_request)

List of sessionRead options

### Example


```python
import openapi_client
from openapi_client.models.app_connector_alloy_db_alloy_db_connector_action_list_tables200_response_inner import AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner
from openapi_client.models.app_connector_google_big_query_google_big_query_connector_action_session_read_request import AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionSessionReadRequest
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
    api_instance = openapi_client.ConnectorsGoogleBigQueryApi(api_client)
    app_connector_google_big_query_google_big_query_connector_action_session_read_request = openapi_client.AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionSessionReadRequest() # AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionSessionReadRequest |  (optional)

    try:
        # List of sessionRead options
        api_response = api_instance.app_connector_google_big_query_google_big_query_connector_action_session_read(app_connector_google_big_query_google_big_query_connector_action_session_read_request=app_connector_google_big_query_google_big_query_connector_action_session_read_request)
        print("The response of ConnectorsGoogleBigQueryApi->app_connector_google_big_query_google_big_query_connector_action_session_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleBigQueryApi->app_connector_google_big_query_google_big_query_connector_action_session_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_connector_google_big_query_google_big_query_connector_action_session_read_request** | [**AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionSessionReadRequest**](AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionSessionReadRequest.md)|  | [optional] 

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
**200** | List of sessionRead options |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_google_big_query_google_big_query_connector_action_sql**
> List[LabelValueResponseInner] app_connector_google_big_query_google_big_query_connector_action_sql(app_connector_google_big_query_google_big_query_connector_action_sql_request=app_connector_google_big_query_google_big_query_connector_action_sql_request)

Get generated SQL

### Example


```python
import openapi_client
from openapi_client.models.app_connector_google_big_query_google_big_query_connector_action_sql_request import AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionSQLRequest
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
    api_instance = openapi_client.ConnectorsGoogleBigQueryApi(api_client)
    app_connector_google_big_query_google_big_query_connector_action_sql_request = openapi_client.AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionSQLRequest() # AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionSQLRequest |  (optional)

    try:
        # Get generated SQL
        api_response = api_instance.app_connector_google_big_query_google_big_query_connector_action_sql(app_connector_google_big_query_google_big_query_connector_action_sql_request=app_connector_google_big_query_google_big_query_connector_action_sql_request)
        print("The response of ConnectorsGoogleBigQueryApi->app_connector_google_big_query_google_big_query_connector_action_sql:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleBigQueryApi->app_connector_google_big_query_google_big_query_connector_action_sql: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_connector_google_big_query_google_big_query_connector_action_sql_request** | [**AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionSQLRequest**](AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionSQLRequest.md)|  | [optional] 

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

# **app_connector_google_big_query_google_big_query_connector_create_source**
> Source app_connector_google_big_query_google_big_query_connector_create_source(google_big_query_dto=google_big_query_dto)

Create Google Big Query source

### Example


```python
import openapi_client
from openapi_client.models.google_big_query_dto import GoogleBigQueryDto
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
    api_instance = openapi_client.ConnectorsGoogleBigQueryApi(api_client)
    google_big_query_dto = openapi_client.GoogleBigQueryDto() # GoogleBigQueryDto |  (optional)

    try:
        # Create Google Big Query source
        api_response = api_instance.app_connector_google_big_query_google_big_query_connector_create_source(google_big_query_dto=google_big_query_dto)
        print("The response of ConnectorsGoogleBigQueryApi->app_connector_google_big_query_google_big_query_connector_create_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleBigQueryApi->app_connector_google_big_query_google_big_query_connector_create_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_big_query_dto** | [**GoogleBigQueryDto**](GoogleBigQueryDto.md)|  | [optional] 

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

# **app_connector_google_big_query_google_big_query_connector_preview**
> SuccessResponse app_connector_google_big_query_google_big_query_connector_preview(google_big_query_dto=google_big_query_dto)

Data preview

### Example


```python
import openapi_client
from openapi_client.models.google_big_query_dto import GoogleBigQueryDto
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
    api_instance = openapi_client.ConnectorsGoogleBigQueryApi(api_client)
    google_big_query_dto = openapi_client.GoogleBigQueryDto() # GoogleBigQueryDto |  (optional)

    try:
        # Data preview
        api_response = api_instance.app_connector_google_big_query_google_big_query_connector_preview(google_big_query_dto=google_big_query_dto)
        print("The response of ConnectorsGoogleBigQueryApi->app_connector_google_big_query_google_big_query_connector_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsGoogleBigQueryApi->app_connector_google_big_query_google_big_query_connector_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_big_query_dto** | [**GoogleBigQueryDto**](GoogleBigQueryDto.md)|  | [optional] 

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

