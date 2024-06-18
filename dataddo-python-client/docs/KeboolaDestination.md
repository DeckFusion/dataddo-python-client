# KeboolaDestination


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
from openapi_client.models.keboola_destination import KeboolaDestination

# TODO update the JSON string below
json = "{}"
# create an instance of KeboolaDestination from a JSON string
keboola_destination_instance = KeboolaDestination.from_json(json)
# print the JSON string representation of the object
print(KeboolaDestination.to_json())

# convert the object into a dict
keboola_destination_dict = keboola_destination_instance.to_dict()
# create an instance of KeboolaDestination from a dict
keboola_destination_from_dict = KeboolaDestination.from_dict(keboola_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


