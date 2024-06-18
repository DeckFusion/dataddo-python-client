# MssqlUserAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**object_id** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**status_detail** | **str** |  | [optional] 
**service_type** | **str** |  | [optional] 
**last_use** | **datetime** |  | [optional] 
**identifier** | **str** |  | [optional] 
**hash** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.mssql_user_auth import MssqlUserAuth

# TODO update the JSON string below
json = "{}"
# create an instance of MssqlUserAuth from a JSON string
mssql_user_auth_instance = MssqlUserAuth.from_json(json)
# print the JSON string representation of the object
print(MssqlUserAuth.to_json())

# convert the object into a dict
mssql_user_auth_dict = mssql_user_auth_instance.to_dict()
# create an instance of MssqlUserAuth from a dict
mssql_user_auth_from_dict = MssqlUserAuth.from_dict(mssql_user_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


