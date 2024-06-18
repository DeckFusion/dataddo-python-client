# SnapchatLookupConnectorForm


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
**organization_id** | **str** |  | 
**account_id** | **str** |  | 
**level** | **str** |  | 
**attribute** | **List[str]** | Snapchat attributes | 

## Example

```python
from openapi_client.models.snapchat_lookup_connector_form import SnapchatLookupConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of SnapchatLookupConnectorForm from a JSON string
snapchat_lookup_connector_form_instance = SnapchatLookupConnectorForm.from_json(json)
# print the JSON string representation of the object
print(SnapchatLookupConnectorForm.to_json())

# convert the object into a dict
snapchat_lookup_connector_form_dict = snapchat_lookup_connector_form_instance.to_dict()
# create an instance of SnapchatLookupConnectorForm from a dict
snapchat_lookup_connector_form_from_dict = SnapchatLookupConnectorForm.from_dict(snapchat_lookup_connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


