# EverflowConnectorForm


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
**date_range** | **str** | Data range expression | [optional] 
**report_type** | **str** |  | 
**column** | **List[str]** |  | [optional] 
**time_column** | **str** |  | [optional] 
**timezone_id** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**metric** | **List[str]** |  | 

## Example

```python
from openapi_client.models.everflow_connector_form import EverflowConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of EverflowConnectorForm from a JSON string
everflow_connector_form_instance = EverflowConnectorForm.from_json(json)
# print the JSON string representation of the object
print(EverflowConnectorForm.to_json())

# convert the object into a dict
everflow_connector_form_dict = everflow_connector_form_instance.to_dict()
# create an instance of EverflowConnectorForm from a dict
everflow_connector_form_from_dict = EverflowConnectorForm.from_dict(everflow_connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


