# LimitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**index** | **int** |  | [optional] 
**length** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.limit_request import LimitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LimitRequest from a JSON string
limit_request_instance = LimitRequest.from_json(json)
# print the JSON string representation of the object
print(LimitRequest.to_json())

# convert the object into a dict
limit_request_dict = limit_request_instance.to_dict()
# create an instance of LimitRequest from a dict
limit_request_from_dict = LimitRequest.from_dict(limit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


