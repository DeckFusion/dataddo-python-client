# BlackDiamondBatchConnectorForm


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
**o_auth_id** | **str** |  | 
**object** | **str** |  | 
**metrics** | **List[str]** |  | 

## Example

```python
from openapi_client.models.black_diamond_batch_connector_form import BlackDiamondBatchConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of BlackDiamondBatchConnectorForm from a JSON string
black_diamond_batch_connector_form_instance = BlackDiamondBatchConnectorForm.from_json(json)
# print the JSON string representation of the object
print(BlackDiamondBatchConnectorForm.to_json())

# convert the object into a dict
black_diamond_batch_connector_form_dict = black_diamond_batch_connector_form_instance.to_dict()
# create an instance of BlackDiamondBatchConnectorForm from a dict
black_diamond_batch_connector_form_from_dict = BlackDiamondBatchConnectorForm.from_dict(black_diamond_batch_connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


