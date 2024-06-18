# KeboolaStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.keboola_storage_request import KeboolaStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KeboolaStorageRequest from a JSON string
keboola_storage_request_instance = KeboolaStorageRequest.from_json(json)
# print the JSON string representation of the object
print(KeboolaStorageRequest.to_json())

# convert the object into a dict
keboola_storage_request_dict = keboola_storage_request_instance.to_dict()
# create an instance of KeboolaStorageRequest from a dict
keboola_storage_request_from_dict = KeboolaStorageRequest.from_dict(keboola_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


