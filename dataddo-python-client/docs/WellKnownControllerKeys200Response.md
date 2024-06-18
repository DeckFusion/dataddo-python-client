# WellKnownControllerKeys200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[List[JWKSInner]]** |  | [optional] 

## Example

```python
from openapi_client.models.well_known_controller_keys200_response import WellKnownControllerKeys200Response

# TODO update the JSON string below
json = "{}"
# create an instance of WellKnownControllerKeys200Response from a JSON string
well_known_controller_keys200_response_instance = WellKnownControllerKeys200Response.from_json(json)
# print the JSON string representation of the object
print(WellKnownControllerKeys200Response.to_json())

# convert the object into a dict
well_known_controller_keys200_response_dict = well_known_controller_keys200_response_instance.to_dict()
# create an instance of WellKnownControllerKeys200Response from a dict
well_known_controller_keys200_response_from_dict = WellKnownControllerKeys200Response.from_dict(well_known_controller_keys200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


