# MysqlDto


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
**default_int** | **int** |  | [optional] 
**default_float** | **int** |  | [optional] 
**default_string** | **str** |  | [optional] 
**default_date** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.mysql_dto import MysqlDto

# TODO update the JSON string below
json = "{}"
# create an instance of MysqlDto from a JSON string
mysql_dto_instance = MysqlDto.from_json(json)
# print the JSON string representation of the object
print(MysqlDto.to_json())

# convert the object into a dict
mysql_dto_dict = mysql_dto_instance.to_dict()
# create an instance of MysqlDto from a dict
mysql_dto_from_dict = MysqlDto.from_dict(mysql_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


