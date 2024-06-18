# OperationRequestUnion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**target** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.operation_request_union import OperationRequestUnion

# TODO update the JSON string below
json = "{}"
# create an instance of OperationRequestUnion from a JSON string
operation_request_union_instance = OperationRequestUnion.from_json(json)
# print the JSON string representation of the object
print(OperationRequestUnion.to_json())

# convert the object into a dict
operation_request_union_dict = operation_request_union_instance.to_dict()
# create an instance of OperationRequestUnion from a dict
operation_request_union_from_dict = OperationRequestUnion.from_dict(operation_request_union_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


