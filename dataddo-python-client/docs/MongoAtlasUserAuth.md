# MongoAtlasUserAuth


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
from openapi_client.models.mongo_atlas_user_auth import MongoAtlasUserAuth

# TODO update the JSON string below
json = "{}"
# create an instance of MongoAtlasUserAuth from a JSON string
mongo_atlas_user_auth_instance = MongoAtlasUserAuth.from_json(json)
# print the JSON string representation of the object
print(MongoAtlasUserAuth.to_json())

# convert the object into a dict
mongo_atlas_user_auth_dict = mongo_atlas_user_auth_instance.to_dict()
# create an instance of MongoAtlasUserAuth from a dict
mongo_atlas_user_auth_from_dict = MongoAtlasUserAuth.from_dict(mongo_atlas_user_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


