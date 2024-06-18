# RedshiftDestination


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
from openapi_client.models.redshift_destination import RedshiftDestination

# TODO update the JSON string below
json = "{}"
# create an instance of RedshiftDestination from a JSON string
redshift_destination_instance = RedshiftDestination.from_json(json)
# print the JSON string representation of the object
print(RedshiftDestination.to_json())

# convert the object into a dict
redshift_destination_dict = redshift_destination_instance.to_dict()
# create an instance of RedshiftDestination from a dict
redshift_destination_from_dict = RedshiftDestination.from_dict(redshift_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


