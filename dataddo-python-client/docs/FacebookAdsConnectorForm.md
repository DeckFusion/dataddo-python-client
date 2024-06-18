# FacebookAdsConnectorForm


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
**use_dataddo_hash** | **bool** | Include Dataddo hash (to be used for upsert) | [optional] 
**account_id** | **str** |  | 
**campaign_id** | **str** |  | [optional] 
**ad_set_id** | **str** |  | [optional] 
**time_breakup** | **str** |  | [default to 'all_days']
**level** | **str** |  | 
**metric** | **List[str]** |  | 
**breakdown** | **List[str]** |  | [optional] 
**data_label** | **List[str]** |  | 

## Example

```python
from openapi_client.models.facebook_ads_connector_form import FacebookAdsConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of FacebookAdsConnectorForm from a JSON string
facebook_ads_connector_form_instance = FacebookAdsConnectorForm.from_json(json)
# print the JSON string representation of the object
print(FacebookAdsConnectorForm.to_json())

# convert the object into a dict
facebook_ads_connector_form_dict = facebook_ads_connector_form_instance.to_dict()
# create an instance of FacebookAdsConnectorForm from a dict
facebook_ads_connector_form_from_dict = FacebookAdsConnectorForm.from_dict(facebook_ads_connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


