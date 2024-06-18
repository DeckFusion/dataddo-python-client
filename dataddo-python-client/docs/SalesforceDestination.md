# SalesforceDestination


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
**instance** | **str** |  | [optional] 
**api_version** | **str** |  | [optional] 
**object** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.salesforce_destination import SalesforceDestination

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceDestination from a JSON string
salesforce_destination_instance = SalesforceDestination.from_json(json)
# print the JSON string representation of the object
print(SalesforceDestination.to_json())

# convert the object into a dict
salesforce_destination_dict = salesforce_destination_instance.to_dict()
# create an instance of SalesforceDestination from a dict
salesforce_destination_from_dict = SalesforceDestination.from_dict(salesforce_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


