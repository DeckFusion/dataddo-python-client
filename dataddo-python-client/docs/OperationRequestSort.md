# OperationRequestSort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**rules** | [**List[SortRuleRequest]**](SortRuleRequest.md) |  | [optional] 

## Example

```python
from openapi_client.models.operation_request_sort import OperationRequestSort

# TODO update the JSON string below
json = "{}"
# create an instance of OperationRequestSort from a JSON string
operation_request_sort_instance = OperationRequestSort.from_json(json)
# print the JSON string representation of the object
print(OperationRequestSort.to_json())

# convert the object into a dict
operation_request_sort_dict = operation_request_sort_instance.to_dict()
# create an instance of OperationRequestSort from a dict
operation_request_sort_from_dict = OperationRequestSort.from_dict(operation_request_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


