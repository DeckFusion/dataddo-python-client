# TrinoTrait


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**user** | **str** |  | [optional] 
**var_schema** | **str** |  | [optional] 
**catalog** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.trino_trait import TrinoTrait

# TODO update the JSON string below
json = "{}"
# create an instance of TrinoTrait from a JSON string
trino_trait_instance = TrinoTrait.from_json(json)
# print the JSON string representation of the object
print(TrinoTrait.to_json())

# convert the object into a dict
trino_trait_dict = trino_trait_instance.to_dict()
# create an instance of TrinoTrait from a dict
trino_trait_from_dict = TrinoTrait.from_dict(trino_trait_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


