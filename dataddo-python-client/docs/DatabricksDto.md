# DatabricksDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**storage_strategy** | **str** |  | [optional] [default to 'incremental']
**allow_empty** | **bool** |  | [optional] [default to False]
**o_auth_id** | **int** |  | [optional] 
**statement** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.databricks_dto import DatabricksDto

# TODO update the JSON string below
json = "{}"
# create an instance of DatabricksDto from a JSON string
databricks_dto_instance = DatabricksDto.from_json(json)
# print the JSON string representation of the object
print(DatabricksDto.to_json())

# convert the object into a dict
databricks_dto_dict = databricks_dto_instance.to_dict()
# create an instance of DatabricksDto from a dict
databricks_dto_from_dict = DatabricksDto.from_dict(databricks_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


