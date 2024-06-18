# AppAuthorizerAwsPgsqlAwsPgsqlAuthorizerCreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'aws_pgsql']
**data** | [**AwsPgsqlDtoAuthorizer**](AwsPgsqlDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_aws_pgsql_aws_pgsql_authorizer_create_service_request import AppAuthorizerAwsPgsqlAwsPgsqlAuthorizerCreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerAwsPgsqlAwsPgsqlAuthorizerCreateServiceRequest from a JSON string
app_authorizer_aws_pgsql_aws_pgsql_authorizer_create_service_request_instance = AppAuthorizerAwsPgsqlAwsPgsqlAuthorizerCreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerAwsPgsqlAwsPgsqlAuthorizerCreateServiceRequest.to_json())

# convert the object into a dict
app_authorizer_aws_pgsql_aws_pgsql_authorizer_create_service_request_dict = app_authorizer_aws_pgsql_aws_pgsql_authorizer_create_service_request_instance.to_dict()
# create an instance of AppAuthorizerAwsPgsqlAwsPgsqlAuthorizerCreateServiceRequest from a dict
app_authorizer_aws_pgsql_aws_pgsql_authorizer_create_service_request_from_dict = AppAuthorizerAwsPgsqlAwsPgsqlAuthorizerCreateServiceRequest.from_dict(app_authorizer_aws_pgsql_aws_pgsql_authorizer_create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


