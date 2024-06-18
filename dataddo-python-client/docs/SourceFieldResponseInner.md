# SourceFieldResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.source_field_response_inner import SourceFieldResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of SourceFieldResponseInner from a JSON string
source_field_response_inner_instance = SourceFieldResponseInner.from_json(json)
# print the JSON string representation of the object
print(SourceFieldResponseInner.to_json())

# convert the object into a dict
source_field_response_inner_dict = source_field_response_inner_instance.to_dict()
# create an instance of SourceFieldResponseInner from a dict
source_field_response_inner_from_dict = SourceFieldResponseInner.from_dict(source_field_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


