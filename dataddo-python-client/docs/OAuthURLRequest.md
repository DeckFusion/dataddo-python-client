# OAuthURLRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 
**config** | **object** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.o_auth_url_request import OAuthURLRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthURLRequest from a JSON string
o_auth_url_request_instance = OAuthURLRequest.from_json(json)
# print the JSON string representation of the object
print(OAuthURLRequest.to_json())

# convert the object into a dict
o_auth_url_request_dict = o_auth_url_request_instance.to_dict()
# create an instance of OAuthURLRequest from a dict
o_auth_url_request_from_dict = OAuthURLRequest.from_dict(o_auth_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


