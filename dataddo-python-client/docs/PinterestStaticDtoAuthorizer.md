# PinterestStaticDtoAuthorizer


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
from openapi_client.models.pinterest_static_dto_authorizer import PinterestStaticDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of PinterestStaticDtoAuthorizer from a JSON string
pinterest_static_dto_authorizer_instance = PinterestStaticDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(PinterestStaticDtoAuthorizer.to_json())

# convert the object into a dict
pinterest_static_dto_authorizer_dict = pinterest_static_dto_authorizer_instance.to_dict()
# create an instance of PinterestStaticDtoAuthorizer from a dict
pinterest_static_dto_authorizer_from_dict = PinterestStaticDtoAuthorizer.from_dict(pinterest_static_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


