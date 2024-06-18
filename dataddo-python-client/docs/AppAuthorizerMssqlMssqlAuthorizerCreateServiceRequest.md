# AppAuthorizerMssqlMssqlAuthorizerCreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'mssql']
**data** | [**MssqlDtoAuthorizer**](MssqlDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_mssql_mssql_authorizer_create_service_request import AppAuthorizerMssqlMssqlAuthorizerCreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerMssqlMssqlAuthorizerCreateServiceRequest from a JSON string
app_authorizer_mssql_mssql_authorizer_create_service_request_instance = AppAuthorizerMssqlMssqlAuthorizerCreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerMssqlMssqlAuthorizerCreateServiceRequest.to_json())

# convert the object into a dict
app_authorizer_mssql_mssql_authorizer_create_service_request_dict = app_authorizer_mssql_mssql_authorizer_create_service_request_instance.to_dict()
# create an instance of AppAuthorizerMssqlMssqlAuthorizerCreateServiceRequest from a dict
app_authorizer_mssql_mssql_authorizer_create_service_request_from_dict = AppAuthorizerMssqlMssqlAuthorizerCreateServiceRequest.from_dict(app_authorizer_mssql_mssql_authorizer_create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


