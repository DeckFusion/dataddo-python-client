# ExactOnlineDestination


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
**division_id** | **str** |  | [optional] 
**endpoint** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.exact_online_destination import ExactOnlineDestination

# TODO update the JSON string below
json = "{}"
# create an instance of ExactOnlineDestination from a JSON string
exact_online_destination_instance = ExactOnlineDestination.from_json(json)
# print the JSON string representation of the object
print(ExactOnlineDestination.to_json())

# convert the object into a dict
exact_online_destination_dict = exact_online_destination_instance.to_dict()
# create an instance of ExactOnlineDestination from a dict
exact_online_destination_from_dict = ExactOnlineDestination.from_dict(exact_online_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


