# MysqlBinlogDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**storage_strategy** | **str** |  | [optional] [default to 'incremental']
**allow_empty** | **bool** |  | [optional] [default to False]
**o_auth_id** | **int** |  | [optional] 
**table** | **str** |  | [optional] 
**log_start_time** | **str** |  | [optional] 
**statement** | **str** |  | [optional] 
**default_int** | **int** |  | [optional] 
**default_float** | **int** |  | [optional] 
**default_string** | **str** |  | [optional] 
**default_date** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.mysql_binlog_dto import MysqlBinlogDto

# TODO update the JSON string below
json = "{}"
# create an instance of MysqlBinlogDto from a JSON string
mysql_binlog_dto_instance = MysqlBinlogDto.from_json(json)
# print the JSON string representation of the object
print(MysqlBinlogDto.to_json())

# convert the object into a dict
mysql_binlog_dto_dict = mysql_binlog_dto_instance.to_dict()
# create an instance of MysqlBinlogDto from a dict
mysql_binlog_dto_from_dict = MysqlBinlogDto.from_dict(mysql_binlog_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


