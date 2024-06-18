# NetsuiteDestination


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
**endpoint** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.netsuite_destination import NetsuiteDestination

# TODO update the JSON string below
json = "{}"
# create an instance of NetsuiteDestination from a JSON string
netsuite_destination_instance = NetsuiteDestination.from_json(json)
# print the JSON string representation of the object
print(NetsuiteDestination.to_json())

# convert the object into a dict
netsuite_destination_dict = netsuite_destination_instance.to_dict()
# create an instance of NetsuiteDestination from a dict
netsuite_destination_from_dict = NetsuiteDestination.from_dict(netsuite_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


