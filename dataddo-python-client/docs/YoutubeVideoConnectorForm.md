# YoutubeVideoConnectorForm


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
**channel_id** | **str** | Your channel id | 
**playlist_id** | **str** | Your playlist id | 
**attribute** | **List[str]** | YT attributes | 

## Example

```python
from openapi_client.models.youtube_video_connector_form import YoutubeVideoConnectorForm

# TODO update the JSON string below
json = "{}"
# create an instance of YoutubeVideoConnectorForm from a JSON string
youtube_video_connector_form_instance = YoutubeVideoConnectorForm.from_json(json)
# print the JSON string representation of the object
print(YoutubeVideoConnectorForm.to_json())

# convert the object into a dict
youtube_video_connector_form_dict = youtube_video_connector_form_instance.to_dict()
# create an instance of YoutubeVideoConnectorForm from a dict
youtube_video_connector_form_from_dict = YoutubeVideoConnectorForm.from_dict(youtube_video_connector_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


