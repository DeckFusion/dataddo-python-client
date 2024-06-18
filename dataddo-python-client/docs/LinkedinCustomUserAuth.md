# LinkedinCustomUserAuth


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
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.linkedin_custom_user_auth import LinkedinCustomUserAuth

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedinCustomUserAuth from a JSON string
linkedin_custom_user_auth_instance = LinkedinCustomUserAuth.from_json(json)
# print the JSON string representation of the object
print(LinkedinCustomUserAuth.to_json())

# convert the object into a dict
linkedin_custom_user_auth_dict = linkedin_custom_user_auth_instance.to_dict()
# create an instance of LinkedinCustomUserAuth from a dict
linkedin_custom_user_auth_from_dict = LinkedinCustomUserAuth.from_dict(linkedin_custom_user_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

