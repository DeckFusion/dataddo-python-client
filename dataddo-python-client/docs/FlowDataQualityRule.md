# FlowDataQualityRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_id** | **str** |  | [optional] 
**rule** | **str** |  | [optional] 
**action** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.flow_data_quality_rule import FlowDataQualityRule

# TODO update the JSON string below
json = "{}"
# create an instance of FlowDataQualityRule from a JSON string
flow_data_quality_rule_instance = FlowDataQualityRule.from_json(json)
# print the JSON string representation of the object
print(FlowDataQualityRule.to_json())

# convert the object into a dict
flow_data_quality_rule_dict = flow_data_quality_rule_instance.to_dict()
# create an instance of FlowDataQualityRule from a dict
flow_data_quality_rule_from_dict = FlowDataQualityRule.from_dict(flow_data_quality_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


