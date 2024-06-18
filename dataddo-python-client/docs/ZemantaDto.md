# ZemantaDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**storage_strategy** | **str** |  | [optional] [default to 'incremental']
**allow_empty** | **bool** |  | [optional] [default to False]
**o_auth_id** | **int** |  | [optional] 
**date_range** | **str** |  | [optional] 
**metrics** | **List[object]** |  | [optional] 
**entities** | **List[object]** |  | [optional] 
**options** | **List[object]** |  | [optional] 
**filters** | **str** |  | [optional] 
**account** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.zemanta_dto import ZemantaDto

# TODO update the JSON string below
json = "{}"
# create an instance of ZemantaDto from a JSON string
zemanta_dto_instance = ZemantaDto.from_json(json)
# print the JSON string representation of the object
print(ZemantaDto.to_json())

# convert the object into a dict
zemanta_dto_dict = zemanta_dto_instance.to_dict()
# create an instance of ZemantaDto from a dict
zemanta_dto_from_dict = ZemantaDto.from_dict(zemanta_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


