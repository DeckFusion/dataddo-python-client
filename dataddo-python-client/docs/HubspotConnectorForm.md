# HubspotConnectorForm


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
**url** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**headers** | **List[object]** | HTTP Headers of the request | [optional] 
**body** | **str** |  | [optional] 
**transformation** | **str** |  | [optional] 
**emitter** | **str** |  | [optional] 
**parameters** | **List[str]** | Custom parameters supplied | [optional] 
**attributes** | **List[str]** | Final selections of the attributes to be included in the source | [optional] 
**object** | **str** |  | 
**var_property** | **List[str]** |  | 

## Example

```python
from openapi_client.models.hubspot_connector_form import HubspotConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of HubspotConnectorForm from a JSON string
hubspot_connector_form_instance = HubspotConnectorForm.from_json(json)
# print the JSON string representation of the object
print(HubspotConnectorForm.to_json())

# convert the object into a dict
hubspot_connector_form_dict = hubspot_connector_form_instance.to_dict()
# create an instance of HubspotConnectorForm from a dict
hubspot_connector_form_from_dict = HubspotConnectorForm.from_dict(hubspot_connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


