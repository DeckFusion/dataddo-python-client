# OperationRequestFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**rules** | [**List[FilterRuleRequest]**](FilterRuleRequest.md) |  | [optional] 

## Example

```python
from openapi_client.models.operation_request_filter import OperationRequestFilter

# TODO update the JSON string below
json = "{}"
# create an instance of OperationRequestFilter from a JSON string
operation_request_filter_instance = OperationRequestFilter.from_json(json)
# print the JSON string representation of the object
print(OperationRequestFilter.to_json())

# convert the object into a dict
operation_request_filter_dict = operation_request_filter_instance.to_dict()
# create an instance of OperationRequestFilter from a dict
operation_request_filter_from_dict = OperationRequestFilter.from_dict(operation_request_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


