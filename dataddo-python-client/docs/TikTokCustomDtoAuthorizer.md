# TikTokCustomDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tik_tok_custom_dto_authorizer import TikTokCustomDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of TikTokCustomDtoAuthorizer from a JSON string
tik_tok_custom_dto_authorizer_instance = TikTokCustomDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(TikTokCustomDtoAuthorizer.to_json())

# convert the object into a dict
tik_tok_custom_dto_authorizer_dict = tik_tok_custom_dto_authorizer_instance.to_dict()
# create an instance of TikTokCustomDtoAuthorizer from a dict
tik_tok_custom_dto_authorizer_from_dict = TikTokCustomDtoAuthorizer.from_dict(tik_tok_custom_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

