# AwsMariadbUserAuth


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
**username** | **str** |  | [optional] 
**database** | **str** |  | [optional] 
**ssh_config** | [**AwsAuroraTraitSshConfig**](AwsAuroraTraitSshConfig.md) |  | [optional] 
**ssl** | **str** |  | [optional] 
**tls** | **str** |  | [optional] 
**extra_params** | **Dict[str, str]** | string&gt; | [optional] 

## Example

```python
from openapi_client.models.aws_mariadb_user_auth import AwsMariadbUserAuth

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMariadbUserAuth from a JSON string
aws_mariadb_user_auth_instance = AwsMariadbUserAuth.from_json(json)
# print the JSON string representation of the object
print(AwsMariadbUserAuth.to_json())

# convert the object into a dict
aws_mariadb_user_auth_dict = aws_mariadb_user_auth_instance.to_dict()
# create an instance of AwsMariadbUserAuth from a dict
aws_mariadb_user_auth_from_dict = AwsMariadbUserAuth.from_dict(aws_mariadb_user_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


