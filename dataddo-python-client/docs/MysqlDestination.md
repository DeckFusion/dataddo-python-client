# MysqlDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**last_use** | **datetime** |  | [optional] 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**status_detail** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.mysql_destination import MysqlDestination

# TODO update the JSON string below
json = "{}"
# create an instance of MysqlDestination from a JSON string
mysql_destination_instance = MysqlDestination.from_json(json)
# print the JSON string representation of the object
print(MysqlDestination.to_json())

# convert the object into a dict
mysql_destination_dict = mysql_destination_instance.to_dict()
# create an instance of MysqlDestination from a dict
mysql_destination_from_dict = MysqlDestination.from_dict(mysql_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


