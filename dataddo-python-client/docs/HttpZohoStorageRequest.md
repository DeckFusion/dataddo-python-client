# HttpZohoStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 
**module** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.http_zoho_storage_request import HttpZohoStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HttpZohoStorageRequest from a JSON string
http_zoho_storage_request_instance = HttpZohoStorageRequest.from_json(json)
# print the JSON string representation of the object
print(HttpZohoStorageRequest.to_json())

# convert the object into a dict
http_zoho_storage_request_dict = http_zoho_storage_request_instance.to_dict()
# create an instance of HttpZohoStorageRequest from a dict
http_zoho_storage_request_from_dict = HttpZohoStorageRequest.from_dict(http_zoho_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


