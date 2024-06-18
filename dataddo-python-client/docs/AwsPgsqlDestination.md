# AwsPgsqlDestination


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
from openapi_client.models.aws_pgsql_destination import AwsPgsqlDestination

# TODO update the JSON string below
json = "{}"
# create an instance of AwsPgsqlDestination from a JSON string
aws_pgsql_destination_instance = AwsPgsqlDestination.from_json(json)
# print the JSON string representation of the object
print(AwsPgsqlDestination.to_json())

# convert the object into a dict
aws_pgsql_destination_dict = aws_pgsql_destination_instance.to_dict()
# create an instance of AwsPgsqlDestination from a dict
aws_pgsql_destination_from_dict = AwsPgsqlDestination.from_dict(aws_pgsql_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


