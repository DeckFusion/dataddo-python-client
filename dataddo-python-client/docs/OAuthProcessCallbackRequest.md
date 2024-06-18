# OAuthProcessCallbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.o_auth_process_callback_request import OAuthProcessCallbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthProcessCallbackRequest from a JSON string
o_auth_process_callback_request_instance = OAuthProcessCallbackRequest.from_json(json)
# print the JSON string representation of the object
print(OAuthProcessCallbackRequest.to_json())

# convert the object into a dict
o_auth_process_callback_request_dict = o_auth_process_callback_request_instance.to_dict()
# create an instance of OAuthProcessCallbackRequest from a dict
o_auth_process_callback_request_from_dict = OAuthProcessCallbackRequest.from_dict(o_auth_process_callback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


