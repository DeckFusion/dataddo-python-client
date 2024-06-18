# ExtractionAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary key of document. The value is null when document is not persisted. | [optional] 
**status** | **str** |  | [optional] 
**status_detail** | **str** |  | [optional] 
**duration** | **str** | Duration | [optional] 
**object_id** | **object** | Object ID | [optional] 
**object_type** | **str** | Object type | [optional] 
**type** | **object** |  | [optional] 
**customer_id** | **str** | Customer ID | [optional] 
**last_execution** | **int** | Last execution timestamp | [optional] 
**next_execution** | **int** | Next execution timestamp. Makes sense only for actions with schedule, otherwise it is null. It is computed and updated based on the schedule change or when action is executed. | [optional] 
**error_count** | **int** | Error iteration count | [optional] 
**is_being_processed** | **bool** | Is the action currently being processed? | [optional] 
**on_error_retry_timeout** | **int** | After how many seconds the action should be retried if it is failed. Default is 0 meaning run retry on next Dispatcher&#39;s tick.  Example: set to 60*60*2 to retry action not earlier than 2hrs after failure | [optional] 
**schedule** | **object** | Action Schedule settings | [optional] 
**storage** | **str** | Use storageStrategy instead. | [optional] 
**storage_strategy** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.extraction_action import ExtractionAction

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractionAction from a JSON string
extraction_action_instance = ExtractionAction.from_json(json)
# print the JSON string representation of the object
print(ExtractionAction.to_json())

# convert the object into a dict
extraction_action_dict = extraction_action_instance.to_dict()
# create an instance of ExtractionAction from a dict
extraction_action_from_dict = ExtractionAction.from_dict(extraction_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


