# ActionEnqueuedDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_id** | **str** |  | [optional] 
**action_id** | **str** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**action_type** | **object** |  | [optional] 
**connector** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.action_enqueued_dto import ActionEnqueuedDto

# TODO update the JSON string below
json = "{}"
# create an instance of ActionEnqueuedDto from a JSON string
action_enqueued_dto_instance = ActionEnqueuedDto.from_json(json)
# print the JSON string representation of the object
print(ActionEnqueuedDto.to_json())

# convert the object into a dict
action_enqueued_dto_dict = action_enqueued_dto_instance.to_dict()
# create an instance of ActionEnqueuedDto from a dict
action_enqueued_dto_from_dict = ActionEnqueuedDto.from_dict(action_enqueued_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


