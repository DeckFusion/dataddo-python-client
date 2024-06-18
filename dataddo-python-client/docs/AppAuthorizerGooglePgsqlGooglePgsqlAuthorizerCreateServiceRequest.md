# AppAuthorizerGooglePgsqlGooglePgsqlAuthorizerCreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'google_pgsql']
**data** | [**GooglePgsqlDtoAuthorizer**](GooglePgsqlDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_google_pgsql_google_pgsql_authorizer_create_service_request import AppAuthorizerGooglePgsqlGooglePgsqlAuthorizerCreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerGooglePgsqlGooglePgsqlAuthorizerCreateServiceRequest from a JSON string
app_authorizer_google_pgsql_google_pgsql_authorizer_create_service_request_instance = AppAuthorizerGooglePgsqlGooglePgsqlAuthorizerCreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerGooglePgsqlGooglePgsqlAuthorizerCreateServiceRequest.to_json())

# convert the object into a dict
app_authorizer_google_pgsql_google_pgsql_authorizer_create_service_request_dict = app_authorizer_google_pgsql_google_pgsql_authorizer_create_service_request_instance.to_dict()
# create an instance of AppAuthorizerGooglePgsqlGooglePgsqlAuthorizerCreateServiceRequest from a dict
app_authorizer_google_pgsql_google_pgsql_authorizer_create_service_request_from_dict = AppAuthorizerGooglePgsqlGooglePgsqlAuthorizerCreateServiceRequest.from_dict(app_authorizer_google_pgsql_google_pgsql_authorizer_create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


