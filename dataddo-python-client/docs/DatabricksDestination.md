# DatabricksDestination


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
from openapi_client.models.databricks_destination import DatabricksDestination

# TODO update the JSON string below
json = "{}"
# create an instance of DatabricksDestination from a JSON string
databricks_destination_instance = DatabricksDestination.from_json(json)
# print the JSON string representation of the object
print(DatabricksDestination.to_json())

# convert the object into a dict
databricks_destination_dict = databricks_destination_instance.to_dict()
# create an instance of DatabricksDestination from a dict
databricks_destination_from_dict = DatabricksDestination.from_dict(databricks_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


