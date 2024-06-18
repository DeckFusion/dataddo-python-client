# AppAuthorizerAwsMariadbAwsMariadbAuthorizerCreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'aws_mariadb']
**data** | [**AwsMariadbDtoAuthorizer**](AwsMariadbDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_aws_mariadb_aws_mariadb_authorizer_create_service_request import AppAuthorizerAwsMariadbAwsMariadbAuthorizerCreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerAwsMariadbAwsMariadbAuthorizerCreateServiceRequest from a JSON string
app_authorizer_aws_mariadb_aws_mariadb_authorizer_create_service_request_instance = AppAuthorizerAwsMariadbAwsMariadbAuthorizerCreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerAwsMariadbAwsMariadbAuthorizerCreateServiceRequest.to_json())

# convert the object into a dict
app_authorizer_aws_mariadb_aws_mariadb_authorizer_create_service_request_dict = app_authorizer_aws_mariadb_aws_mariadb_authorizer_create_service_request_instance.to_dict()
# create an instance of AppAuthorizerAwsMariadbAwsMariadbAuthorizerCreateServiceRequest from a dict
app_authorizer_aws_mariadb_aws_mariadb_authorizer_create_service_request_from_dict = AppAuthorizerAwsMariadbAwsMariadbAuthorizerCreateServiceRequest.from_dict(app_authorizer_aws_mariadb_aws_mariadb_authorizer_create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


