# GoogleDisplayVideoCustomUserAuth


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
from openapi_client.models.google_display_video_custom_user_auth import GoogleDisplayVideoCustomUserAuth

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleDisplayVideoCustomUserAuth from a JSON string
google_display_video_custom_user_auth_instance = GoogleDisplayVideoCustomUserAuth.from_json(json)
# print the JSON string representation of the object
print(GoogleDisplayVideoCustomUserAuth.to_json())

# convert the object into a dict
google_display_video_custom_user_auth_dict = google_display_video_custom_user_auth_instance.to_dict()
# create an instance of GoogleDisplayVideoCustomUserAuth from a dict
google_display_video_custom_user_auth_from_dict = GoogleDisplayVideoCustomUserAuth.from_dict(google_display_video_custom_user_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


