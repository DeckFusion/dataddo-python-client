# FlowOperationUnion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source #1 ID | [optional] 
**target** | **str** | Source #2 ID | [optional] 

## Example

```python
from openapi_client.models.flow_operation_union import FlowOperationUnion

# TODO update the JSON string below
json = "{}"
# create an instance of FlowOperationUnion from a JSON string
flow_operation_union_instance = FlowOperationUnion.from_json(json)
# print the JSON string representation of the object
print(FlowOperationUnion.to_json())

# convert the object into a dict
flow_operation_union_dict = flow_operation_union_instance.to_dict()
# create an instance of FlowOperationUnion from a dict
flow_operation_union_from_dict = FlowOperationUnion.from_dict(flow_operation_union_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


