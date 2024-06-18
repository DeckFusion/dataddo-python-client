# AppAuthorizerAwsAuroraPgsqlAwsAuroraPgsqlAuthorizerCreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'aws_aurora_pgsql']
**data** | [**AwsAuroraPgsqlDtoAuthorizer**](AwsAuroraPgsqlDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_aws_aurora_pgsql_aws_aurora_pgsql_authorizer_create_service_request import AppAuthorizerAwsAuroraPgsqlAwsAuroraPgsqlAuthorizerCreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerAwsAuroraPgsqlAwsAuroraPgsqlAuthorizerCreateServiceRequest from a JSON string
app_authorizer_aws_aurora_pgsql_aws_aurora_pgsql_authorizer_create_service_request_instance = AppAuthorizerAwsAuroraPgsqlAwsAuroraPgsqlAuthorizerCreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerAwsAuroraPgsqlAwsAuroraPgsqlAuthorizerCreateServiceRequest.to_json())

# convert the object into a dict
app_authorizer_aws_aurora_pgsql_aws_aurora_pgsql_authorizer_create_service_request_dict = app_authorizer_aws_aurora_pgsql_aws_aurora_pgsql_authorizer_create_service_request_instance.to_dict()
# create an instance of AppAuthorizerAwsAuroraPgsqlAwsAuroraPgsqlAuthorizerCreateServiceRequest from a dict
app_authorizer_aws_aurora_pgsql_aws_aurora_pgsql_authorizer_create_service_request_from_dict = AppAuthorizerAwsAuroraPgsqlAwsAuroraPgsqlAuthorizerCreateServiceRequest.from_dict(app_authorizer_aws_aurora_pgsql_aws_aurora_pgsql_authorizer_create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


