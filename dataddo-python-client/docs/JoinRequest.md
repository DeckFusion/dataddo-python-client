# JoinRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**conditions** | [**List[JoinConditionRequest]**](JoinConditionRequest.md) |  | [optional] 
**columns** | [**List[JoinColumnRequest]**](JoinColumnRequest.md) |  | [optional] 

## Example

```python
from openapi_client.models.join_request import JoinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JoinRequest from a JSON string
join_request_instance = JoinRequest.from_json(json)
# print the JSON string representation of the object
print(JoinRequest.to_json())

# convert the object into a dict
join_request_dict = join_request_instance.to_dict()
# create an instance of JoinRequest from a dict
join_request_from_dict = JoinRequest.from_dict(join_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


