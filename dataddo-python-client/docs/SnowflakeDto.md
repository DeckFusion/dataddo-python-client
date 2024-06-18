# SnowflakeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**storage_strategy** | **str** |  | [optional] [default to 'incremental']
**allow_empty** | **bool** |  | [optional] [default to False]
**o_auth_id** | **int** |  | [optional] 
**statement** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.snowflake_dto import SnowflakeDto

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeDto from a JSON string
snowflake_dto_instance = SnowflakeDto.from_json(json)
# print the JSON string representation of the object
print(SnowflakeDto.to_json())

# convert the object into a dict
snowflake_dto_dict = snowflake_dto_instance.to_dict()
# create an instance of SnowflakeDto from a dict
snowflake_dto_from_dict = SnowflakeDto.from_dict(snowflake_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


