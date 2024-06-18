# AmazonSellingPartnerCustomDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **str** |  | [optional] 
**store_name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.amazon_selling_partner_custom_dto_authorizer import AmazonSellingPartnerCustomDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonSellingPartnerCustomDtoAuthorizer from a JSON string
amazon_selling_partner_custom_dto_authorizer_instance = AmazonSellingPartnerCustomDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(AmazonSellingPartnerCustomDtoAuthorizer.to_json())

# convert the object into a dict
amazon_selling_partner_custom_dto_authorizer_dict = amazon_selling_partner_custom_dto_authorizer_instance.to_dict()
# create an instance of AmazonSellingPartnerCustomDtoAuthorizer from a dict
amazon_selling_partner_custom_dto_authorizer_from_dict = AmazonSellingPartnerCustomDtoAuthorizer.from_dict(amazon_selling_partner_custom_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


