# ActionCurrentState


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_id** | **str** |  | [optional] 
**status** | [**ActionStatusEnum**](ActionStatusEnum.md) |  | [optional] 
**last_run_started** | **datetime** |  | [optional] 
**last_run_finished** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.action_current_state import ActionCurrentState

# TODO update the JSON string below
json = "{}"
# create an instance of ActionCurrentState from a JSON string
action_current_state_instance = ActionCurrentState.from_json(json)
# print the JSON string representation of the object
print(ActionCurrentState.to_json())

# convert the object into a dict
action_current_state_dict = action_current_state_instance.to_dict()
# create an instance of ActionCurrentState from a dict
action_current_state_from_dict = ActionCurrentState.from_dict(action_current_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


