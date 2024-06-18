# FlowOperationView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source ID | [optional] 
**strategy** | **str** | Strategy name (eg. keep/discard) | [optional] 
**columns** | **List[str]** | Column IDs | [optional] 

## Example

```python
from openapi_client.models.flow_operation_view import FlowOperationView

# TODO update the JSON string below
json = "{}"
# create an instance of FlowOperationView from a JSON string
flow_operation_view_instance = FlowOperationView.from_json(json)
# print the JSON string representation of the object
print(FlowOperationView.to_json())

# convert the object into a dict
flow_operation_view_dict = flow_operation_view_instance.to_dict()
# create an instance of FlowOperationView from a dict
flow_operation_view_from_dict = FlowOperationView.from_dict(flow_operation_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


