# YoutubeAnalyticsControllerActionPlaylistRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**o_auth_id** | **str** |  | [optional] 
**channel_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.youtube_analytics_controller_action_playlist_request import YoutubeAnalyticsControllerActionPlaylistRequest

# TODO update the JSON string below
json = "{}"
# create an instance of YoutubeAnalyticsControllerActionPlaylistRequest from a JSON string
youtube_analytics_controller_action_playlist_request_instance = YoutubeAnalyticsControllerActionPlaylistRequest.from_json(json)
# print the JSON string representation of the object
print(YoutubeAnalyticsControllerActionPlaylistRequest.to_json())

# convert the object into a dict
youtube_analytics_controller_action_playlist_request_dict = youtube_analytics_controller_action_playlist_request_instance.to_dict()
# create an instance of YoutubeAnalyticsControllerActionPlaylistRequest from a dict
youtube_analytics_controller_action_playlist_request_from_dict = YoutubeAnalyticsControllerActionPlaylistRequest.from_dict(youtube_analytics_controller_action_playlist_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


