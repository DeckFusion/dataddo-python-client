# openapi_client.ConnectorsAmazonAdsApi

All URIs are relative to *https://headless.dataddo.com/customer-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**amazon_ads_controller_action_ad_product**](ConnectorsAmazonAdsApi.md#amazon_ads_controller_action_ad_product) | **GET** /connectors/amazon_ads/actions/adProduct | List Amazon Ads report category/ad product
[**amazon_ads_controller_action_authorization**](ConnectorsAmazonAdsApi.md#amazon_ads_controller_action_authorization) | **GET** /connectors/amazon_ads/actions/authorization | List of authorization objects
[**amazon_ads_controller_action_column**](ConnectorsAmazonAdsApi.md#amazon_ads_controller_action_column) | **POST** /connectors/amazon_ads/actions/column | List Amazon Ads columns
[**amazon_ads_controller_action_date_range**](ConnectorsAmazonAdsApi.md#amazon_ads_controller_action_date_range) | **GET** /connectors/amazon_ads/actions/dateRange | Method for listing date range
[**amazon_ads_controller_action_group_by**](ConnectorsAmazonAdsApi.md#amazon_ads_controller_action_group_by) | **POST** /connectors/amazon_ads/actions/groupBy | List Amazon Ads grouping parameters
[**amazon_ads_controller_action_load**](ConnectorsAmazonAdsApi.md#amazon_ads_controller_action_load) | **POST** /connectors/amazon_ads/create-source | Create Amazon Ads source
[**amazon_ads_controller_action_preview**](ConnectorsAmazonAdsApi.md#amazon_ads_controller_action_preview) | **POST** /connectors/amazon_ads/preview | Preview the data
[**amazon_ads_controller_action_profile**](ConnectorsAmazonAdsApi.md#amazon_ads_controller_action_profile) | **POST** /connectors/amazon_ads/actions/profile | List of profile ids
[**amazon_ads_controller_action_report_type**](ConnectorsAmazonAdsApi.md#amazon_ads_controller_action_report_type) | **POST** /connectors/amazon_ads/actions/reportType | List Amazon Ads report types
[**amazon_ads_controller_action_time_unit**](ConnectorsAmazonAdsApi.md#amazon_ads_controller_action_time_unit) | **GET** /connectors/amazon_ads/actions/timeUnit | List Amazon Ads time units


# **amazon_ads_controller_action_ad_product**
> List[LabelValueResponseInner] amazon_ads_controller_action_ad_product()

List Amazon Ads report category/ad product

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
    api_instance = openapi_client.ConnectorsAmazonAdsApi(api_client)

    try:
        # List Amazon Ads report category/ad product
        api_response = api_instance.amazon_ads_controller_action_ad_product()
        print("The response of ConnectorsAmazonAdsApi->amazon_ads_controller_action_ad_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAmazonAdsApi->amazon_ads_controller_action_ad_product: %s\n" % e)
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
**200** | List of report categories (ad products) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amazon_ads_controller_action_authorization**
> List[ActionAuthorizationResponseInner] amazon_ads_controller_action_authorization()

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
    api_instance = openapi_client.ConnectorsAmazonAdsApi(api_client)

    try:
        # List of authorization objects
        api_response = api_instance.amazon_ads_controller_action_authorization()
        print("The response of ConnectorsAmazonAdsApi->amazon_ads_controller_action_authorization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAmazonAdsApi->amazon_ads_controller_action_authorization: %s\n" % e)
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

# **amazon_ads_controller_action_column**
> List[LabelValueResponseInner] amazon_ads_controller_action_column(request_body=request_body)

List Amazon Ads columns

### Example


```python
import openapi_client
from openapi_client.models.amazon_ads_controller_action_column_request_value import AmazonAdsControllerActionColumnRequestValue
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
    api_instance = openapi_client.ConnectorsAmazonAdsApi(api_client)
    request_body = {'key': openapi_client.AmazonAdsControllerActionColumnRequestValue()} # Dict[str, AmazonAdsControllerActionColumnRequestValue] |  (optional)

    try:
        # List Amazon Ads columns
        api_response = api_instance.amazon_ads_controller_action_column(request_body=request_body)
        print("The response of ConnectorsAmazonAdsApi->amazon_ads_controller_action_column:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAmazonAdsApi->amazon_ads_controller_action_column: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, AmazonAdsControllerActionColumnRequestValue]**](AmazonAdsControllerActionColumnRequestValue.md)|  | [optional] 

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
**200** | List of Amazon Ads columns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amazon_ads_controller_action_date_range**
> List[LabelValueResponseInner] amazon_ads_controller_action_date_range()

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
    api_instance = openapi_client.ConnectorsAmazonAdsApi(api_client)

    try:
        # Method for listing date range
        api_response = api_instance.amazon_ads_controller_action_date_range()
        print("The response of ConnectorsAmazonAdsApi->amazon_ads_controller_action_date_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAmazonAdsApi->amazon_ads_controller_action_date_range: %s\n" % e)
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
**200** | List of Amazon Ads date ranges |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amazon_ads_controller_action_group_by**
> List[LabelValueResponseInner] amazon_ads_controller_action_group_by(request_body=request_body)

List Amazon Ads grouping parameters

### Example


```python
import openapi_client
from openapi_client.models.amazon_ads_controller_action_group_by_request_value import AmazonAdsControllerActionGroupByRequestValue
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
    api_instance = openapi_client.ConnectorsAmazonAdsApi(api_client)
    request_body = {'key': openapi_client.AmazonAdsControllerActionGroupByRequestValue()} # Dict[str, AmazonAdsControllerActionGroupByRequestValue] |  (optional)

    try:
        # List Amazon Ads grouping parameters
        api_response = api_instance.amazon_ads_controller_action_group_by(request_body=request_body)
        print("The response of ConnectorsAmazonAdsApi->amazon_ads_controller_action_group_by:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAmazonAdsApi->amazon_ads_controller_action_group_by: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, AmazonAdsControllerActionGroupByRequestValue]**](AmazonAdsControllerActionGroupByRequestValue.md)|  | [optional] 

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
**200** | List of Amazon Ads grouping options |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amazon_ads_controller_action_load**
> Source amazon_ads_controller_action_load(amazon_ads_connector_form=amazon_ads_connector_form)

Create Amazon Ads source

### Example


```python
import openapi_client
from openapi_client.models.amazon_ads_connector_form import AmazonAdsConnectorForm
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
    api_instance = openapi_client.ConnectorsAmazonAdsApi(api_client)
    amazon_ads_connector_form = openapi_client.AmazonAdsConnectorForm() # AmazonAdsConnectorForm |  (optional)

    try:
        # Create Amazon Ads source
        api_response = api_instance.amazon_ads_controller_action_load(amazon_ads_connector_form=amazon_ads_connector_form)
        print("The response of ConnectorsAmazonAdsApi->amazon_ads_controller_action_load:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAmazonAdsApi->amazon_ads_controller_action_load: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_ads_connector_form** | [**AmazonAdsConnectorForm**](AmazonAdsConnectorForm.md)|  | [optional] 

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

# **amazon_ads_controller_action_preview**
> SuccessResponse amazon_ads_controller_action_preview(amazon_ads_connector_form=amazon_ads_connector_form)

Preview the data

### Example


```python
import openapi_client
from openapi_client.models.amazon_ads_connector_form import AmazonAdsConnectorForm
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
    api_instance = openapi_client.ConnectorsAmazonAdsApi(api_client)
    amazon_ads_connector_form = openapi_client.AmazonAdsConnectorForm() # AmazonAdsConnectorForm |  (optional)

    try:
        # Preview the data
        api_response = api_instance.amazon_ads_controller_action_preview(amazon_ads_connector_form=amazon_ads_connector_form)
        print("The response of ConnectorsAmazonAdsApi->amazon_ads_controller_action_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAmazonAdsApi->amazon_ads_controller_action_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amazon_ads_connector_form** | [**AmazonAdsConnectorForm**](AmazonAdsConnectorForm.md)|  | [optional] 

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

# **amazon_ads_controller_action_profile**
> List[LabelValueResponseInner] amazon_ads_controller_action_profile(request_body=request_body)

List of profile ids

### Example


```python
import openapi_client
from openapi_client.models.amazon_ads_controller_action_profile_request_value import AmazonAdsControllerActionProfileRequestValue
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
    api_instance = openapi_client.ConnectorsAmazonAdsApi(api_client)
    request_body = {'key': openapi_client.AmazonAdsControllerActionProfileRequestValue()} # Dict[str, AmazonAdsControllerActionProfileRequestValue] |  (optional)

    try:
        # List of profile ids
        api_response = api_instance.amazon_ads_controller_action_profile(request_body=request_body)
        print("The response of ConnectorsAmazonAdsApi->amazon_ads_controller_action_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAmazonAdsApi->amazon_ads_controller_action_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, AmazonAdsControllerActionProfileRequestValue]**](AmazonAdsControllerActionProfileRequestValue.md)|  | [optional] 

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
**200** | List of Amazon Ads profiles |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amazon_ads_controller_action_report_type**
> List[LabelValueResponseInner] amazon_ads_controller_action_report_type(request_body=request_body)

List Amazon Ads report types

### Example


```python
import openapi_client
from openapi_client.models.amazon_ads_controller_action_report_type_request_value import AmazonAdsControllerActionReportTypeRequestValue
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
    api_instance = openapi_client.ConnectorsAmazonAdsApi(api_client)
    request_body = {'key': openapi_client.AmazonAdsControllerActionReportTypeRequestValue()} # Dict[str, AmazonAdsControllerActionReportTypeRequestValue] |  (optional)

    try:
        # List Amazon Ads report types
        api_response = api_instance.amazon_ads_controller_action_report_type(request_body=request_body)
        print("The response of ConnectorsAmazonAdsApi->amazon_ads_controller_action_report_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAmazonAdsApi->amazon_ads_controller_action_report_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, AmazonAdsControllerActionReportTypeRequestValue]**](AmazonAdsControllerActionReportTypeRequestValue.md)|  | [optional] 

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
**200** | List of Amazon Ads report types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amazon_ads_controller_action_time_unit**
> List[LabelValueResponseInner] amazon_ads_controller_action_time_unit()

List Amazon Ads time units

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
    api_instance = openapi_client.ConnectorsAmazonAdsApi(api_client)

    try:
        # List Amazon Ads time units
        api_response = api_instance.amazon_ads_controller_action_time_unit()
        print("The response of ConnectorsAmazonAdsApi->amazon_ads_controller_action_time_unit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsAmazonAdsApi->amazon_ads_controller_action_time_unit: %s\n" % e)
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
**200** | List of available time units |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

