# FilterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**rules** | [**List[FilterRuleRequest]**](FilterRuleRequest.md) |  | [optional] 

## Example

```python
from openapi_client.models.filter_request import FilterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FilterRequest from a JSON string
filter_request_instance = FilterRequest.from_json(json)
# print the JSON string representation of the object
print(FilterRequest.to_json())

# convert the object into a dict
filter_request_dict = filter_request_instance.to_dict()
# create an instance of FilterRequest from a dict
filter_request_from_dict = FilterRequest.from_dict(filter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


