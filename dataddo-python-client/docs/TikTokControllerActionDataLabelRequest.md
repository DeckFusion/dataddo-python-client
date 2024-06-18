# TikTokControllerActionDataLabelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_type** | **str** |  | [optional] 
**id_dimension** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tik_tok_controller_action_data_label_request import TikTokControllerActionDataLabelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TikTokControllerActionDataLabelRequest from a JSON string
tik_tok_controller_action_data_label_request_instance = TikTokControllerActionDataLabelRequest.from_json(json)
# print the JSON string representation of the object
print(TikTokControllerActionDataLabelRequest.to_json())

# convert the object into a dict
tik_tok_controller_action_data_label_request_dict = tik_tok_controller_action_data_label_request_instance.to_dict()
# create an instance of TikTokControllerActionDataLabelRequest from a dict
tik_tok_controller_action_data_label_request_from_dict = TikTokControllerActionDataLabelRequest.from_dict(tik_tok_controller_action_data_label_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


