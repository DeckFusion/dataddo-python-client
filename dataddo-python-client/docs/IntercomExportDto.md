# IntercomExportDto


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
**file** | **str** |  | [optional] 
**date_range** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.intercom_export_dto import IntercomExportDto

# TODO update the JSON string below
json = "{}"
# create an instance of IntercomExportDto from a JSON string
intercom_export_dto_instance = IntercomExportDto.from_json(json)
# print the JSON string representation of the object
print(IntercomExportDto.to_json())

# convert the object into a dict
intercom_export_dto_dict = intercom_export_dto_instance.to_dict()
# create an instance of IntercomExportDto from a dict
intercom_export_dto_from_dict = IntercomExportDto.from_dict(intercom_export_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


