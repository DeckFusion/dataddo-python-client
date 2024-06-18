# FacebookLeadsControllerActionFormRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**o_auth_id** | **str** |  | [optional] 
**page_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.facebook_leads_controller_action_form_request import FacebookLeadsControllerActionFormRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FacebookLeadsControllerActionFormRequest from a JSON string
facebook_leads_controller_action_form_request_instance = FacebookLeadsControllerActionFormRequest.from_json(json)
# print the JSON string representation of the object
print(FacebookLeadsControllerActionFormRequest.to_json())

# convert the object into a dict
facebook_leads_controller_action_form_request_dict = facebook_leads_controller_action_form_request_instance.to_dict()
# create an instance of FacebookLeadsControllerActionFormRequest from a dict
facebook_leads_controller_action_form_request_from_dict = FacebookLeadsControllerActionFormRequest.from_dict(facebook_leads_controller_action_form_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


