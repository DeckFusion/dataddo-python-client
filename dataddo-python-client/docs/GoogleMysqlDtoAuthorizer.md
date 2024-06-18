# GoogleMysqlDtoAuthorizer


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
from openapi_client.models.google_mysql_dto_authorizer import GoogleMysqlDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleMysqlDtoAuthorizer from a JSON string
google_mysql_dto_authorizer_instance = GoogleMysqlDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(GoogleMysqlDtoAuthorizer.to_json())

# convert the object into a dict
google_mysql_dto_authorizer_dict = google_mysql_dto_authorizer_instance.to_dict()
# create an instance of GoogleMysqlDtoAuthorizer from a dict
google_mysql_dto_authorizer_from_dict = GoogleMysqlDtoAuthorizer.from_dict(google_mysql_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


