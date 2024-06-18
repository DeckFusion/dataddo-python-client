# SortRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sort_rule_request import SortRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SortRuleRequest from a JSON string
sort_rule_request_instance = SortRuleRequest.from_json(json)
# print the JSON string representation of the object
print(SortRuleRequest.to_json())

# convert the object into a dict
sort_rule_request_dict = sort_rule_request_instance.to_dict()
# create an instance of SortRuleRequest from a dict
sort_rule_request_from_dict = SortRuleRequest.from_dict(sort_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


