# SourceColumnDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**hash** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.source_column_dto import SourceColumnDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SourceColumnDTO from a JSON string
source_column_dto_instance = SourceColumnDTO.from_json(json)
# print the JSON string representation of the object
print(SourceColumnDTO.to_json())

# convert the object into a dict
source_column_dto_dict = source_column_dto_instance.to_dict()
# create an instance of SourceColumnDTO from a dict
source_column_dto_from_dict = SourceColumnDTO.from_dict(source_column_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


