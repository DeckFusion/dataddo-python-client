# HubspotControllerActionPropertyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**o_auth_id** | **str** |  | [optional] 
**object** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.hubspot_controller_action_property_request import HubspotControllerActionPropertyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HubspotControllerActionPropertyRequest from a JSON string
hubspot_controller_action_property_request_instance = HubspotControllerActionPropertyRequest.from_json(json)
# print the JSON string representation of the object
print(HubspotControllerActionPropertyRequest.to_json())

# convert the object into a dict
hubspot_controller_action_property_request_dict = hubspot_controller_action_property_request_instance.to_dict()
# create an instance of HubspotControllerActionPropertyRequest from a dict
hubspot_controller_action_property_request_from_dict = HubspotControllerActionPropertyRequest.from_dict(hubspot_controller_action_property_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


