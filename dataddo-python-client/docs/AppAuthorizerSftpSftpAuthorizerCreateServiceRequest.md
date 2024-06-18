# AppAuthorizerSftpSftpAuthorizerCreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'sftp']
**data** | [**SftpDtoAuthorizer**](SftpDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_sftp_sftp_authorizer_create_service_request import AppAuthorizerSftpSftpAuthorizerCreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerSftpSftpAuthorizerCreateServiceRequest from a JSON string
app_authorizer_sftp_sftp_authorizer_create_service_request_instance = AppAuthorizerSftpSftpAuthorizerCreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerSftpSftpAuthorizerCreateServiceRequest.to_json())

# convert the object into a dict
app_authorizer_sftp_sftp_authorizer_create_service_request_dict = app_authorizer_sftp_sftp_authorizer_create_service_request_instance.to_dict()
# create an instance of AppAuthorizerSftpSftpAuthorizerCreateServiceRequest from a dict
app_authorizer_sftp_sftp_authorizer_create_service_request_from_dict = AppAuthorizerSftpSftpAuthorizerCreateServiceRequest.from_dict(app_authorizer_sftp_sftp_authorizer_create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


