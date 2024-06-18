# AppAuthorizerDatabricksDatabricksAuthorizerCreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'databricks']
**data** | [**DatabricksDtoAuthorizer**](DatabricksDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_databricks_databricks_authorizer_create_service_request import AppAuthorizerDatabricksDatabricksAuthorizerCreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerDatabricksDatabricksAuthorizerCreateServiceRequest from a JSON string
app_authorizer_databricks_databricks_authorizer_create_service_request_instance = AppAuthorizerDatabricksDatabricksAuthorizerCreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerDatabricksDatabricksAuthorizerCreateServiceRequest.to_json())

# convert the object into a dict
app_authorizer_databricks_databricks_authorizer_create_service_request_dict = app_authorizer_databricks_databricks_authorizer_create_service_request_instance.to_dict()
# create an instance of AppAuthorizerDatabricksDatabricksAuthorizerCreateServiceRequest from a dict
app_authorizer_databricks_databricks_authorizer_create_service_request_from_dict = AppAuthorizerDatabricksDatabricksAuthorizerCreateServiceRequest.from_dict(app_authorizer_databricks_databricks_authorizer_create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


