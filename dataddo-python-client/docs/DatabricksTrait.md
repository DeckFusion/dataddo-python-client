# DatabricksTrait


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalog** | **str** |  | [optional] 
**database** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.databricks_trait import DatabricksTrait

# TODO update the JSON string below
json = "{}"
# create an instance of DatabricksTrait from a JSON string
databricks_trait_instance = DatabricksTrait.from_json(json)
# print the JSON string representation of the object
print(DatabricksTrait.to_json())

# convert the object into a dict
databricks_trait_dict = databricks_trait_instance.to_dict()
# create an instance of DatabricksTrait from a dict
databricks_trait_from_dict = DatabricksTrait.from_dict(databricks_trait_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


