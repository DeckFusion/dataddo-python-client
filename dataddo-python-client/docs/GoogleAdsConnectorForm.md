# GoogleAdsConnectorForm


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
**use_dataddo_hash** | **bool** | Include Dataddo hash (to be used for upsert) | [optional] 
**google_customer_id** | **str** | Google Customer Id | [optional] 
**customer_client_id** | **str** | Google Customer Client Id | [optional] 
**attribute** | **List[str]** |  | [optional] 
**segment** | **List[str]** |  | [optional] 
**metric** | **List[str]** |  | [optional] 
**report_type** | **str** |  | [optional] 
**where_filter** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.google_ads_connector_form import GoogleAdsConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsConnectorForm from a JSON string
google_ads_connector_form_instance = GoogleAdsConnectorForm.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsConnectorForm.to_json())

# convert the object into a dict
google_ads_connector_form_dict = google_ads_connector_form_instance.to_dict()
# create an instance of GoogleAdsConnectorForm from a dict
google_ads_connector_form_from_dict = GoogleAdsConnectorForm.from_dict(google_ads_connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


