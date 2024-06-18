# OperationRequestView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**strategy** | **str** |  | [optional] 
**columns** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.operation_request_view import OperationRequestView

# TODO update the JSON string below
json = "{}"
# create an instance of OperationRequestView from a JSON string
operation_request_view_instance = OperationRequestView.from_json(json)
# print the JSON string representation of the object
print(OperationRequestView.to_json())

# convert the object into a dict
operation_request_view_dict = operation_request_view_instance.to_dict()
# create an instance of OperationRequestView from a dict
operation_request_view_from_dict = OperationRequestView.from_dict(operation_request_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


