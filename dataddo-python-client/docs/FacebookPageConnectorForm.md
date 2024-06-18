# FacebookPageConnectorForm


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
**page_id** | **str** |  | 
**metric** | **List[str]** |  | 
**data_label** | **List[str]** |  | 

## Example

```python
from openapi_client.models.facebook_page_connector_form import FacebookPageConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of FacebookPageConnectorForm from a JSON string
facebook_page_connector_form_instance = FacebookPageConnectorForm.from_json(json)
# print the JSON string representation of the object
print(FacebookPageConnectorForm.to_json())

# convert the object into a dict
facebook_page_connector_form_dict = facebook_page_connector_form_instance.to_dict()
# create an instance of FacebookPageConnectorForm from a dict
facebook_page_connector_form_from_dict = FacebookPageConnectorForm.from_dict(facebook_page_connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


