# VerticaDestination


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
from openapi_client.models.vertica_destination import VerticaDestination

# TODO update the JSON string below
json = "{}"
# create an instance of VerticaDestination from a JSON string
vertica_destination_instance = VerticaDestination.from_json(json)
# print the JSON string representation of the object
print(VerticaDestination.to_json())

# convert the object into a dict
vertica_destination_dict = vertica_destination_instance.to_dict()
# create an instance of VerticaDestination from a dict
vertica_destination_from_dict = VerticaDestination.from_dict(vertica_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


