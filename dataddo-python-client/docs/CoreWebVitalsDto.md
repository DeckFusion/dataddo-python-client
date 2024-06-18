# CoreWebVitalsDto


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

## Example

```python
from openapi_client.models.core_web_vitals_dto import CoreWebVitalsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CoreWebVitalsDto from a JSON string
core_web_vitals_dto_instance = CoreWebVitalsDto.from_json(json)
# print the JSON string representation of the object
print(CoreWebVitalsDto.to_json())

# convert the object into a dict
core_web_vitals_dto_dict = core_web_vitals_dto_instance.to_dict()
# create an instance of CoreWebVitalsDto from a dict
core_web_vitals_dto_from_dict = CoreWebVitalsDto.from_dict(core_web_vitals_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


