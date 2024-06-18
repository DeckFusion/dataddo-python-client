# FlowOperationColumn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**column** | **str** |  | [optional] 
**var_as** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.flow_operation_column import FlowOperationColumn

# TODO update the JSON string below
json = "{}"
# create an instance of FlowOperationColumn from a JSON string
flow_operation_column_instance = FlowOperationColumn.from_json(json)
# print the JSON string representation of the object
print(FlowOperationColumn.to_json())

# convert the object into a dict
flow_operation_column_dict = flow_operation_column_instance.to_dict()
# create an instance of FlowOperationColumn from a dict
flow_operation_column_from_dict = FlowOperationColumn.from_dict(flow_operation_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


