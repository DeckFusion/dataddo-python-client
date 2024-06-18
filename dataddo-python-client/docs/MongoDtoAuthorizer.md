# MongoDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dsn** | **str** |  | [optional] 
**database** | **str** |  | [optional] 
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
from openapi_client.models.mongo_dto_authorizer import MongoDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of MongoDtoAuthorizer from a JSON string
mongo_dto_authorizer_instance = MongoDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(MongoDtoAuthorizer.to_json())

# convert the object into a dict
mongo_dto_authorizer_dict = mongo_dto_authorizer_instance.to_dict()
# create an instance of MongoDtoAuthorizer from a dict
mongo_dto_authorizer_from_dict = MongoDtoAuthorizer.from_dict(mongo_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


