# AmazonDspDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**storage_strategy** | **str** |  | [optional] [default to 'incremental']
**allow_empty** | **bool** |  | [optional] [default to False]
**o_auth_id** | **int** |  | [optional] 
**date_range** | **str** |  | [optional] 
**profile_id** | **List[object]** |  | [optional] 
**metrics** | **List[object]** |  | [optional] 
**dimensions** | **List[object]** |  | [optional] 
**report_type** | **str** |  | [optional] 
**time_unit** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.amazon_dsp_dto import AmazonDspDto

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonDspDto from a JSON string
amazon_dsp_dto_instance = AmazonDspDto.from_json(json)
# print the JSON string representation of the object
print(AmazonDspDto.to_json())

# convert the object into a dict
amazon_dsp_dto_dict = amazon_dsp_dto_instance.to_dict()
# create an instance of AmazonDspDto from a dict
amazon_dsp_dto_from_dict = AmazonDspDto.from_dict(amazon_dsp_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


