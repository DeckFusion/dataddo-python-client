# FlowOperationFilterRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **str** | Column ID | [optional] 
**comparator** | **str** | Comparator string (eg: &#x3D;&#x3D;, !&#x3D;, &gt;, &lt;. &gt;&#x3D;, &lt;&#x3D;, in) | [optional] 
**value** | **str** | Value to compare with | [optional] 

## Example

```python
from openapi_client.models.flow_operation_filter_rule import FlowOperationFilterRule

# TODO update the JSON string below
json = "{}"
# create an instance of FlowOperationFilterRule from a JSON string
flow_operation_filter_rule_instance = FlowOperationFilterRule.from_json(json)
# print the JSON string representation of the object
print(FlowOperationFilterRule.to_json())

# convert the object into a dict
flow_operation_filter_rule_dict = flow_operation_filter_rule_instance.to_dict()
# create an instance of FlowOperationFilterRule from a dict
flow_operation_filter_rule_from_dict = FlowOperationFilterRule.from_dict(flow_operation_filter_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


