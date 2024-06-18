# FlowOperationLeftJoin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | First Source ID | [optional] 
**target** | **str** | Second Source ID | [optional] 
**conditions** | [**List[FlowOperationJoinCondition]**](FlowOperationJoinCondition.md) |  | [optional] 
**columns** | [**List[FlowOperationColumn]**](FlowOperationColumn.md) |  | [optional] 

## Example

```python
from openapi_client.models.flow_operation_left_join import FlowOperationLeftJoin

# TODO update the JSON string below
json = "{}"
# create an instance of FlowOperationLeftJoin from a JSON string
flow_operation_left_join_instance = FlowOperationLeftJoin.from_json(json)
# print the JSON string representation of the object
print(FlowOperationLeftJoin.to_json())

# convert the object into a dict
flow_operation_left_join_dict = flow_operation_left_join_instance.to_dict()
# create an instance of FlowOperationLeftJoin from a dict
flow_operation_left_join_from_dict = FlowOperationLeftJoin.from_dict(flow_operation_left_join_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


