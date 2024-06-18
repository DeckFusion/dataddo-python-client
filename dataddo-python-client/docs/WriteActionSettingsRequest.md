# WriteActionSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**write_mode** | **str** |  | [optional] 
**unique_columns** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.write_action_settings_request import WriteActionSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WriteActionSettingsRequest from a JSON string
write_action_settings_request_instance = WriteActionSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(WriteActionSettingsRequest.to_json())

# convert the object into a dict
write_action_settings_request_dict = write_action_settings_request_instance.to_dict()
# create an instance of WriteActionSettingsRequest from a dict
write_action_settings_request_from_dict = WriteActionSettingsRequest.from_dict(write_action_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


