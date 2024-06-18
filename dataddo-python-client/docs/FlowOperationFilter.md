# FlowOperationFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Source ID | [optional] 
**filters** | [**List[FlowOperationFilterRule]**](FlowOperationFilterRule.md) | List of filters to be applied | [optional] 

## Example

```python
from openapi_client.models.flow_operation_filter import FlowOperationFilter

# TODO update the JSON string below
json = "{}"
# create an instance of FlowOperationFilter from a JSON string
flow_operation_filter_instance = FlowOperationFilter.from_json(json)
# print the JSON string representation of the object
print(FlowOperationFilter.to_json())

# convert the object into a dict
flow_operation_filter_dict = flow_operation_filter_instance.to_dict()
# create an instance of FlowOperationFilter from a dict
flow_operation_filter_from_dict = FlowOperationFilter.from_dict(flow_operation_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


