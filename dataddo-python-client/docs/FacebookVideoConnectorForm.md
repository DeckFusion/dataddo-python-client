# FacebookVideoConnectorForm


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
**page_id** | **str** |  | 
**metric** | **List[str]** |  | 
**data_label** | **List[str]** |  | 
**limit** | **int** |  | [default to 100]

## Example

```python
from openapi_client.models.facebook_video_connector_form import FacebookVideoConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of FacebookVideoConnectorForm from a JSON string
facebook_video_connector_form_instance = FacebookVideoConnectorForm.from_json(json)
# print the JSON string representation of the object
print(FacebookVideoConnectorForm.to_json())

# convert the object into a dict
facebook_video_connector_form_dict = facebook_video_connector_form_instance.to_dict()
# create an instance of FacebookVideoConnectorForm from a dict
facebook_video_connector_form_from_dict = FacebookVideoConnectorForm.from_dict(facebook_video_connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


