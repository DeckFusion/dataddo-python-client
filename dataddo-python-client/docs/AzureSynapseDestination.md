# AzureSynapseDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**last_use** | **datetime** |  | [optional] 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**status_detail** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.azure_synapse_destination import AzureSynapseDestination

# TODO update the JSON string below
json = "{}"
# create an instance of AzureSynapseDestination from a JSON string
azure_synapse_destination_instance = AzureSynapseDestination.from_json(json)
# print the JSON string representation of the object
print(AzureSynapseDestination.to_json())

# convert the object into a dict
azure_synapse_destination_dict = azure_synapse_destination_instance.to_dict()
# create an instance of AzureSynapseDestination from a dict
azure_synapse_destination_from_dict = AzureSynapseDestination.from_dict(azure_synapse_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


