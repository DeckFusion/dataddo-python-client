# FlowOperationLimit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source ID | [optional] 
**index** | **int** | Offset identifier | [optional] 
**length** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.flow_operation_limit import FlowOperationLimit

# TODO update the JSON string below
json = "{}"
# create an instance of FlowOperationLimit from a JSON string
flow_operation_limit_instance = FlowOperationLimit.from_json(json)
# print the JSON string representation of the object
print(FlowOperationLimit.to_json())

# convert the object into a dict
flow_operation_limit_dict = flow_operation_limit_instance.to_dict()
# create an instance of FlowOperationLimit from a dict
flow_operation_limit_from_dict = FlowOperationLimit.from_dict(flow_operation_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


