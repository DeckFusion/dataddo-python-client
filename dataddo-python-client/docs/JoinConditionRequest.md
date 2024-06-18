# JoinConditionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_column** | **str** |  | [optional] 
**target_column** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.join_condition_request import JoinConditionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JoinConditionRequest from a JSON string
join_condition_request_instance = JoinConditionRequest.from_json(json)
# print the JSON string representation of the object
print(JoinConditionRequest.to_json())

# convert the object into a dict
join_condition_request_dict = join_condition_request_instance.to_dict()
# create an instance of JoinConditionRequest from a dict
join_condition_request_from_dict = JoinConditionRequest.from_dict(join_condition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


