# KlaviyoV3Dto


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
**date_range** | **str** |  | [optional] 
**campaign_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.klaviyo_v3_dto import KlaviyoV3Dto

# TODO update the JSON string below
json = "{}"
# create an instance of KlaviyoV3Dto from a JSON string
klaviyo_v3_dto_instance = KlaviyoV3Dto.from_json(json)
# print the JSON string representation of the object
print(KlaviyoV3Dto.to_json())

# convert the object into a dict
klaviyo_v3_dto_dict = klaviyo_v3_dto_instance.to_dict()
# create an instance of KlaviyoV3Dto from a dict
klaviyo_v3_dto_from_dict = KlaviyoV3Dto.from_dict(klaviyo_v3_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


