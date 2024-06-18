# FlowOperationSort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source ID | [optional] 
**rules** | [**List[FlowOperationSortRules]**](FlowOperationSortRules.md) | List of filters to be applied | [optional] 

## Example

```python
from openapi_client.models.flow_operation_sort import FlowOperationSort

# TODO update the JSON string below
json = "{}"
# create an instance of FlowOperationSort from a JSON string
flow_operation_sort_instance = FlowOperationSort.from_json(json)
# print the JSON string representation of the object
print(FlowOperationSort.to_json())

# convert the object into a dict
flow_operation_sort_dict = flow_operation_sort_instance.to_dict()
# create an instance of FlowOperationSort from a dict
flow_operation_sort_from_dict = FlowOperationSort.from_dict(flow_operation_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


