# SnapchatCustomDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.snapchat_custom_dto_authorizer import SnapchatCustomDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of SnapchatCustomDtoAuthorizer from a JSON string
snapchat_custom_dto_authorizer_instance = SnapchatCustomDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(SnapchatCustomDtoAuthorizer.to_json())

# convert the object into a dict
snapchat_custom_dto_authorizer_dict = snapchat_custom_dto_authorizer_instance.to_dict()
# create an instance of SnapchatCustomDtoAuthorizer from a dict
snapchat_custom_dto_authorizer_from_dict = SnapchatCustomDtoAuthorizer.from_dict(snapchat_custom_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


