# MongoUserAuth


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
**dsn** | **str** |  | [optional] 
**database** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.mongo_user_auth import MongoUserAuth

# TODO update the JSON string below
json = "{}"
# create an instance of MongoUserAuth from a JSON string
mongo_user_auth_instance = MongoUserAuth.from_json(json)
# print the JSON string representation of the object
print(MongoUserAuth.to_json())

# convert the object into a dict
mongo_user_auth_dict = mongo_user_auth_instance.to_dict()
# create an instance of MongoUserAuth from a dict
mongo_user_auth_from_dict = MongoUserAuth.from_dict(mongo_user_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


