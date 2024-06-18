# SortRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**rules** | [**List[SortRuleRequest]**](SortRuleRequest.md) |  | [optional] 

## Example

```python
from openapi_client.models.sort_request import SortRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SortRequest from a JSON string
sort_request_instance = SortRequest.from_json(json)
# print the JSON string representation of the object
print(SortRequest.to_json())

# convert the object into a dict
sort_request_dict = sort_request_instance.to_dict()
# create an instance of SortRequest from a dict
sort_request_from_dict = SortRequest.from_dict(sort_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


