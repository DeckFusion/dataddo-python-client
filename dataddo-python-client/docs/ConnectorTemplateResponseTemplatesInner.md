# ConnectorTemplateResponseTemplatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**category_id** | **List[object]** |  | [optional] 
**attributes** | **List[object]** |  | [optional] 

## Example

```python
from openapi_client.models.connector_template_response_templates_inner import ConnectorTemplateResponseTemplatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorTemplateResponseTemplatesInner from a JSON string
connector_template_response_templates_inner_instance = ConnectorTemplateResponseTemplatesInner.from_json(json)
# print the JSON string representation of the object
print(ConnectorTemplateResponseTemplatesInner.to_json())

# convert the object into a dict
connector_template_response_templates_inner_dict = connector_template_response_templates_inner_instance.to_dict()
# create an instance of ConnectorTemplateResponseTemplatesInner from a dict
connector_template_response_templates_inner_from_dict = ConnectorTemplateResponseTemplatesInner.from_dict(connector_template_response_templates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


