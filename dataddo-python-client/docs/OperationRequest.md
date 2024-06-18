# OperationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**output** | **str** |  | [optional] 
**union** | [**OperationRequestUnion**](OperationRequestUnion.md) |  | [optional] 
**left_join** | [**OperationRequestLeftJoin**](OperationRequestLeftJoin.md) |  | [optional] 
**inner_join** | [**OperationRequestInnerJoin**](OperationRequestInnerJoin.md) |  | [optional] 
**view** | [**OperationRequestView**](OperationRequestView.md) |  | [optional] 
**limit** | [**OperationRequestLimit**](OperationRequestLimit.md) |  | [optional] 
**sort** | [**OperationRequestSort**](OperationRequestSort.md) |  | [optional] 
**filter** | [**OperationRequestFilter**](OperationRequestFilter.md) |  | [optional] 
**format** | [**OperationRequestFormat**](OperationRequestFormat.md) |  | [optional] 

## Example

```python
from openapi_client.models.operation_request import OperationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OperationRequest from a JSON string
operation_request_instance = OperationRequest.from_json(json)
# print the JSON string representation of the object
print(OperationRequest.to_json())

# convert the object into a dict
operation_request_dict = operation_request_instance.to_dict()
# create an instance of OperationRequest from a dict
operation_request_from_dict = OperationRequest.from_dict(operation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


