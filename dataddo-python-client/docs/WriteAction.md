# WriteAction


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
**write_mode** | **str** |  | [optional] 
**stream** | **bool** |  | [optional] 
**skip_bulk** | **bool** |  | [optional] 
**unique_columns** | **List[object]** |  | [optional] 
**setup_instructions** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.write_action import WriteAction

# TODO update the JSON string below
json = "{}"
# create an instance of WriteAction from a JSON string
write_action_instance = WriteAction.from_json(json)
# print the JSON string representation of the object
print(WriteAction.to_json())

# convert the object into a dict
write_action_dict = write_action_instance.to_dict()
# create an instance of WriteAction from a dict
write_action_from_dict = WriteAction.from_dict(write_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


