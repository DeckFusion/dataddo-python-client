# OperationRequestFormat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**rules** | [**List[FormatRuleRequest]**](FormatRuleRequest.md) |  | [optional] 

## Example

```python
from openapi_client.models.operation_request_format import OperationRequestFormat

# TODO update the JSON string below
json = "{}"
# create an instance of OperationRequestFormat from a JSON string
operation_request_format_instance = OperationRequestFormat.from_json(json)
# print the JSON string representation of the object
print(OperationRequestFormat.to_json())

# convert the object into a dict
operation_request_format_dict = operation_request_format_instance.to_dict()
# create an instance of OperationRequestFormat from a dict
operation_request_format_from_dict = OperationRequestFormat.from_dict(operation_request_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

