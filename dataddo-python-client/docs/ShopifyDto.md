# ShopifyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**storage_strategy** | **str** |  | [optional] [default to 'incremental']
**allow_empty** | **bool** |  | [optional] [default to False]
**request** | [**HttpConnectorDtoRequest**](HttpConnectorDtoRequest.md) |  | [optional] 
**o_auth_id** | **int** |  | [optional] 
**shop** | **str** |  | [optional] 
**attributes** | **List[object]** |  | [optional] 

## Example

```python
from openapi_client.models.shopify_dto import ShopifyDto

# TODO update the JSON string below
json = "{}"
# create an instance of ShopifyDto from a JSON string
shopify_dto_instance = ShopifyDto.from_json(json)
# print the JSON string representation of the object
print(ShopifyDto.to_json())

# convert the object into a dict
shopify_dto_dict = shopify_dto_instance.to_dict()
# create an instance of ShopifyDto from a dict
shopify_dto_from_dict = ShopifyDto.from_dict(shopify_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


