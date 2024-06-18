# AwsSqlServerDestination


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
from openapi_client.models.aws_sql_server_destination import AwsSqlServerDestination

# TODO update the JSON string below
json = "{}"
# create an instance of AwsSqlServerDestination from a JSON string
aws_sql_server_destination_instance = AwsSqlServerDestination.from_json(json)
# print the JSON string representation of the object
print(AwsSqlServerDestination.to_json())

# convert the object into a dict
aws_sql_server_destination_dict = aws_sql_server_destination_instance.to_dict()
# create an instance of AwsSqlServerDestination from a dict
aws_sql_server_destination_from_dict = AwsSqlServerDestination.from_dict(aws_sql_server_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


