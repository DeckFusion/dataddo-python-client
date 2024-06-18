# NetsuiteDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**storage_strategy** | **str** |  | [optional] [default to 'incremental']
**allow_empty** | **bool** |  | [optional] [default to False]
**o_auth_id** | **int** |  | [optional] 
**attributes** | **List[object]** |  | [optional] 
**object** | **str** |  | [optional] 
**where** | **str** |  | [optional] 
**group_by** | **str** |  | [optional] 
**order_by** | **str** |  | [optional] 
**limit** | **int** |  | [optional] 
**query** | **str** |  | [optional] 
**date_range** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.netsuite_dto import NetsuiteDto

# TODO update the JSON string below
json = "{}"
# create an instance of NetsuiteDto from a JSON string
netsuite_dto_instance = NetsuiteDto.from_json(json)
# print the JSON string representation of the object
print(NetsuiteDto.to_json())

# convert the object into a dict
netsuite_dto_dict = netsuite_dto_instance.to_dict()
# create an instance of NetsuiteDto from a dict
netsuite_dto_from_dict = NetsuiteDto.from_dict(netsuite_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


