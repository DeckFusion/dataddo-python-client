# MssqlDestination


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
from openapi_client.models.mssql_destination import MssqlDestination

# TODO update the JSON string below
json = "{}"
# create an instance of MssqlDestination from a JSON string
mssql_destination_instance = MssqlDestination.from_json(json)
# print the JSON string representation of the object
print(MssqlDestination.to_json())

# convert the object into a dict
mssql_destination_dict = mssql_destination_instance.to_dict()
# create an instance of MssqlDestination from a dict
mssql_destination_from_dict = MssqlDestination.from_dict(mssql_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


