# QuickbooksCustomDtoAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**tenant** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.quickbooks_custom_dto_authorizer import QuickbooksCustomDtoAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of QuickbooksCustomDtoAuthorizer from a JSON string
quickbooks_custom_dto_authorizer_instance = QuickbooksCustomDtoAuthorizer.from_json(json)
# print the JSON string representation of the object
print(QuickbooksCustomDtoAuthorizer.to_json())

# convert the object into a dict
quickbooks_custom_dto_authorizer_dict = quickbooks_custom_dto_authorizer_instance.to_dict()
# create an instance of QuickbooksCustomDtoAuthorizer from a dict
quickbooks_custom_dto_authorizer_from_dict = QuickbooksCustomDtoAuthorizer.from_dict(quickbooks_custom_dto_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


