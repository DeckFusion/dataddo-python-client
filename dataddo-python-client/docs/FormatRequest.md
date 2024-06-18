# FormatRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**rules** | [**List[FormatRuleRequest]**](FormatRuleRequest.md) |  | [optional] 

## Example

```python
from openapi_client.models.format_request import FormatRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FormatRequest from a JSON string
format_request_instance = FormatRequest.from_json(json)
# print the JSON string representation of the object
print(FormatRequest.to_json())

# convert the object into a dict
format_request_dict = format_request_instance.to_dict()
# create an instance of FormatRequest from a dict
format_request_from_dict = FormatRequest.from_dict(format_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


