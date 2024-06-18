# PgsqlWalDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**storage_strategy** | **str** |  | [optional] [default to 'incremental']
**allow_empty** | **bool** |  | [optional] [default to False]
**o_auth_id** | **int** |  | [optional] 
**table** | **str** |  | [optional] 
**statement** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.pgsql_wal_dto import PgsqlWalDto

# TODO update the JSON string below
json = "{}"
# create an instance of PgsqlWalDto from a JSON string
pgsql_wal_dto_instance = PgsqlWalDto.from_json(json)
# print the JSON string representation of the object
print(PgsqlWalDto.to_json())

# convert the object into a dict
pgsql_wal_dto_dict = pgsql_wal_dto_instance.to_dict()
# create an instance of PgsqlWalDto from a dict
pgsql_wal_dto_from_dict = PgsqlWalDto.from_dict(pgsql_wal_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


