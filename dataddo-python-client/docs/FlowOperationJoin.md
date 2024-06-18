# FlowOperationJoin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | First Source ID | [optional] 
**target** | **str** | Second Source ID | [optional] 
**conditions** | [**List[FlowOperationJoinCondition]**](FlowOperationJoinCondition.md) |  | [optional] 
**columns** | [**List[FlowOperationColumn]**](FlowOperationColumn.md) |  | [optional] 

## Example

```python
from openapi_client.models.flow_operation_join import FlowOperationJoin

# TODO update the JSON string below
json = "{}"
# create an instance of FlowOperationJoin from a JSON string
flow_operation_join_instance = FlowOperationJoin.from_json(json)
# print the JSON string representation of the object
print(FlowOperationJoin.to_json())

# convert the object into a dict
flow_operation_join_dict = flow_operation_join_instance.to_dict()
# create an instance of FlowOperationJoin from a dict
flow_operation_join_from_dict = FlowOperationJoin.from_dict(flow_operation_join_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


