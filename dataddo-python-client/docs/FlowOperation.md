# FlowOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The operation name (left_join, right_join, sort, ...) | [optional] 
**output** | **str** | Name of the output. By this name it may be used in following operation as a source. | [optional] 
**union** | [**FlowOperationUnion**](FlowOperationUnion.md) |  | [optional] 
**left_join** | [**FlowOperationLeftJoin**](FlowOperationLeftJoin.md) |  | [optional] 
**inner_join** | [**FlowOperationInnerJoin**](FlowOperationInnerJoin.md) |  | [optional] 
**view** | [**FlowOperationView**](FlowOperationView.md) |  | [optional] 
**filter** | [**FlowOperationFilter**](FlowOperationFilter.md) |  | [optional] 
**limit** | [**FlowOperationLimit**](FlowOperationLimit.md) |  | [optional] 
**format** | [**FlowOperationFormat**](FlowOperationFormat.md) |  | [optional] 
**sort** | [**FlowOperationSort**](FlowOperationSort.md) |  | [optional] 

## Example

```python
from openapi_client.models.flow_operation import FlowOperation

# TODO update the JSON string below
json = "{}"
# create an instance of FlowOperation from a JSON string
flow_operation_instance = FlowOperation.from_json(json)
# print the JSON string representation of the object
print(FlowOperation.to_json())

# convert the object into a dict
flow_operation_dict = flow_operation_instance.to_dict()
# create an instance of FlowOperation from a dict
flow_operation_from_dict = FlowOperation.from_dict(flow_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


