# OperationRequestLeftJoin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**conditions** | [**List[JoinConditionRequest]**](JoinConditionRequest.md) |  | [optional] 
**columns** | [**List[JoinColumnRequest]**](JoinColumnRequest.md) |  | [optional] 

## Example

```python
from openapi_client.models.operation_request_left_join import OperationRequestLeftJoin

# TODO update the JSON string below
json = "{}"
# create an instance of OperationRequestLeftJoin from a JSON string
operation_request_left_join_instance = OperationRequestLeftJoin.from_json(json)
# print the JSON string representation of the object
print(OperationRequestLeftJoin.to_json())

# convert the object into a dict
operation_request_left_join_dict = operation_request_left_join_instance.to_dict()
# create an instance of OperationRequestLeftJoin from a dict
operation_request_left_join_from_dict = OperationRequestLeftJoin.from_dict(operation_request_left_join_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


