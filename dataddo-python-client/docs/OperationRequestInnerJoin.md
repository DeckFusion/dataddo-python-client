# OperationRequestInnerJoin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**conditions** | [**List[JoinConditionRequest]**](JoinConditionRequest.md) |  | [optional] 
**columns** | [**List[JoinColumnRequest]**](JoinColumnRequest.md) |  | [optional] 

## Example

```python
from openapi_client.models.operation_request_inner_join import OperationRequestInnerJoin

# TODO update the JSON string below
json = "{}"
# create an instance of OperationRequestInnerJoin from a JSON string
operation_request_inner_join_instance = OperationRequestInnerJoin.from_json(json)
# print the JSON string representation of the object
print(OperationRequestInnerJoin.to_json())

# convert the object into a dict
operation_request_inner_join_dict = operation_request_inner_join_instance.to_dict()
# create an instance of OperationRequestInnerJoin from a dict
operation_request_inner_join_from_dict = OperationRequestInnerJoin.from_dict(operation_request_inner_join_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


