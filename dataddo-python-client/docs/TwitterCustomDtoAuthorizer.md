# TwitterCustomDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.twitter_custom_dto_authorizer import TwitterCustomDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of TwitterCustomDtoAuthorizer from a JSON string
twitter_custom_dto_authorizer_instance = TwitterCustomDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(TwitterCustomDtoAuthorizer.to_json())

# convert the object into a dict
twitter_custom_dto_authorizer_dict = twitter_custom_dto_authorizer_instance.to_dict()
# create an instance of TwitterCustomDtoAuthorizer from a dict
twitter_custom_dto_authorizer_from_dict = TwitterCustomDtoAuthorizer.from_dict(twitter_custom_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


