# VerticaStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.vertica_storage_request import VerticaStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerticaStorageRequest from a JSON string
vertica_storage_request_instance = VerticaStorageRequest.from_json(json)
# print the JSON string representation of the object
print(VerticaStorageRequest.to_json())

# convert the object into a dict
vertica_storage_request_dict = vertica_storage_request_instance.to_dict()
# create an instance of VerticaStorageRequest from a dict
vertica_storage_request_from_dict = VerticaStorageRequest.from_dict(vertica_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


