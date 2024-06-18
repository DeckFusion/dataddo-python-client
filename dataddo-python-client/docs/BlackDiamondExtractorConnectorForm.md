# BlackDiamondExtractorConnectorForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ensure_data_types** | **object** | Enforcing data types | [optional] 
**allow_empty** | **bool** |  | [optional] [default to True]
**nullable_fields** | **bool** |  | [optional] [default to True]
**connector_id** | **str** |  | 
**template_id** | **str** |  | 
**strategy** | **str** | Use storageStrategy instead. | [optional] 
**storage_strategy** | **str** |  | 
**label** | **str** | Label of the source | 
**flow** | **str** | Dataddo Flow endpoint | 
**token** | **str** | Dataddo token | 

## Example

```python
from openapi_client.models.black_diamond_extractor_connector_form import BlackDiamondExtractorConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of BlackDiamondExtractorConnectorForm from a JSON string
black_diamond_extractor_connector_form_instance = BlackDiamondExtractorConnectorForm.from_json(json)
# print the JSON string representation of the object
print(BlackDiamondExtractorConnectorForm.to_json())

# convert the object into a dict
black_diamond_extractor_connector_form_dict = black_diamond_extractor_connector_form_instance.to_dict()
# create an instance of BlackDiamondExtractorConnectorForm from a dict
black_diamond_extractor_connector_form_from_dict = BlackDiamondExtractorConnectorForm.from_dict(black_diamond_extractor_connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


