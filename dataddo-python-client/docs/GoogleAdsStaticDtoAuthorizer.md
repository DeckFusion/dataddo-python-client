# GoogleAdsStaticDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**static_key** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 
**developer_token** | **str** |  | [optional] 
**client_customer_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.google_ads_static_dto_authorizer import GoogleAdsStaticDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAdsStaticDtoAuthorizer from a JSON string
google_ads_static_dto_authorizer_instance = GoogleAdsStaticDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(GoogleAdsStaticDtoAuthorizer.to_json())

# convert the object into a dict
google_ads_static_dto_authorizer_dict = google_ads_static_dto_authorizer_instance.to_dict()
# create an instance of GoogleAdsStaticDtoAuthorizer from a dict
google_ads_static_dto_authorizer_from_dict = GoogleAdsStaticDtoAuthorizer.from_dict(google_ads_static_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


