# YoutubeAnalyticsConnectorForm


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
**url** | **str** |  | 
**method** | **str** |  | 
**headers** | **List[object]** | HTTP Headers of the request | [optional] 
**body** | **str** |  | [optional] 
**transformation** | **str** |  | 
**emitter** | **str** |  | [optional] 
**parameters** | **List[str]** | Custom parameters supplied | [optional] 
**attributes** | **List[str]** | Final selections of the attributes to be included in the source | 

## Example

```python
from openapi_client.models.youtube_analytics_connector_form import YoutubeAnalyticsConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of YoutubeAnalyticsConnectorForm from a JSON string
youtube_analytics_connector_form_instance = YoutubeAnalyticsConnectorForm.from_json(json)
# print the JSON string representation of the object
print(YoutubeAnalyticsConnectorForm.to_json())

# convert the object into a dict
youtube_analytics_connector_form_dict = youtube_analytics_connector_form_instance.to_dict()
# create an instance of YoutubeAnalyticsConnectorForm from a dict
youtube_analytics_connector_form_from_dict = YoutubeAnalyticsConnectorForm.from_dict(youtube_analytics_connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


