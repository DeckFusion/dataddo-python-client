# LabelValueResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.label_value_response_inner import LabelValueResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of LabelValueResponseInner from a JSON string
label_value_response_inner_instance = LabelValueResponseInner.from_json(json)
# print the JSON string representation of the object
print(LabelValueResponseInner.to_json())

# convert the object into a dict
label_value_response_inner_dict = label_value_response_inner_instance.to_dict()
# create an instance of LabelValueResponseInner from a dict
label_value_response_inner_from_dict = LabelValueResponseInner.from_dict(label_value_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


