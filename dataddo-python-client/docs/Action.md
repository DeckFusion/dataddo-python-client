# Action


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary key of document. The value is null when document is not persisted. | [optional] 
**status** | **str** |  | [optional] 
**status_detail** | **str** |  | [optional] 
**duration** | **str** | Duration | [optional] 
**object_id** | **object** | Object ID | [optional] 
**object_type** | **str** | Object type | [optional] 
**type** | **str** | Action type | [optional] 
**customer_id** | **str** | Customer ID | [optional] 
**last_execution** | **int** | Last execution timestamp | [optional] 
**next_execution** | **int** | Next execution timestamp. Makes sense only for actions with schedule, otherwise it is null. It is computed and updated based on the schedule change or when action is executed. | [optional] 
**error_count** | **int** | Error iteration count | [optional] 
**is_being_processed** | **bool** | Is the action currently being processed? | [optional] 
**on_error_retry_timeout** | **int** | After how many seconds the action should be retried if it is failed. Default is 0 meaning run retry on next Dispatcher&#39;s tick.  Example: set to 60*60*2 to retry action not earlier than 2hrs after failure | [optional] 
**schedule** | **object** | Action Schedule settings | [optional] 

## Example

```python
from openapi_client.models.action import Action

# TODO update the JSON string below
json = "{}"
# create an instance of Action from a JSON string
action_instance = Action.from_json(json)
# print the JSON string representation of the object
print(Action.to_json())

# convert the object into a dict
action_dict = action_instance.to_dict()
# create an instance of Action from a dict
action_from_dict = Action.from_dict(action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


