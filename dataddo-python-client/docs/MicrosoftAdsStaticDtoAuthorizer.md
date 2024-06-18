# MicrosoftAdsStaticDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**static_key** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**developer_token** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 
**tenant** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.microsoft_ads_static_dto_authorizer import MicrosoftAdsStaticDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftAdsStaticDtoAuthorizer from a JSON string
microsoft_ads_static_dto_authorizer_instance = MicrosoftAdsStaticDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(MicrosoftAdsStaticDtoAuthorizer.to_json())

# convert the object into a dict
microsoft_ads_static_dto_authorizer_dict = microsoft_ads_static_dto_authorizer_instance.to_dict()
# create an instance of MicrosoftAdsStaticDtoAuthorizer from a dict
microsoft_ads_static_dto_authorizer_from_dict = MicrosoftAdsStaticDtoAuthorizer.from_dict(microsoft_ads_static_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


