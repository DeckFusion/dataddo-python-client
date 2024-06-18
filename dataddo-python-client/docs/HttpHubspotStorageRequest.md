# HttpHubspotStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 
**api_object** | **str** |  | [optional] 
**api_object_custom_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.http_hubspot_storage_request import HttpHubspotStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HttpHubspotStorageRequest from a JSON string
http_hubspot_storage_request_instance = HttpHubspotStorageRequest.from_json(json)
# print the JSON string representation of the object
print(HttpHubspotStorageRequest.to_json())

# convert the object into a dict
http_hubspot_storage_request_dict = http_hubspot_storage_request_instance.to_dict()
# create an instance of HttpHubspotStorageRequest from a dict
http_hubspot_storage_request_from_dict = HttpHubspotStorageRequest.from_dict(http_hubspot_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


