# SnapchatConnectorForm


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
**date_range** | **str** | Data range expression | 
**organization_id** | **str** | Snapchat Organization identifier | 
**account_id** | **str** | Snapchat Ad Account identifier | 
**metrics** | **List[str]** |  | 
**labels** | **List[str]** |  | 
**breakdown** | **str** |  | 
**action_report_time** | **str** |  | 
**swipe_up_attribution_window** | **str** |  | 
**view_attribution_window** | **str** |  | 

## Example

```python
from openapi_client.models.snapchat_connector_form import SnapchatConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of SnapchatConnectorForm from a JSON string
snapchat_connector_form_instance = SnapchatConnectorForm.from_json(json)
# print the JSON string representation of the object
print(SnapchatConnectorForm.to_json())

# convert the object into a dict
snapchat_connector_form_dict = snapchat_connector_form_instance.to_dict()
# create an instance of SnapchatConnectorForm from a dict
snapchat_connector_form_from_dict = SnapchatConnectorForm.from_dict(snapchat_connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


