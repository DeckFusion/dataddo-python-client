# LinkedinStaticDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**static_key** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.linkedin_static_dto_authorizer import LinkedinStaticDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedinStaticDtoAuthorizer from a JSON string
linkedin_static_dto_authorizer_instance = LinkedinStaticDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(LinkedinStaticDtoAuthorizer.to_json())

# convert the object into a dict
linkedin_static_dto_authorizer_dict = linkedin_static_dto_authorizer_instance.to_dict()
# create an instance of LinkedinStaticDtoAuthorizer from a dict
linkedin_static_dto_authorizer_from_dict = LinkedinStaticDtoAuthorizer.from_dict(linkedin_static_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


