# ActionAuthorizationResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**service** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.action_authorization_response_inner import ActionAuthorizationResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ActionAuthorizationResponseInner from a JSON string
action_authorization_response_inner_instance = ActionAuthorizationResponseInner.from_json(json)
# print the JSON string representation of the object
print(ActionAuthorizationResponseInner.to_json())

# convert the object into a dict
action_authorization_response_inner_dict = action_authorization_response_inner_instance.to_dict()
# create an instance of ActionAuthorizationResponseInner from a dict
action_authorization_response_inner_from_dict = ActionAuthorizationResponseInner.from_dict(action_authorization_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


