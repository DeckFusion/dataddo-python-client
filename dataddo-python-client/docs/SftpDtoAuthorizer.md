# SftpDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**timeout** | **int** |  | [optional] 
**certificate_id** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**certificate_password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sftp_dto_authorizer import SftpDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of SftpDtoAuthorizer from a JSON string
sftp_dto_authorizer_instance = SftpDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(SftpDtoAuthorizer.to_json())

# convert the object into a dict
sftp_dto_authorizer_dict = sftp_dto_authorizer_instance.to_dict()
# create an instance of SftpDtoAuthorizer from a dict
sftp_dto_authorizer_from_dict = SftpDtoAuthorizer.from_dict(sftp_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


