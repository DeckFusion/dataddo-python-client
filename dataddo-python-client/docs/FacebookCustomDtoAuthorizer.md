# FacebookCustomDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.facebook_custom_dto_authorizer import FacebookCustomDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of FacebookCustomDtoAuthorizer from a JSON string
facebook_custom_dto_authorizer_instance = FacebookCustomDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(FacebookCustomDtoAuthorizer.to_json())

# convert the object into a dict
facebook_custom_dto_authorizer_dict = facebook_custom_dto_authorizer_instance.to_dict()
# create an instance of FacebookCustomDtoAuthorizer from a dict
facebook_custom_dto_authorizer_from_dict = FacebookCustomDtoAuthorizer.from_dict(facebook_custom_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


