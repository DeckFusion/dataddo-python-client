# CoreWebVitalsUserAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**object_id** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**status_detail** | **str** |  | [optional] 
**service_type** | **str** |  | [optional] 
**last_use** | **datetime** |  | [optional] 
**identifier** | **str** |  | [optional] 
**hash** | **str** |  | [optional] 
**static_key** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.core_web_vitals_user_auth import CoreWebVitalsUserAuth

# TODO update the JSON string below
json = "{}"
# create an instance of CoreWebVitalsUserAuth from a JSON string
core_web_vitals_user_auth_instance = CoreWebVitalsUserAuth.from_json(json)
# print the JSON string representation of the object
print(CoreWebVitalsUserAuth.to_json())

# convert the object into a dict
core_web_vitals_user_auth_dict = core_web_vitals_user_auth_instance.to_dict()
# create an instance of CoreWebVitalsUserAuth from a dict
core_web_vitals_user_auth_from_dict = CoreWebVitalsUserAuth.from_dict(core_web_vitals_user_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


