# SnapchatStaticDtoAuthorizer


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
from openapi_client.models.snapchat_static_dto_authorizer import SnapchatStaticDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of SnapchatStaticDtoAuthorizer from a JSON string
snapchat_static_dto_authorizer_instance = SnapchatStaticDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(SnapchatStaticDtoAuthorizer.to_json())

# convert the object into a dict
snapchat_static_dto_authorizer_dict = snapchat_static_dto_authorizer_instance.to_dict()
# create an instance of SnapchatStaticDtoAuthorizer from a dict
snapchat_static_dto_authorizer_from_dict = SnapchatStaticDtoAuthorizer.from_dict(snapchat_static_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


