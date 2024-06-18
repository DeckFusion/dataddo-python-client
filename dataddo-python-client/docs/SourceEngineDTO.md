# SourceEngineDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**encryption_key** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.source_engine_dto import SourceEngineDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SourceEngineDTO from a JSON string
source_engine_dto_instance = SourceEngineDTO.from_json(json)
# print the JSON string representation of the object
print(SourceEngineDTO.to_json())

# convert the object into a dict
source_engine_dto_dict = source_engine_dto_instance.to_dict()
# create an instance of SourceEngineDTO from a dict
source_engine_dto_from_dict = SourceEngineDTO.from_dict(source_engine_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


