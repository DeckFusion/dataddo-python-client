# TrinoUserAuth


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
**host** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**user** | **str** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**catalog** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.trino_user_auth import TrinoUserAuth

# TODO update the JSON string below
json = "{}"
# create an instance of TrinoUserAuth from a JSON string
trino_user_auth_instance = TrinoUserAuth.from_json(json)
# print the JSON string representation of the object
print(TrinoUserAuth.to_json())

# convert the object into a dict
trino_user_auth_dict = trino_user_auth_instance.to_dict()
# create an instance of TrinoUserAuth from a dict
trino_user_auth_from_dict = TrinoUserAuth.from_dict(trino_user_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


