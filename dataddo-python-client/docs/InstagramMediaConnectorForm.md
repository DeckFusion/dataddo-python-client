# InstagramMediaConnectorForm


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
**account_id** | **str** |  | 
**attribute** | **List[str]** |  | 

## Example

```python
from openapi_client.models.instagram_media_connector_form import InstagramMediaConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of InstagramMediaConnectorForm from a JSON string
instagram_media_connector_form_instance = InstagramMediaConnectorForm.from_json(json)
# print the JSON string representation of the object
print(InstagramMediaConnectorForm.to_json())

# convert the object into a dict
instagram_media_connector_form_dict = instagram_media_connector_form_instance.to_dict()
# create an instance of InstagramMediaConnectorForm from a dict
instagram_media_connector_form_from_dict = InstagramMediaConnectorForm.from_dict(instagram_media_connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


