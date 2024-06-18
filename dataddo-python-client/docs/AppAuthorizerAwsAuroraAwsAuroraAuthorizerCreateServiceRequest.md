# AppAuthorizerAwsAuroraAwsAuroraAuthorizerCreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'aws_aurora']
**data** | [**AwsAuroraDtoAuthorizer**](AwsAuroraDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_aws_aurora_aws_aurora_authorizer_create_service_request import AppAuthorizerAwsAuroraAwsAuroraAuthorizerCreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerAwsAuroraAwsAuroraAuthorizerCreateServiceRequest from a JSON string
app_authorizer_aws_aurora_aws_aurora_authorizer_create_service_request_instance = AppAuthorizerAwsAuroraAwsAuroraAuthorizerCreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerAwsAuroraAwsAuroraAuthorizerCreateServiceRequest.to_json())

# convert the object into a dict
app_authorizer_aws_aurora_aws_aurora_authorizer_create_service_request_dict = app_authorizer_aws_aurora_aws_aurora_authorizer_create_service_request_instance.to_dict()
# create an instance of AppAuthorizerAwsAuroraAwsAuroraAuthorizerCreateServiceRequest from a dict
app_authorizer_aws_aurora_aws_aurora_authorizer_create_service_request_from_dict = AppAuthorizerAwsAuroraAwsAuroraAuthorizerCreateServiceRequest.from_dict(app_authorizer_aws_aurora_aws_aurora_authorizer_create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


