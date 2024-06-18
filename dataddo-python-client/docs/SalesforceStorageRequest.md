# SalesforceStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 
**instance** | **str** |  | [optional] 
**api_version** | **str** |  | [optional] 
**object** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.salesforce_storage_request import SalesforceStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceStorageRequest from a JSON string
salesforce_storage_request_instance = SalesforceStorageRequest.from_json(json)
# print the JSON string representation of the object
print(SalesforceStorageRequest.to_json())

# convert the object into a dict
salesforce_storage_request_dict = salesforce_storage_request_instance.to_dict()
# create an instance of SalesforceStorageRequest from a dict
salesforce_storage_request_from_dict = SalesforceStorageRequest.from_dict(salesforce_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


