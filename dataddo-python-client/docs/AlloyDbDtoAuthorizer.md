# AlloyDbDtoAuthorizer


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
from openapi_client.models.alloy_db_dto_authorizer import AlloyDbDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of AlloyDbDtoAuthorizer from a JSON string
alloy_db_dto_authorizer_instance = AlloyDbDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(AlloyDbDtoAuthorizer.to_json())

# convert the object into a dict
alloy_db_dto_authorizer_dict = alloy_db_dto_authorizer_instance.to_dict()
# create an instance of AlloyDbDtoAuthorizer from a dict
alloy_db_dto_authorizer_from_dict = AlloyDbDtoAuthorizer.from_dict(alloy_db_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


