# AppAuthorizerGoogleMssqlGoogleMssqlAuthorizerCreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'google_mssql']
**data** | [**GoogleMssqlDtoAuthorizer**](GoogleMssqlDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_google_mssql_google_mssql_authorizer_create_service_request import AppAuthorizerGoogleMssqlGoogleMssqlAuthorizerCreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerGoogleMssqlGoogleMssqlAuthorizerCreateServiceRequest from a JSON string
app_authorizer_google_mssql_google_mssql_authorizer_create_service_request_instance = AppAuthorizerGoogleMssqlGoogleMssqlAuthorizerCreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerGoogleMssqlGoogleMssqlAuthorizerCreateServiceRequest.to_json())

# convert the object into a dict
app_authorizer_google_mssql_google_mssql_authorizer_create_service_request_dict = app_authorizer_google_mssql_google_mssql_authorizer_create_service_request_instance.to_dict()
# create an instance of AppAuthorizerGoogleMssqlGoogleMssqlAuthorizerCreateServiceRequest from a dict
app_authorizer_google_mssql_google_mssql_authorizer_create_service_request_from_dict = AppAuthorizerGoogleMssqlGoogleMssqlAuthorizerCreateServiceRequest.from_dict(app_authorizer_google_mssql_google_mssql_authorizer_create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


