# GoogleAnalytics4ControllerActionPropertyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**o_auth_id** | **str** |  | [optional] 
**account_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.google_analytics4_controller_action_property_request import GoogleAnalytics4ControllerActionPropertyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleAnalytics4ControllerActionPropertyRequest from a JSON string
google_analytics4_controller_action_property_request_instance = GoogleAnalytics4ControllerActionPropertyRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleAnalytics4ControllerActionPropertyRequest.to_json())

# convert the object into a dict
google_analytics4_controller_action_property_request_dict = google_analytics4_controller_action_property_request_instance.to_dict()
# create an instance of GoogleAnalytics4ControllerActionPropertyRequest from a dict
google_analytics4_controller_action_property_request_from_dict = GoogleAnalytics4ControllerActionPropertyRequest.from_dict(google_analytics4_controller_action_property_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


