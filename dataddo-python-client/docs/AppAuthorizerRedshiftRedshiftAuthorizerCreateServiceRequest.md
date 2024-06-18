# AppAuthorizerRedshiftRedshiftAuthorizerCreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'redshift']
**data** | [**RedshiftDtoAuthorizer**](RedshiftDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_redshift_redshift_authorizer_create_service_request import AppAuthorizerRedshiftRedshiftAuthorizerCreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerRedshiftRedshiftAuthorizerCreateServiceRequest from a JSON string
app_authorizer_redshift_redshift_authorizer_create_service_request_instance = AppAuthorizerRedshiftRedshiftAuthorizerCreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerRedshiftRedshiftAuthorizerCreateServiceRequest.to_json())

# convert the object into a dict
app_authorizer_redshift_redshift_authorizer_create_service_request_dict = app_authorizer_redshift_redshift_authorizer_create_service_request_instance.to_dict()
# create an instance of AppAuthorizerRedshiftRedshiftAuthorizerCreateServiceRequest from a dict
app_authorizer_redshift_redshift_authorizer_create_service_request_from_dict = AppAuthorizerRedshiftRedshiftAuthorizerCreateServiceRequest.from_dict(app_authorizer_redshift_redshift_authorizer_create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


