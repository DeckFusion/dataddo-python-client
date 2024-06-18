# FlowOperationFormatRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **str** | Column ID | [optional] 
**column_wildcard** | **str** | If used will be used instead of column (eg. *, all_dates) | [optional] 
**function** | **str** | Formatting function to be used (eg: timestamp_to_string) | [optional] 
**format** | **str** | Style format to which the real value will be formatted to | [optional] 

## Example

```python
from openapi_client.models.flow_operation_format_rules import FlowOperationFormatRules

# TODO update the JSON string below
json = "{}"
# create an instance of FlowOperationFormatRules from a JSON string
flow_operation_format_rules_instance = FlowOperationFormatRules.from_json(json)
# print the JSON string representation of the object
print(FlowOperationFormatRules.to_json())

# convert the object into a dict
flow_operation_format_rules_dict = flow_operation_format_rules_instance.to_dict()
# create an instance of FlowOperationFormatRules from a dict
flow_operation_format_rules_from_dict = FlowOperationFormatRules.from_dict(flow_operation_format_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


