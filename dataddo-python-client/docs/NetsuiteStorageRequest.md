# NetsuiteStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 
**endpoint** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.netsuite_storage_request import NetsuiteStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NetsuiteStorageRequest from a JSON string
netsuite_storage_request_instance = NetsuiteStorageRequest.from_json(json)
# print the JSON string representation of the object
print(NetsuiteStorageRequest.to_json())

# convert the object into a dict
netsuite_storage_request_dict = netsuite_storage_request_instance.to_dict()
# create an instance of NetsuiteStorageRequest from a dict
netsuite_storage_request_from_dict = NetsuiteStorageRequest.from_dict(netsuite_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


