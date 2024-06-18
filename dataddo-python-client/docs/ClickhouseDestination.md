# ClickhouseDestination


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
from openapi_client.models.clickhouse_destination import ClickhouseDestination

# TODO update the JSON string below
json = "{}"
# create an instance of ClickhouseDestination from a JSON string
clickhouse_destination_instance = ClickhouseDestination.from_json(json)
# print the JSON string representation of the object
print(ClickhouseDestination.to_json())

# convert the object into a dict
clickhouse_destination_dict = clickhouse_destination_instance.to_dict()
# create an instance of ClickhouseDestination from a dict
clickhouse_destination_from_dict = ClickhouseDestination.from_dict(clickhouse_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


