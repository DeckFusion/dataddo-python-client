# MemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**email** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.member_request import MemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MemberRequest from a JSON string
member_request_instance = MemberRequest.from_json(json)
# print the JSON string representation of the object
print(MemberRequest.to_json())

# convert the object into a dict
member_request_dict = member_request_instance.to_dict()
# create an instance of MemberRequest from a dict
member_request_from_dict = MemberRequest.from_dict(member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


