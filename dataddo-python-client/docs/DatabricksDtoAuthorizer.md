# DatabricksDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog** | **str** |  | [optional] 
**database** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**dsn** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.databricks_dto_authorizer import DatabricksDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of DatabricksDtoAuthorizer from a JSON string
databricks_dto_authorizer_instance = DatabricksDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(DatabricksDtoAuthorizer.to_json())

# convert the object into a dict
databricks_dto_authorizer_dict = databricks_dto_authorizer_instance.to_dict()
# create an instance of DatabricksDtoAuthorizer from a dict
databricks_dto_authorizer_from_dict = DatabricksDtoAuthorizer.from_dict(databricks_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


