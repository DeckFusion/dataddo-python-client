# TrinoDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**user** | **str** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**catalog** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.trino_dto_authorizer import TrinoDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of TrinoDtoAuthorizer from a JSON string
trino_dto_authorizer_instance = TrinoDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(TrinoDtoAuthorizer.to_json())

# convert the object into a dict
trino_dto_authorizer_dict = trino_dto_authorizer_instance.to_dict()
# create an instance of TrinoDtoAuthorizer from a dict
trino_dto_authorizer_from_dict = TrinoDtoAuthorizer.from_dict(trino_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


