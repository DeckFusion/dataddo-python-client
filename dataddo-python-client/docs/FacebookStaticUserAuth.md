# FacebookStaticUserAuth


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
**static_key** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.facebook_static_user_auth import FacebookStaticUserAuth

# TODO update the JSON string below
json = "{}"
# create an instance of FacebookStaticUserAuth from a JSON string
facebook_static_user_auth_instance = FacebookStaticUserAuth.from_json(json)
# print the JSON string representation of the object
print(FacebookStaticUserAuth.to_json())

# convert the object into a dict
facebook_static_user_auth_dict = facebook_static_user_auth_instance.to_dict()
# create an instance of FacebookStaticUserAuth from a dict
facebook_static_user_auth_from_dict = FacebookStaticUserAuth.from_dict(facebook_static_user_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


