# Flow

Class Flow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary key of document. The value is null when document is not persisted. | [optional] 
**label** | **object** | Label | [optional] 
**user_id** | **object** | User customerId instead. | [optional] 
**customer_id** | **object** | Customer | [optional] 
**source** | [**List[FlowSource]**](FlowSource.md) | The list of sources that are involved in the flow | [optional] 
**tag** | **List[str]** |  | [optional] 
**operation** | [**List[FlowOperation]**](FlowOperation.md) | The list of operations to be run in DPI on the data | [optional] 
**rules** | [**List[FlowDataQualityRule]**](FlowDataQualityRule.md) | The list of data quality rules | [optional] 
**api** | [**FlowApi**](FlowApi.md) |  | [optional] 
**write_action** | [**FlowWriteAction**](FlowWriteAction.md) |  | [optional] 

## Example

```python
from openapi_client.models.flow import Flow

# TODO update the JSON string below
json = "{}"
# create an instance of Flow from a JSON string
flow_instance = Flow.from_json(json)
# print the JSON string representation of the object
print(Flow.to_json())

# convert the object into a dict
flow_dict = flow_instance.to_dict()
# create an instance of Flow from a dict
flow_from_dict = Flow.from_dict(flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


