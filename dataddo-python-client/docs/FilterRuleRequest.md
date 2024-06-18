# FilterRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **str** |  | [optional] 
**comparator** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.filter_rule_request import FilterRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FilterRuleRequest from a JSON string
filter_rule_request_instance = FilterRuleRequest.from_json(json)
# print the JSON string representation of the object
print(FilterRuleRequest.to_json())

# convert the object into a dict
filter_rule_request_dict = filter_rule_request_instance.to_dict()
# create an instance of FilterRuleRequest from a dict
filter_rule_request_from_dict = FilterRuleRequest.from_dict(filter_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


