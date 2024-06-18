# HubspotCustomDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.hubspot_custom_dto_authorizer import HubspotCustomDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of HubspotCustomDtoAuthorizer from a JSON string
hubspot_custom_dto_authorizer_instance = HubspotCustomDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(HubspotCustomDtoAuthorizer.to_json())

# convert the object into a dict
hubspot_custom_dto_authorizer_dict = hubspot_custom_dto_authorizer_instance.to_dict()
# create an instance of HubspotCustomDtoAuthorizer from a dict
hubspot_custom_dto_authorizer_from_dict = HubspotCustomDtoAuthorizer.from_dict(hubspot_custom_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


