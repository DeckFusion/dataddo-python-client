# SecurityDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**provider** | **object** |  | [optional] 
**realm_id** | **int** |  | [optional] 
**expires_in** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.security_dto import SecurityDto

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityDto from a JSON string
security_dto_instance = SecurityDto.from_json(json)
# print the JSON string representation of the object
print(SecurityDto.to_json())

# convert the object into a dict
security_dto_dict = security_dto_instance.to_dict()
# create an instance of SecurityDto from a dict
security_dto_from_dict = SecurityDto.from_dict(security_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


