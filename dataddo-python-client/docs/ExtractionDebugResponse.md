# ExtractionDebugResponse


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
**row_count** | **int** |  | [optional] 
**blob** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.extraction_debug_response import ExtractionDebugResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractionDebugResponse from a JSON string
extraction_debug_response_instance = ExtractionDebugResponse.from_json(json)
# print the JSON string representation of the object
print(ExtractionDebugResponse.to_json())

# convert the object into a dict
extraction_debug_response_dict = extraction_debug_response_instance.to_dict()
# create an instance of ExtractionDebugResponse from a dict
extraction_debug_response_from_dict = ExtractionDebugResponse.from_dict(extraction_debug_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


