# MssqlDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_ssh** | **bool** |  | [optional] 
**certificate_id** | **str** |  | [optional] 
**ssh_host** | **str** |  | [optional] 
**ssh_port** | **int** |  | [optional] 
**ssh_remote_host** | **str** |  | [optional] 
**ssh_remote_port** | **int** |  | [optional] 
**ssh_username** | **str** |  | [optional] 
**ssh_password** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.mssql_dto_authorizer import MssqlDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of MssqlDtoAuthorizer from a JSON string
mssql_dto_authorizer_instance = MssqlDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(MssqlDtoAuthorizer.to_json())

# convert the object into a dict
mssql_dto_authorizer_dict = mssql_dto_authorizer_instance.to_dict()
# create an instance of MssqlDtoAuthorizer from a dict
mssql_dto_authorizer_from_dict = MssqlDtoAuthorizer.from_dict(mssql_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


