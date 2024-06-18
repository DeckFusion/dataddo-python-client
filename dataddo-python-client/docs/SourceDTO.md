# SourceDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**Source**](Source.md) |  | [optional] 
**storage** | [**StorageSourceMeta**](StorageSourceMeta.md) |  | [optional] 
**engine** | [**SourceEngineDTO**](SourceEngineDTO.md) |  | [optional] 
**column** | [**List[SourceColumnDTO]**](SourceColumnDTO.md) |  | [optional] 
**id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**created** | **int** | Timestamp | [optional] 
**template_id** | **str** |  | [optional] 
**connector_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.source_dto import SourceDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SourceDTO from a JSON string
source_dto_instance = SourceDTO.from_json(json)
# print the JSON string representation of the object
print(SourceDTO.to_json())

# convert the object into a dict
source_dto_dict = source_dto_instance.to_dict()
# create an instance of SourceDTO from a dict
source_dto_from_dict = SourceDTO.from_dict(source_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


