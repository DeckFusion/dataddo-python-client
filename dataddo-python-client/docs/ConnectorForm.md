# ConnectorForm


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

## Example

```python
from openapi_client.models.connector_form import ConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorForm from a JSON string
connector_form_instance = ConnectorForm.from_json(json)
# print the JSON string representation of the object
print(ConnectorForm.to_json())

# convert the object into a dict
connector_form_dict = connector_form_instance.to_dict()
# create an instance of ConnectorForm from a dict
connector_form_from_dict = ConnectorForm.from_dict(connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


