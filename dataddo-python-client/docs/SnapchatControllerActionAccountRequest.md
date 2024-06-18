# SnapchatControllerActionAccountRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**o_auth_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.snapchat_controller_action_account_request import SnapchatControllerActionAccountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SnapchatControllerActionAccountRequest from a JSON string
snapchat_controller_action_account_request_instance = SnapchatControllerActionAccountRequest.from_json(json)
# print the JSON string representation of the object
print(SnapchatControllerActionAccountRequest.to_json())

# convert the object into a dict
snapchat_controller_action_account_request_dict = snapchat_controller_action_account_request_instance.to_dict()
# create an instance of SnapchatControllerActionAccountRequest from a dict
snapchat_controller_action_account_request_from_dict = SnapchatControllerActionAccountRequest.from_dict(snapchat_controller_action_account_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


