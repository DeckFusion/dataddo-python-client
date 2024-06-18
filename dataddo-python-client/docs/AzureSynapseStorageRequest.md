# AzureSynapseStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.azure_synapse_storage_request import AzureSynapseStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSynapseStorageRequest from a JSON string
azure_synapse_storage_request_instance = AzureSynapseStorageRequest.from_json(json)
# print the JSON string representation of the object
print(AzureSynapseStorageRequest.to_json())

# convert the object into a dict
azure_synapse_storage_request_dict = azure_synapse_storage_request_instance.to_dict()
# create an instance of AzureSynapseStorageRequest from a dict
azure_synapse_storage_request_from_dict = AzureSynapseStorageRequest.from_dict(azure_synapse_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


