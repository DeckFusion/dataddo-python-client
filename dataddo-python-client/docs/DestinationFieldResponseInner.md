# DestinationFieldResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**unique** | **bool** |  | [optional] 
**required** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.destination_field_response_inner import DestinationFieldResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationFieldResponseInner from a JSON string
destination_field_response_inner_instance = DestinationFieldResponseInner.from_json(json)
# print the JSON string representation of the object
print(DestinationFieldResponseInner.to_json())

# convert the object into a dict
destination_field_response_inner_dict = destination_field_response_inner_instance.to_dict()
# create an instance of DestinationFieldResponseInner from a dict
destination_field_response_inner_from_dict = DestinationFieldResponseInner.from_dict(destination_field_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


