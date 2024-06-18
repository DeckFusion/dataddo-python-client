# InnerJoinRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**conditions** | [**List[JoinConditionRequest]**](JoinConditionRequest.md) |  | [optional] 
**columns** | [**List[JoinColumnRequest]**](JoinColumnRequest.md) |  | [optional] 

## Example

```python
from openapi_client.models.inner_join_request import InnerJoinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InnerJoinRequest from a JSON string
inner_join_request_instance = InnerJoinRequest.from_json(json)
# print the JSON string representation of the object
print(InnerJoinRequest.to_json())

# convert the object into a dict
inner_join_request_dict = inner_join_request_instance.to_dict()
# create an instance of InnerJoinRequest from a dict
inner_join_request_from_dict = InnerJoinRequest.from_dict(inner_join_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


