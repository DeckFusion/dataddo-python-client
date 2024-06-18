# AppAuthorizerMongoMongoAuthorizerCreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'mongo']
**data** | [**MongoDtoAuthorizer**](MongoDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_mongo_mongo_authorizer_create_service_request import AppAuthorizerMongoMongoAuthorizerCreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerMongoMongoAuthorizerCreateServiceRequest from a JSON string
app_authorizer_mongo_mongo_authorizer_create_service_request_instance = AppAuthorizerMongoMongoAuthorizerCreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerMongoMongoAuthorizerCreateServiceRequest.to_json())

# convert the object into a dict
app_authorizer_mongo_mongo_authorizer_create_service_request_dict = app_authorizer_mongo_mongo_authorizer_create_service_request_instance.to_dict()
# create an instance of AppAuthorizerMongoMongoAuthorizerCreateServiceRequest from a dict
app_authorizer_mongo_mongo_authorizer_create_service_request_from_dict = AppAuthorizerMongoMongoAuthorizerCreateServiceRequest.from_dict(app_authorizer_mongo_mongo_authorizer_create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


