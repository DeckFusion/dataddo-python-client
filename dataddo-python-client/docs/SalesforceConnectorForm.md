# SalesforceConnectorForm


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
**instance** | **str** |  | 
**object** | **str** |  | 
**api_version** | **str** |  | 
**filter** | **str** |  | [optional] 
**attribute** | **List[str]** | List of selected fields | 

## Example

```python
from openapi_client.models.salesforce_connector_form import SalesforceConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceConnectorForm from a JSON string
salesforce_connector_form_instance = SalesforceConnectorForm.from_json(json)
# print the JSON string representation of the object
print(SalesforceConnectorForm.to_json())

# convert the object into a dict
salesforce_connector_form_dict = salesforce_connector_form_instance.to_dict()
# create an instance of SalesforceConnectorForm from a dict
salesforce_connector_form_from_dict = SalesforceConnectorForm.from_dict(salesforce_connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


