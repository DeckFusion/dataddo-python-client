# UnionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**target** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.union_request import UnionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnionRequest from a JSON string
union_request_instance = UnionRequest.from_json(json)
# print the JSON string representation of the object
print(UnionRequest.to_json())

# convert the object into a dict
union_request_dict = union_request_instance.to_dict()
# create an instance of UnionRequest from a dict
union_request_from_dict = UnionRequest.from_dict(union_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


