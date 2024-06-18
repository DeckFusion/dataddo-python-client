# AmazonAdsDataExtractorConnectorForm


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
**flow** | **str** | Dataddo Flow endpoint | 
**token** | **str** | Dataddo token | 

## Example

```python
from openapi_client.models.amazon_ads_data_extractor_connector_form import AmazonAdsDataExtractorConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonAdsDataExtractorConnectorForm from a JSON string
amazon_ads_data_extractor_connector_form_instance = AmazonAdsDataExtractorConnectorForm.from_json(json)
# print the JSON string representation of the object
print(AmazonAdsDataExtractorConnectorForm.to_json())

# convert the object into a dict
amazon_ads_data_extractor_connector_form_dict = amazon_ads_data_extractor_connector_form_instance.to_dict()
# create an instance of AmazonAdsDataExtractorConnectorForm from a dict
amazon_ads_data_extractor_connector_form_from_dict = AmazonAdsDataExtractorConnectorForm.from_dict(amazon_ads_data_extractor_connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


