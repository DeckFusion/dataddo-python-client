# PinterestConnectorForm


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
**label** | **str** | Label of the source | [optional] 
**o_auth_id** | **str** |  | [optional] 
**date_range** | **str** | Data range expression | [optional] 
**report_level** | **str** |  | [optional] 
**ad_account_ids** | **List[int]** |  | [optional] 
**column** | **List[str]** |  | [optional] 
**data_label** | **List[str]** |  | [optional] 
**engagement_window_days** | **str** |  | [optional] 
**view_window_days** | **str** |  | [optional] 
**conversion_report_time** | **str** |  | [optional] 
**granularity** | **str** |  | [optional] 
**click_window_days** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.pinterest_connector_form import PinterestConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of PinterestConnectorForm from a JSON string
pinterest_connector_form_instance = PinterestConnectorForm.from_json(json)
# print the JSON string representation of the object
print(PinterestConnectorForm.to_json())

# convert the object into a dict
pinterest_connector_form_dict = pinterest_connector_form_instance.to_dict()
# create an instance of PinterestConnectorForm from a dict
pinterest_connector_form_from_dict = PinterestConnectorForm.from_dict(pinterest_connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


