# ConnectorTemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** |  | [optional] 
**source_name** | **str** |  | [optional] 
**categories** | **List[object]** |  | [optional] 
**templates** | [**List[ConnectorTemplateResponseTemplatesInner]**](ConnectorTemplateResponseTemplatesInner.md) |  | [optional] 
**icon_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.connector_template_response import ConnectorTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorTemplateResponse from a JSON string
connector_template_response_instance = ConnectorTemplateResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectorTemplateResponse.to_json())

# convert the object into a dict
connector_template_response_dict = connector_template_response_instance.to_dict()
# create an instance of ConnectorTemplateResponse from a dict
connector_template_response_from_dict = ConnectorTemplateResponse.from_dict(connector_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


