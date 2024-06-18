# FlowOperationInnerJoin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | First Source ID | [optional] 
**target** | **str** | Second Source ID | [optional] 
**conditions** | [**List[FlowOperationJoinCondition]**](FlowOperationJoinCondition.md) |  | [optional] 
**columns** | [**List[FlowOperationColumn]**](FlowOperationColumn.md) |  | [optional] 

## Example

```python
from openapi_client.models.flow_operation_inner_join import FlowOperationInnerJoin

# TODO update the JSON string below
json = "{}"
# create an instance of FlowOperationInnerJoin from a JSON string
flow_operation_inner_join_instance = FlowOperationInnerJoin.from_json(json)
# print the JSON string representation of the object
print(FlowOperationInnerJoin.to_json())

# convert the object into a dict
flow_operation_inner_join_dict = flow_operation_inner_join_instance.to_dict()
# create an instance of FlowOperationInnerJoin from a dict
flow_operation_inner_join_from_dict = FlowOperationInnerJoin.from_dict(flow_operation_inner_join_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


