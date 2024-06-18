# AppAuthorizerS3S3AuthorizerCreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 's3']
**data** | [**S3DtoAuthorizer**](S3DtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_s3_s3_authorizer_create_service_request import AppAuthorizerS3S3AuthorizerCreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerS3S3AuthorizerCreateServiceRequest from a JSON string
app_authorizer_s3_s3_authorizer_create_service_request_instance = AppAuthorizerS3S3AuthorizerCreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerS3S3AuthorizerCreateServiceRequest.to_json())

# convert the object into a dict
app_authorizer_s3_s3_authorizer_create_service_request_dict = app_authorizer_s3_s3_authorizer_create_service_request_instance.to_dict()
# create an instance of AppAuthorizerS3S3AuthorizerCreateServiceRequest from a dict
app_authorizer_s3_s3_authorizer_create_service_request_from_dict = AppAuthorizerS3S3AuthorizerCreateServiceRequest.from_dict(app_authorizer_s3_s3_authorizer_create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


