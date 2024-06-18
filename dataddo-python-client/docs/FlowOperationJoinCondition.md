# FlowOperationJoinCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_column** | **str** |  | [optional] 
**target_column** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.flow_operation_join_condition import FlowOperationJoinCondition

# TODO update the JSON string below
json = "{}"
# create an instance of FlowOperationJoinCondition from a JSON string
flow_operation_join_condition_instance = FlowOperationJoinCondition.from_json(json)
# print the JSON string representation of the object
print(FlowOperationJoinCondition.to_json())

# convert the object into a dict
flow_operation_join_condition_dict = flow_operation_join_condition_instance.to_dict()
# create an instance of FlowOperationJoinCondition from a dict
flow_operation_join_condition_from_dict = FlowOperationJoinCondition.from_dict(flow_operation_join_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


