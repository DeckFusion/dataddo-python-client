# FtpDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**timeout** | **int** |  | [optional] 
**disable_explicit_tls** | **bool** |  | [optional] 
**dial_timeout** | **int** |  | [optional] 
**shut_timeout** | **int** |  | [optional] 
**disable_epsv** | **bool** |  | [optional] 
**disable_utf8** | **bool** |  | [optional] 
**disable_mlsd** | **bool** |  | [optional] 
**mdtm_write** | **bool** |  | [optional] 
**password** | **str** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ftp_dto_authorizer import FtpDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of FtpDtoAuthorizer from a JSON string
ftp_dto_authorizer_instance = FtpDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(FtpDtoAuthorizer.to_json())

# convert the object into a dict
ftp_dto_authorizer_dict = ftp_dto_authorizer_instance.to_dict()
# create an instance of FtpDtoAuthorizer from a dict
ftp_dto_authorizer_from_dict = FtpDtoAuthorizer.from_dict(ftp_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


