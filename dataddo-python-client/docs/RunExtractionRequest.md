# RunExtractionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**limit** | **str** |  | [optional] 
**date_from** | **str** | A \&quot;Y-m-d\&quot; formatted value | [optional] 
**date_to** | **str** | A \&quot;Y-m-d\&quot; formatted value | [optional] 
**date_range_expression** | **str** | A \&quot;{{1d1}}\&quot; formatted value | [optional] 
**storage_strategy** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.run_extraction_request import RunExtractionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunExtractionRequest from a JSON string
run_extraction_request_instance = RunExtractionRequest.from_json(json)
# print the JSON string representation of the object
print(RunExtractionRequest.to_json())

# convert the object into a dict
run_extraction_request_dict = run_extraction_request_instance.to_dict()
# create an instance of RunExtractionRequest from a dict
run_extraction_request_from_dict = RunExtractionRequest.from_dict(run_extraction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


