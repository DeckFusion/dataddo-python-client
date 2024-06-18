# openapi_client.ConnectorsSnapchatApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**snapchat_controller_action_account**](ConnectorsSnapchatApi.md#snapchat_controller_action_account) | **POST** /connectors/snapchat/actions/account | List of all Snapchat Ad account IDs
[**snapchat_controller_action_authorization**](ConnectorsSnapchatApi.md#snapchat_controller_action_authorization) | **GET** /connectors/snapchat/actions/authorization | List of authorization objects
[**snapchat_controller_action_breakdown**](ConnectorsSnapchatApi.md#snapchat_controller_action_breakdown) | **GET** /connectors/snapchat/actions/breakdown | List of stats breakdowns
[**snapchat_controller_action_campaign**](ConnectorsSnapchatApi.md#snapchat_controller_action_campaign) | **POST** /connectors/snapchat/actions/campaign | List of all Snapchat campaign IDs
[**snapchat_controller_action_date_range**](ConnectorsSnapchatApi.md#snapchat_controller_action_date_range) | **GET** /connectors/snapchat/actions/dateRange | List of date ranges
[**snapchat_controller_action_labels**](ConnectorsSnapchatApi.md#snapchat_controller_action_labels) | **GET** /connectors/snapchat/actions/labels | List of all labels
[**snapchat_controller_action_load**](ConnectorsSnapchatApi.md#snapchat_controller_action_load) | **POST** /connectors/snapchat/create-source | Create Snapchat source
[**snapchat_controller_action_metric**](ConnectorsSnapchatApi.md#snapchat_controller_action_metric) | **GET** /connectors/snapchat/actions/metric | List of all metrics
[**snapchat_controller_action_organization**](ConnectorsSnapchatApi.md#snapchat_controller_action_organization) | **POST** /connectors/snapchat/actions/organization | List of Snapchat organization IDs
[**snapchat_controller_action_preview**](ConnectorsSnapchatApi.md#snapchat_controller_action_preview) | **POST** /connectors/snapchat/preview | Preview the data


# **snapchat_controller_action_account**
> List[LabelValueResponseInner] snapchat_controller_action_account(snapchat_controller_action_account_request=snapchat_controller_action_account_request)

List of all Snapchat Ad account IDs

List all AdAccount IDs

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.snapchat_controller_action_account_request import SnapchatControllerActionAccountRequest
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
    api_instance = openapi_client.ConnectorsSnapchatApi(api_client)
    snapchat_controller_action_account_request = openapi_client.SnapchatControllerActionAccountRequest() # SnapchatControllerActionAccountRequest |  (optional)

    try:
        # List of all Snapchat Ad account IDs
        api_response = api_instance.snapchat_controller_action_account(snapchat_controller_action_account_request=snapchat_controller_action_account_request)
        print("The response of ConnectorsSnapchatApi->snapchat_controller_action_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSnapchatApi->snapchat_controller_action_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapchat_controller_action_account_request** | [**SnapchatControllerActionAccountRequest**](SnapchatControllerActionAccountRequest.md)|  | [optional] 

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
**200** | List of all Snapchat Ad account IDs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapchat_controller_action_authorization**
> List[ActionAuthorizationResponseInner] snapchat_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsSnapchatApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.snapchat_controller_action_authorization()
        print("The response of ConnectorsSnapchatApi->snapchat_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSnapchatApi->snapchat_controller_action_authorization: %s\n" % e)
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

# **snapchat_controller_action_breakdown**
> List[LabelValueResponseInner] snapchat_controller_action_breakdown()

List of stats breakdowns

Method for listing stats breakdowns

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
    api_instance = openapi_client.ConnectorsSnapchatApi(api_client)

    try:
        # List of stats breakdowns
        api_response = api_instance.snapchat_controller_action_breakdown()
        print("The response of ConnectorsSnapchatApi->snapchat_controller_action_breakdown:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSnapchatApi->snapchat_controller_action_breakdown: %s\n" % e)
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
**200** | List of stats breakdowns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapchat_controller_action_campaign**
> List[LabelValueResponseInner] snapchat_controller_action_campaign(snapchat_controller_action_campaign_request=snapchat_controller_action_campaign_request)

List of all Snapchat campaign IDs

List all Campaign IDs

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.snapchat_controller_action_campaign_request import SnapchatControllerActionCampaignRequest
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
    api_instance = openapi_client.ConnectorsSnapchatApi(api_client)
    snapchat_controller_action_campaign_request = openapi_client.SnapchatControllerActionCampaignRequest() # SnapchatControllerActionCampaignRequest |  (optional)

    try:
        # List of all Snapchat campaign IDs
        api_response = api_instance.snapchat_controller_action_campaign(snapchat_controller_action_campaign_request=snapchat_controller_action_campaign_request)
        print("The response of ConnectorsSnapchatApi->snapchat_controller_action_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSnapchatApi->snapchat_controller_action_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapchat_controller_action_campaign_request** | [**SnapchatControllerActionCampaignRequest**](SnapchatControllerActionCampaignRequest.md)|  | [optional] 

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
**200** | List of all Snapchat Ad account IDs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapchat_controller_action_date_range**
> List[LabelValueResponseInner] snapchat_controller_action_date_range()

List of date ranges

Method for listing date range

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
    api_instance = openapi_client.ConnectorsSnapchatApi(api_client)

    try:
        # List of date ranges
        api_response = api_instance.snapchat_controller_action_date_range()
        print("The response of ConnectorsSnapchatApi->snapchat_controller_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSnapchatApi->snapchat_controller_action_date_range: %s\n" % e)
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
**200** | List of date range objects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapchat_controller_action_labels**
> List[LabelValueResponseInner] snapchat_controller_action_labels()

List of all labels

List all labels

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
    api_instance = openapi_client.ConnectorsSnapchatApi(api_client)

    try:
        # List of all labels
        api_response = api_instance.snapchat_controller_action_labels()
        print("The response of ConnectorsSnapchatApi->snapchat_controller_action_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSnapchatApi->snapchat_controller_action_labels: %s\n" % e)
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
**200** | List of all labels |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapchat_controller_action_load**
> Source snapchat_controller_action_load(snapchat_connector_form=snapchat_connector_form)

Create Snapchat source

### Example


```python
import openapi_client
from openapi_client.models.snapchat_connector_form import SnapchatConnectorForm
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
    api_instance = openapi_client.ConnectorsSnapchatApi(api_client)
    snapchat_connector_form = openapi_client.SnapchatConnectorForm() # SnapchatConnectorForm |  (optional)

    try:
        # Create Snapchat source
        api_response = api_instance.snapchat_controller_action_load(snapchat_connector_form=snapchat_connector_form)
        print("The response of ConnectorsSnapchatApi->snapchat_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSnapchatApi->snapchat_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapchat_connector_form** | [**SnapchatConnectorForm**](SnapchatConnectorForm.md)|  | [optional] 

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
**200** | Create source |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapchat_controller_action_metric**
> List[LabelValueResponseInner] snapchat_controller_action_metric()

List of all metrics

List all metrics

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
    api_instance = openapi_client.ConnectorsSnapchatApi(api_client)

    try:
        # List of all metrics
        api_response = api_instance.snapchat_controller_action_metric()
        print("The response of ConnectorsSnapchatApi->snapchat_controller_action_metric:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSnapchatApi->snapchat_controller_action_metric: %s\n" % e)
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
**200** | List of all metrics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapchat_controller_action_organization**
> List[LabelValueResponseInner] snapchat_controller_action_organization(snapchat_controller_action_organization_request=snapchat_controller_action_organization_request)

List of Snapchat organization IDs

### Example


```python
import openapi_client
from openapi_client.models.label_value_response_inner import LabelValueResponseInner
from openapi_client.models.snapchat_controller_action_organization_request import SnapchatControllerActionOrganizationRequest
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
    api_instance = openapi_client.ConnectorsSnapchatApi(api_client)
    snapchat_controller_action_organization_request = openapi_client.SnapchatControllerActionOrganizationRequest() # SnapchatControllerActionOrganizationRequest |  (optional)

    try:
        # List of Snapchat organization IDs
        api_response = api_instance.snapchat_controller_action_organization(snapchat_controller_action_organization_request=snapchat_controller_action_organization_request)
        print("The response of ConnectorsSnapchatApi->snapchat_controller_action_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSnapchatApi->snapchat_controller_action_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapchat_controller_action_organization_request** | [**SnapchatControllerActionOrganizationRequest**](SnapchatControllerActionOrganizationRequest.md)|  | [optional] 

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
**200** | List of Snapchat organization IDs |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapchat_controller_action_preview**
> SuccessResponse snapchat_controller_action_preview(snapchat_connector_form=snapchat_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.snapchat_connector_form import SnapchatConnectorForm
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
    api_instance = openapi_client.ConnectorsSnapchatApi(api_client)
    snapchat_connector_form = openapi_client.SnapchatConnectorForm() # SnapchatConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.snapchat_controller_action_preview(snapchat_connector_form=snapchat_connector_form)
        print("The response of ConnectorsSnapchatApi->snapchat_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsSnapchatApi->snapchat_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapchat_connector_form** | [**SnapchatConnectorForm**](SnapchatConnectorForm.md)|  | [optional] 

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

