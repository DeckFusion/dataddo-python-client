# FlowPreviewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sources** | **List[str]** | List of sources to be used | [optional] 
**operations** | [**List[OperationRequest]**](OperationRequest.md) | List of DPI operations to be applied to sources defined above | [optional] 

## Example

```python
from openapi_client.models.flow_preview_request import FlowPreviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowPreviewRequest from a JSON string
flow_preview_request_instance = FlowPreviewRequest.from_json(json)
# print the JSON string representation of the object
print(FlowPreviewRequest.to_json())

# convert the object into a dict
flow_preview_request_dict = flow_preview_request_instance.to_dict()
# create an instance of FlowPreviewRequest from a dict
flow_preview_request_from_dict = FlowPreviewRequest.from_dict(flow_preview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


