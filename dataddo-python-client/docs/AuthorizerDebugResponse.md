# AuthorizerDebugResponse


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
from openapi_client.models.authorizer_debug_response import AuthorizerDebugResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizerDebugResponse from a JSON string
authorizer_debug_response_instance = AuthorizerDebugResponse.from_json(json)
# print the JSON string representation of the object
print(AuthorizerDebugResponse.to_json())

# convert the object into a dict
authorizer_debug_response_dict = authorizer_debug_response_instance.to_dict()
# create an instance of AuthorizerDebugResponse from a dict
authorizer_debug_response_from_dict = AuthorizerDebugResponse.from_dict(authorizer_debug_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


