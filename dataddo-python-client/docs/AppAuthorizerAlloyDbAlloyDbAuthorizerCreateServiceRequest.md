# AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'alloy_db']
**data** | [**AlloyDbDtoAuthorizer**](AlloyDbDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_alloy_db_alloy_db_authorizer_create_service_request import AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest from a JSON string
app_authorizer_alloy_db_alloy_db_authorizer_create_service_request_instance = AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest.to_json())

# convert the object into a dict
app_authorizer_alloy_db_alloy_db_authorizer_create_service_request_dict = app_authorizer_alloy_db_alloy_db_authorizer_create_service_request_instance.to_dict()
# create an instance of AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest from a dict
app_authorizer_alloy_db_alloy_db_authorizer_create_service_request_from_dict = AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest.from_dict(app_authorizer_alloy_db_alloy_db_authorizer_create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


