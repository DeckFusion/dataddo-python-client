# FlowOperationFormat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source ID | [optional] 
**formats** | [**List[FlowOperationFormatRules]**](FlowOperationFormatRules.md) | List of formatters to be applied | [optional] 

## Example

```python
from openapi_client.models.flow_operation_format import FlowOperationFormat

# TODO update the JSON string below
json = "{}"
# create an instance of FlowOperationFormat from a JSON string
flow_operation_format_instance = FlowOperationFormat.from_json(json)
# print the JSON string representation of the object
print(FlowOperationFormat.to_json())

# convert the object into a dict
flow_operation_format_dict = flow_operation_format_instance.to_dict()
# create an instance of FlowOperationFormat from a dict
flow_operation_format_from_dict = FlowOperationFormat.from_dict(flow_operation_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


