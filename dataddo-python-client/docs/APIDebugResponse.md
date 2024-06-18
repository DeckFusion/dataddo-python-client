# APIDebugResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**started** | **float** |  | [optional] 
**ended** | **float** |  | [optional] 
**duration** | **str** |  | [optional] 
**memory_mb** | **int** |  | [optional] 
**logs** | **List[object]** |  | [optional] 

## Example

```python
from openapi_client.models.api_debug_response import APIDebugResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIDebugResponse from a JSON string
api_debug_response_instance = APIDebugResponse.from_json(json)
# print the JSON string representation of the object
print(APIDebugResponse.to_json())

# convert the object into a dict
api_debug_response_dict = api_debug_response_instance.to_dict()
# create an instance of APIDebugResponse from a dict
api_debug_response_from_dict = APIDebugResponse.from_dict(api_debug_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


