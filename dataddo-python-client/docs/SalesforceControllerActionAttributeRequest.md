# SalesforceControllerActionAttributeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**o_auth_id** | **str** |  | [optional] 
**instance** | **str** |  | [optional] 
**api_version** | **str** |  | [optional] 
**object** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.salesforce_controller_action_attribute_request import SalesforceControllerActionAttributeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceControllerActionAttributeRequest from a JSON string
salesforce_controller_action_attribute_request_instance = SalesforceControllerActionAttributeRequest.from_json(json)
# print the JSON string representation of the object
print(SalesforceControllerActionAttributeRequest.to_json())

# convert the object into a dict
salesforce_controller_action_attribute_request_dict = salesforce_controller_action_attribute_request_instance.to_dict()
# create an instance of SalesforceControllerActionAttributeRequest from a dict
salesforce_controller_action_attribute_request_from_dict = SalesforceControllerActionAttributeRequest.from_dict(salesforce_controller_action_attribute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


