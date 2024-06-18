# DatabricksStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.databricks_storage_request import DatabricksStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DatabricksStorageRequest from a JSON string
databricks_storage_request_instance = DatabricksStorageRequest.from_json(json)
# print the JSON string representation of the object
print(DatabricksStorageRequest.to_json())

# convert the object into a dict
databricks_storage_request_dict = databricks_storage_request_instance.to_dict()
# create an instance of DatabricksStorageRequest from a dict
databricks_storage_request_from_dict = DatabricksStorageRequest.from_dict(databricks_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


