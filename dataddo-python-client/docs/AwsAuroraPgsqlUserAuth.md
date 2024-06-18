# AwsAuroraPgsqlUserAuth


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
from openapi_client.models.aws_aurora_pgsql_user_auth import AwsAuroraPgsqlUserAuth

# TODO update the JSON string below
json = "{}"
# create an instance of AwsAuroraPgsqlUserAuth from a JSON string
aws_aurora_pgsql_user_auth_instance = AwsAuroraPgsqlUserAuth.from_json(json)
# print the JSON string representation of the object
print(AwsAuroraPgsqlUserAuth.to_json())

# convert the object into a dict
aws_aurora_pgsql_user_auth_dict = aws_aurora_pgsql_user_auth_instance.to_dict()
# create an instance of AwsAuroraPgsqlUserAuth from a dict
aws_aurora_pgsql_user_auth_from_dict = AwsAuroraPgsqlUserAuth.from_dict(aws_aurora_pgsql_user_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


