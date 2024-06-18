# MssqlDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**storage_strategy** | **str** |  | [optional] [default to 'incremental']
**allow_empty** | **bool** |  | [optional] [default to False]
**o_auth_id** | **int** |  | [optional] 
**statement** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.mssql_dto import MssqlDto

# TODO update the JSON string below
json = "{}"
# create an instance of MssqlDto from a JSON string
mssql_dto_instance = MssqlDto.from_json(json)
# print the JSON string representation of the object
print(MssqlDto.to_json())

# convert the object into a dict
mssql_dto_dict = mssql_dto_instance.to_dict()
# create an instance of MssqlDto from a dict
mssql_dto_from_dict = MssqlDto.from_dict(mssql_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


