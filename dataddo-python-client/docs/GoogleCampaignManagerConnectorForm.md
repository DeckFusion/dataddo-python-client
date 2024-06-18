# GoogleCampaignManagerConnectorForm


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
**o_auth_id** | **str** |  | 
**date_range** | **str** | Data range expression | [optional] 
**profile_id** | **str** |  | 
**report_type** | **str** |  | 
**date_range_expression** | **str** |  | 

## Example

```python
from openapi_client.models.google_campaign_manager_connector_form import GoogleCampaignManagerConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleCampaignManagerConnectorForm from a JSON string
google_campaign_manager_connector_form_instance = GoogleCampaignManagerConnectorForm.from_json(json)
# print the JSON string representation of the object
print(GoogleCampaignManagerConnectorForm.to_json())

# convert the object into a dict
google_campaign_manager_connector_form_dict = google_campaign_manager_connector_form_instance.to_dict()
# create an instance of GoogleCampaignManagerConnectorForm from a dict
google_campaign_manager_connector_form_from_dict = GoogleCampaignManagerConnectorForm.from_dict(google_campaign_manager_connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


