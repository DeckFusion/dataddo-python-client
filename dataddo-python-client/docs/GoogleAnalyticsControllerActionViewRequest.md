# GoogleAnalyticsControllerActionViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**o_auth_id** | **str** |  | [optional] 
**account_id** | **int** |  | [optional] 
**property_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.google_analytics_controller_action_view_request import GoogleAnalyticsControllerActionViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAnalyticsControllerActionViewRequest from a JSON string
google_analytics_controller_action_view_request_instance = GoogleAnalyticsControllerActionViewRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleAnalyticsControllerActionViewRequest.to_json())

# convert the object into a dict
google_analytics_controller_action_view_request_dict = google_analytics_controller_action_view_request_instance.to_dict()
# create an instance of GoogleAnalyticsControllerActionViewRequest from a dict
google_analytics_controller_action_view_request_from_dict = GoogleAnalyticsControllerActionViewRequest.from_dict(google_analytics_controller_action_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


