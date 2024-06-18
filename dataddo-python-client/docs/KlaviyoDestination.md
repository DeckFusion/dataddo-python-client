# KlaviyoDestination


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
**object** | **str** |  | [optional] 
**object_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.klaviyo_destination import KlaviyoDestination

# TODO update the JSON string below
json = "{}"
# create an instance of KlaviyoDestination from a JSON string
klaviyo_destination_instance = KlaviyoDestination.from_json(json)
# print the JSON string representation of the object
print(KlaviyoDestination.to_json())

# convert the object into a dict
klaviyo_destination_dict = klaviyo_destination_instance.to_dict()
# create an instance of KlaviyoDestination from a dict
klaviyo_destination_from_dict = KlaviyoDestination.from_dict(klaviyo_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


