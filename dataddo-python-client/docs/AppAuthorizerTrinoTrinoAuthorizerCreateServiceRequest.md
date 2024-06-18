# AppAuthorizerTrinoTrinoAuthorizerCreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'trino']
**data** | [**TrinoDtoAuthorizer**](TrinoDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_trino_trino_authorizer_create_service_request import AppAuthorizerTrinoTrinoAuthorizerCreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerTrinoTrinoAuthorizerCreateServiceRequest from a JSON string
app_authorizer_trino_trino_authorizer_create_service_request_instance = AppAuthorizerTrinoTrinoAuthorizerCreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerTrinoTrinoAuthorizerCreateServiceRequest.to_json())

# convert the object into a dict
app_authorizer_trino_trino_authorizer_create_service_request_dict = app_authorizer_trino_trino_authorizer_create_service_request_instance.to_dict()
# create an instance of AppAuthorizerTrinoTrinoAuthorizerCreateServiceRequest from a dict
app_authorizer_trino_trino_authorizer_create_service_request_from_dict = AppAuthorizerTrinoTrinoAuthorizerCreateServiceRequest.from_dict(app_authorizer_trino_trino_authorizer_create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


