# AwsMssqlDtoAuthorizer


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
**label** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.aws_mssql_dto_authorizer import AwsMssqlDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMssqlDtoAuthorizer from a JSON string
aws_mssql_dto_authorizer_instance = AwsMssqlDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(AwsMssqlDtoAuthorizer.to_json())

# convert the object into a dict
aws_mssql_dto_authorizer_dict = aws_mssql_dto_authorizer_instance.to_dict()
# create an instance of AwsMssqlDtoAuthorizer from a dict
aws_mssql_dto_authorizer_from_dict = AwsMssqlDtoAuthorizer.from_dict(aws_mssql_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


