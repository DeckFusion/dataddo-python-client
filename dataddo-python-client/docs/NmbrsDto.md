# NmbrsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**storage_strategy** | **str** |  | [optional] [default to 'incremental']
**allow_empty** | **bool** |  | [optional] [default to False]
**request** | [**HttpConnectorDtoRequest**](HttpConnectorDtoRequest.md) |  | [optional] 
**o_auth_id** | **int** |  | [optional] 
**company** | **str** |  | [optional] 
**dataset** | **str** |  | [optional] 
**date_range** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.nmbrs_dto import NmbrsDto

# TODO update the JSON string below
json = "{}"
# create an instance of NmbrsDto from a JSON string
nmbrs_dto_instance = NmbrsDto.from_json(json)
# print the JSON string representation of the object
print(NmbrsDto.to_json())

# convert the object into a dict
nmbrs_dto_dict = nmbrs_dto_instance.to_dict()
# create an instance of NmbrsDto from a dict
nmbrs_dto_from_dict = NmbrsDto.from_dict(nmbrs_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


