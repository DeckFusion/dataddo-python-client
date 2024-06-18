# AuthMFARequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.auth_mfa_request import AuthMFARequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthMFARequest from a JSON string
auth_mfa_request_instance = AuthMFARequest.from_json(json)
# print the JSON string representation of the object
print(AuthMFARequest.to_json())

# convert the object into a dict
auth_mfa_request_dict = auth_mfa_request_instance.to_dict()
# create an instance of AuthMFARequest from a dict
auth_mfa_request_from_dict = AuthMFARequest.from_dict(auth_mfa_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


