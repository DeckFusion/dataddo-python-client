# AwsPgsqlUserAuth


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
from openapi_client.models.aws_pgsql_user_auth import AwsPgsqlUserAuth

# TODO update the JSON string below
json = "{}"
# create an instance of AwsPgsqlUserAuth from a JSON string
aws_pgsql_user_auth_instance = AwsPgsqlUserAuth.from_json(json)
# print the JSON string representation of the object
print(AwsPgsqlUserAuth.to_json())

# convert the object into a dict
aws_pgsql_user_auth_dict = aws_pgsql_user_auth_instance.to_dict()
# create an instance of AwsPgsqlUserAuth from a dict
aws_pgsql_user_auth_from_dict = AwsPgsqlUserAuth.from_dict(aws_pgsql_user_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


