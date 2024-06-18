# OneDriveDestination


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
**path** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 
**drive_id** | **str** |  | [optional] 
**tenant** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.one_drive_destination import OneDriveDestination

# TODO update the JSON string below
json = "{}"
# create an instance of OneDriveDestination from a JSON string
one_drive_destination_instance = OneDriveDestination.from_json(json)
# print the JSON string representation of the object
print(OneDriveDestination.to_json())

# convert the object into a dict
one_drive_destination_dict = one_drive_destination_instance.to_dict()
# create an instance of OneDriveDestination from a dict
one_drive_destination_from_dict = OneDriveDestination.from_dict(one_drive_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


