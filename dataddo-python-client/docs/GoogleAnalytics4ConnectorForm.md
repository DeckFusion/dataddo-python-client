# GoogleAnalytics4ConnectorForm


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
**use_dataddo_hash** | **bool** | Include Dataddo hash (to be used for upsert) | [optional] 
**account_id** | **str** |  | [optional] 
**property_id** | **str** |  | 
**sub_property_id** | **str** |  | [optional] 
**property_ids** | **List[str]** |  | [optional] 
**metric** | **List[str]** |  | 
**dimension** | **List[str]** |  | 
**limit** | **int** |  | [optional] [default to 10000]
**dimension_filter** | **str** |  | [optional] 
**metric_filter** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.google_analytics4_connector_form import GoogleAnalytics4ConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAnalytics4ConnectorForm from a JSON string
google_analytics4_connector_form_instance = GoogleAnalytics4ConnectorForm.from_json(json)
# print the JSON string representation of the object
print(GoogleAnalytics4ConnectorForm.to_json())

# convert the object into a dict
google_analytics4_connector_form_dict = google_analytics4_connector_form_instance.to_dict()
# create an instance of GoogleAnalytics4ConnectorForm from a dict
google_analytics4_connector_form_from_dict = GoogleAnalytics4ConnectorForm.from_dict(google_analytics4_connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


