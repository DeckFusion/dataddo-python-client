# MailchimpControllerActionListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**o_auth_id** | **str** |  | [optional] 
**dc** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.mailchimp_controller_action_list_request import MailchimpControllerActionListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MailchimpControllerActionListRequest from a JSON string
mailchimp_controller_action_list_request_instance = MailchimpControllerActionListRequest.from_json(json)
# print the JSON string representation of the object
print(MailchimpControllerActionListRequest.to_json())

# convert the object into a dict
mailchimp_controller_action_list_request_dict = mailchimp_controller_action_list_request_instance.to_dict()
# create an instance of MailchimpControllerActionListRequest from a dict
mailchimp_controller_action_list_request_from_dict = MailchimpControllerActionListRequest.from_dict(mailchimp_controller_action_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


