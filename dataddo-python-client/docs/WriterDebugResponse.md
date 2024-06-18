# WriterDebugResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**started** | **float** |  | [optional] 
**ended** | **float** |  | [optional] 
**duration** | **str** |  | [optional] 
**memory_mb** | **int** |  | [optional] 
**connection_result** | [**WriterDebugResponseAllOfConnectionResult**](WriterDebugResponseAllOfConnectionResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.writer_debug_response import WriterDebugResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WriterDebugResponse from a JSON string
writer_debug_response_instance = WriterDebugResponse.from_json(json)
# print the JSON string representation of the object
print(WriterDebugResponse.to_json())

# convert the object into a dict
writer_debug_response_dict = writer_debug_response_instance.to_dict()
# create an instance of WriterDebugResponse from a dict
writer_debug_response_from_dict = WriterDebugResponse.from_dict(writer_debug_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


