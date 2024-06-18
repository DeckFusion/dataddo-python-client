# MysqlDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**database** | **str** |  | [optional] 
**ssh_config** | [**AwsAuroraTraitSshConfig**](AwsAuroraTraitSshConfig.md) |  | [optional] 
**ssl** | **str** |  | [optional] 
**tls** | **str** |  | [optional] 
**extra_params** | **Dict[str, str]** | string&gt; | [optional] 
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
from openapi_client.models.mysql_dto_authorizer import MysqlDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of MysqlDtoAuthorizer from a JSON string
mysql_dto_authorizer_instance = MysqlDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(MysqlDtoAuthorizer.to_json())

# convert the object into a dict
mysql_dto_authorizer_dict = mysql_dto_authorizer_instance.to_dict()
# create an instance of MysqlDtoAuthorizer from a dict
mysql_dto_authorizer_from_dict = MysqlDtoAuthorizer.from_dict(mysql_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


