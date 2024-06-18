# openapi_client.ConnectorsPgsqlWalApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_connector_pgsql_wal_pgsql_wal_connector_action_authorization**](ConnectorsPgsqlWalApi.md#app_connector_pgsql_wal_pgsql_wal_connector_action_authorization) | **GET** /connectors/pgsql_wal/actions/authorization | List of authorization objects
[**app_connector_pgsql_wal_pgsql_wal_connector_action_list_columns**](ConnectorsPgsqlWalApi.md#app_connector_pgsql_wal_pgsql_wal_connector_action_list_columns) | **GET** /connectors/pgsql_wal/actions/list-columns | List of table columns
[**app_connector_pgsql_wal_pgsql_wal_connector_action_list_tables**](ConnectorsPgsqlWalApi.md#app_connector_pgsql_wal_pgsql_wal_connector_action_list_tables) | **GET** /connectors/pgsql_wal/actions/list-tables | List of database tables
[**app_connector_pgsql_wal_pgsql_wal_connector_create_source**](ConnectorsPgsqlWalApi.md#app_connector_pgsql_wal_pgsql_wal_connector_create_source) | **POST** /connectors/pgsql_wal/create-source | Create Pgsql Binlog source
[**app_connector_pgsql_wal_pgsql_wal_connector_preview**](ConnectorsPgsqlWalApi.md#app_connector_pgsql_wal_pgsql_wal_connector_preview) | **POST** /connectors/pgsql_wal/preview | Data preview


# **app_connector_pgsql_wal_pgsql_wal_connector_action_authorization**
> List[ActionAuthorizationResponseInner] app_connector_pgsql_wal_pgsql_wal_connector_action_authorization()

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
    api_instance = openapi_client.ConnectorsPgsqlWalApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.app_connector_pgsql_wal_pgsql_wal_connector_action_authorization()
        print("The response of ConnectorsPgsqlWalApi->app_connector_pgsql_wal_pgsql_wal_connector_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsPgsqlWalApi->app_connector_pgsql_wal_pgsql_wal_connector_action_authorization: %s\n" % e)
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

# **app_connector_pgsql_wal_pgsql_wal_connector_action_list_columns**
> List[AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner] app_connector_pgsql_wal_pgsql_wal_connector_action_list_columns()

List of table columns

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ConnectorsPgsqlWalApi(api_client)

    try:
        # List of table columns
        api_response = api_instance.app_connector_pgsql_wal_pgsql_wal_connector_action_list_columns()
        print("The response of ConnectorsPgsqlWalApi->app_connector_pgsql_wal_pgsql_wal_connector_action_list_columns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsPgsqlWalApi->app_connector_pgsql_wal_pgsql_wal_connector_action_list_columns: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner]**](AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of table columns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_pgsql_wal_pgsql_wal_connector_action_list_tables**
> List[AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner] app_connector_pgsql_wal_pgsql_wal_connector_action_list_tables()

List of database tables

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ConnectorsPgsqlWalApi(api_client)

    try:
        # List of database tables
        api_response = api_instance.app_connector_pgsql_wal_pgsql_wal_connector_action_list_tables()
        print("The response of ConnectorsPgsqlWalApi->app_connector_pgsql_wal_pgsql_wal_connector_action_list_tables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsPgsqlWalApi->app_connector_pgsql_wal_pgsql_wal_connector_action_list_tables: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner]**](AppConnectorAlloyDbAlloyDbConnectorActionListTables200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of database tables |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_connector_pgsql_wal_pgsql_wal_connector_create_source**
> Source app_connector_pgsql_wal_pgsql_wal_connector_create_source(pgsql_wal_dto=pgsql_wal_dto)

Create Pgsql Binlog source

### Example


```python
import openapi_client
from openapi_client.models.pgsql_wal_dto import PgsqlWalDto
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
    api_instance = openapi_client.ConnectorsPgsqlWalApi(api_client)
    pgsql_wal_dto = openapi_client.PgsqlWalDto() # PgsqlWalDto |  (optional)

    try:
        # Create Pgsql Binlog source
        api_response = api_instance.app_connector_pgsql_wal_pgsql_wal_connector_create_source(pgsql_wal_dto=pgsql_wal_dto)
        print("The response of ConnectorsPgsqlWalApi->app_connector_pgsql_wal_pgsql_wal_connector_create_source:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsPgsqlWalApi->app_connector_pgsql_wal_pgsql_wal_connector_create_source: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pgsql_wal_dto** | [**PgsqlWalDto**](PgsqlWalDto.md)|  | [optional] 

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

# **app_connector_pgsql_wal_pgsql_wal_connector_preview**
> SuccessResponse app_connector_pgsql_wal_pgsql_wal_connector_preview(pgsql_wal_dto=pgsql_wal_dto)

Data preview

### Example


```python
import openapi_client
from openapi_client.models.pgsql_wal_dto import PgsqlWalDto
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
    api_instance = openapi_client.ConnectorsPgsqlWalApi(api_client)
    pgsql_wal_dto = openapi_client.PgsqlWalDto() # PgsqlWalDto |  (optional)

    try:
        # Data preview
        api_response = api_instance.app_connector_pgsql_wal_pgsql_wal_connector_preview(pgsql_wal_dto=pgsql_wal_dto)
        print("The response of ConnectorsPgsqlWalApi->app_connector_pgsql_wal_pgsql_wal_connector_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsPgsqlWalApi->app_connector_pgsql_wal_pgsql_wal_connector_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pgsql_wal_dto** | [**PgsqlWalDto**](PgsqlWalDto.md)|  | [optional] 

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

