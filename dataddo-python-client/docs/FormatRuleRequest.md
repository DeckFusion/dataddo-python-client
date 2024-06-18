# FormatRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **str** |  | [optional] 
**column_wildcard** | **str** |  | [optional] 
**function** | **str** |  | [optional] 
**format** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.format_rule_request import FormatRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FormatRuleRequest from a JSON string
format_rule_request_instance = FormatRuleRequest.from_json(json)
# print the JSON string representation of the object
print(FormatRuleRequest.to_json())

# convert the object into a dict
format_rule_request_dict = format_rule_request_instance.to_dict()
# create an instance of FormatRuleRequest from a dict
format_rule_request_from_dict = FormatRuleRequest.from_dict(format_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


