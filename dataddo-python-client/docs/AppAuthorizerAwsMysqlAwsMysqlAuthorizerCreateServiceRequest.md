# AppAuthorizerAwsMysqlAwsMysqlAuthorizerCreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'aws_mysql']
**data** | [**AwsMysqlDtoAuthorizer**](AwsMysqlDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_aws_mysql_aws_mysql_authorizer_create_service_request import AppAuthorizerAwsMysqlAwsMysqlAuthorizerCreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerAwsMysqlAwsMysqlAuthorizerCreateServiceRequest from a JSON string
app_authorizer_aws_mysql_aws_mysql_authorizer_create_service_request_instance = AppAuthorizerAwsMysqlAwsMysqlAuthorizerCreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerAwsMysqlAwsMysqlAuthorizerCreateServiceRequest.to_json())

# convert the object into a dict
app_authorizer_aws_mysql_aws_mysql_authorizer_create_service_request_dict = app_authorizer_aws_mysql_aws_mysql_authorizer_create_service_request_instance.to_dict()
# create an instance of AppAuthorizerAwsMysqlAwsMysqlAuthorizerCreateServiceRequest from a dict
app_authorizer_aws_mysql_aws_mysql_authorizer_create_service_request_from_dict = AppAuthorizerAwsMysqlAwsMysqlAuthorizerCreateServiceRequest.from_dict(app_authorizer_aws_mysql_aws_mysql_authorizer_create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


