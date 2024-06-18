# JoinColumnRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**column** | **str** |  | [optional] 
**var_as** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.join_column_request import JoinColumnRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JoinColumnRequest from a JSON string
join_column_request_instance = JoinColumnRequest.from_json(json)
# print the JSON string representation of the object
print(JoinColumnRequest.to_json())

# convert the object into a dict
join_column_request_dict = join_column_request_instance.to_dict()
# create an instance of JoinColumnRequest from a dict
join_column_request_from_dict = JoinColumnRequest.from_dict(join_column_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


