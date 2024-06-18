# AmazonAdsConnectorForm


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
**profile_id** | **str** |  | 
**ad_product** | **str** | Amazon Ads Report Category (Ad Product) | 
**report_type** | **str** |  | 
**group_by** | **List[str]** |  | [optional] 
**time_unit** | **str** |  | [optional] 
**tactic** | **str** |  | [optional] 
**column** | **List[str]** |  | 

## Example

```python
from openapi_client.models.amazon_ads_connector_form import AmazonAdsConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonAdsConnectorForm from a JSON string
amazon_ads_connector_form_instance = AmazonAdsConnectorForm.from_json(json)
# print the JSON string representation of the object
print(AmazonAdsConnectorForm.to_json())

# convert the object into a dict
amazon_ads_connector_form_dict = amazon_ads_connector_form_instance.to_dict()
# create an instance of AmazonAdsConnectorForm from a dict
amazon_ads_connector_form_from_dict = AmazonAdsConnectorForm.from_dict(amazon_ads_connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


