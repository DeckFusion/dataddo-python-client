# DebugResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**started** | **float** |  | [optional] 
**ended** | **float** |  | [optional] 
**duration** | **str** |  | [optional] 
**memory_mb** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.debug_response import DebugResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DebugResponse from a JSON string
debug_response_instance = DebugResponse.from_json(json)
# print the JSON string representation of the object
print(DebugResponse.to_json())

# convert the object into a dict
debug_response_dict = debug_response_instance.to_dict()
# create an instance of DebugResponse from a dict
debug_response_from_dict = DebugResponse.from_dict(debug_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


