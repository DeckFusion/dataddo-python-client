# LeftJoinRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**conditions** | [**List[JoinConditionRequest]**](JoinConditionRequest.md) |  | [optional] 
**columns** | [**List[JoinColumnRequest]**](JoinColumnRequest.md) |  | [optional] 

## Example

```python
from openapi_client.models.left_join_request import LeftJoinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LeftJoinRequest from a JSON string
left_join_request_instance = LeftJoinRequest.from_json(json)
# print the JSON string representation of the object
print(LeftJoinRequest.to_json())

# convert the object into a dict
left_join_request_dict = left_join_request_instance.to_dict()
# create an instance of LeftJoinRequest from a dict
left_join_request_from_dict = LeftJoinRequest.from_dict(left_join_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


