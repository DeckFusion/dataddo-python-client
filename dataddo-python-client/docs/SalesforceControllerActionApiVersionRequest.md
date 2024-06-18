# SalesforceControllerActionApiVersionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**o_auth_id** | **str** |  | [optional] 
**instance** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.salesforce_controller_action_api_version_request import SalesforceControllerActionApiVersionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SalesforceControllerActionApiVersionRequest from a JSON string
salesforce_controller_action_api_version_request_instance = SalesforceControllerActionApiVersionRequest.from_json(json)
# print the JSON string representation of the object
print(SalesforceControllerActionApiVersionRequest.to_json())

# convert the object into a dict
salesforce_controller_action_api_version_request_dict = salesforce_controller_action_api_version_request_instance.to_dict()
# create an instance of SalesforceControllerActionApiVersionRequest from a dict
salesforce_controller_action_api_version_request_from_dict = SalesforceControllerActionApiVersionRequest.from_dict(salesforce_controller_action_api_version_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


