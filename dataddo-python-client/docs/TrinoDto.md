# TrinoDto


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
from openapi_client.models.trino_dto import TrinoDto

# TODO update the JSON string below
json = "{}"
# create an instance of TrinoDto from a JSON string
trino_dto_instance = TrinoDto.from_json(json)
# print the JSON string representation of the object
print(TrinoDto.to_json())

# convert the object into a dict
trino_dto_dict = trino_dto_instance.to_dict()
# create an instance of TrinoDto from a dict
trino_dto_from_dict = TrinoDto.from_dict(trino_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


