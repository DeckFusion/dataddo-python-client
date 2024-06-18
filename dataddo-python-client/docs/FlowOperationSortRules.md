# FlowOperationSortRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **str** | Column ID | [optional] 
**direction** | **str** | Direction (eg. Asc, Desc) | [optional] 

## Example

```python
from openapi_client.models.flow_operation_sort_rules import FlowOperationSortRules

# TODO update the JSON string below
json = "{}"
# create an instance of FlowOperationSortRules from a JSON string
flow_operation_sort_rules_instance = FlowOperationSortRules.from_json(json)
# print the JSON string representation of the object
print(FlowOperationSortRules.to_json())

# convert the object into a dict
flow_operation_sort_rules_dict = flow_operation_sort_rules_instance.to_dict()
# create an instance of FlowOperationSortRules from a dict
flow_operation_sort_rules_from_dict = FlowOperationSortRules.from_dict(flow_operation_sort_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


