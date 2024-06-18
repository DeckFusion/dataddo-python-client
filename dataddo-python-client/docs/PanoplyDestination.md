# PanoplyDestination


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
**project_id** | **str** |  | [optional] 
**dataset_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.panoply_destination import PanoplyDestination

# TODO update the JSON string below
json = "{}"
# create an instance of PanoplyDestination from a JSON string
panoply_destination_instance = PanoplyDestination.from_json(json)
# print the JSON string representation of the object
print(PanoplyDestination.to_json())

# convert the object into a dict
panoply_destination_dict = panoply_destination_instance.to_dict()
# create an instance of PanoplyDestination from a dict
panoply_destination_from_dict = PanoplyDestination.from_dict(panoply_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


