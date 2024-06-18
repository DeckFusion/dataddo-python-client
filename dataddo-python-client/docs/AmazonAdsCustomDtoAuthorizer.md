# AmazonAdsCustomDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.amazon_ads_custom_dto_authorizer import AmazonAdsCustomDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonAdsCustomDtoAuthorizer from a JSON string
amazon_ads_custom_dto_authorizer_instance = AmazonAdsCustomDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(AmazonAdsCustomDtoAuthorizer.to_json())

# convert the object into a dict
amazon_ads_custom_dto_authorizer_dict = amazon_ads_custom_dto_authorizer_instance.to_dict()
# create an instance of AmazonAdsCustomDtoAuthorizer from a dict
amazon_ads_custom_dto_authorizer_from_dict = AmazonAdsCustomDtoAuthorizer.from_dict(amazon_ads_custom_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


