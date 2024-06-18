# AppAuthorizerAwsMssqlAwsMssqlAuthorizerCreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'aws_mssql']
**data** | [**AwsMssqlDtoAuthorizer**](AwsMssqlDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_aws_mssql_aws_mssql_authorizer_create_service_request import AppAuthorizerAwsMssqlAwsMssqlAuthorizerCreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerAwsMssqlAwsMssqlAuthorizerCreateServiceRequest from a JSON string
app_authorizer_aws_mssql_aws_mssql_authorizer_create_service_request_instance = AppAuthorizerAwsMssqlAwsMssqlAuthorizerCreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerAwsMssqlAwsMssqlAuthorizerCreateServiceRequest.to_json())

# convert the object into a dict
app_authorizer_aws_mssql_aws_mssql_authorizer_create_service_request_dict = app_authorizer_aws_mssql_aws_mssql_authorizer_create_service_request_instance.to_dict()
# create an instance of AppAuthorizerAwsMssqlAwsMssqlAuthorizerCreateServiceRequest from a dict
app_authorizer_aws_mssql_aws_mssql_authorizer_create_service_request_from_dict = AppAuthorizerAwsMssqlAwsMssqlAuthorizerCreateServiceRequest.from_dict(app_authorizer_aws_mssql_aws_mssql_authorizer_create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


