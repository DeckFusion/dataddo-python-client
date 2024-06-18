# AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'google_mysql']
**data** | [**GoogleMysqlDtoAuthorizer**](GoogleMysqlDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_google_mysql_google_mysql_authorizer_create_service_request import AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest from a JSON string
app_authorizer_google_mysql_google_mysql_authorizer_create_service_request_instance = AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest.to_json())

# convert the object into a dict
app_authorizer_google_mysql_google_mysql_authorizer_create_service_request_dict = app_authorizer_google_mysql_google_mysql_authorizer_create_service_request_instance.to_dict()
# create an instance of AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest from a dict
app_authorizer_google_mysql_google_mysql_authorizer_create_service_request_from_dict = AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest.from_dict(app_authorizer_google_mysql_google_mysql_authorizer_create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


