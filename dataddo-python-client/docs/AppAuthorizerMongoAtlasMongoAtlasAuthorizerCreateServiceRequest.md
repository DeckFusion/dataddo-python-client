# AppAuthorizerMongoAtlasMongoAtlasAuthorizerCreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'mongo_atlas']
**data** | [**MongoDtoAuthorizer**](MongoDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_mongo_atlas_mongo_atlas_authorizer_create_service_request import AppAuthorizerMongoAtlasMongoAtlasAuthorizerCreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerMongoAtlasMongoAtlasAuthorizerCreateServiceRequest from a JSON string
app_authorizer_mongo_atlas_mongo_atlas_authorizer_create_service_request_instance = AppAuthorizerMongoAtlasMongoAtlasAuthorizerCreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerMongoAtlasMongoAtlasAuthorizerCreateServiceRequest.to_json())

# convert the object into a dict
app_authorizer_mongo_atlas_mongo_atlas_authorizer_create_service_request_dict = app_authorizer_mongo_atlas_mongo_atlas_authorizer_create_service_request_instance.to_dict()
# create an instance of AppAuthorizerMongoAtlasMongoAtlasAuthorizerCreateServiceRequest from a dict
app_authorizer_mongo_atlas_mongo_atlas_authorizer_create_service_request_from_dict = AppAuthorizerMongoAtlasMongoAtlasAuthorizerCreateServiceRequest.from_dict(app_authorizer_mongo_atlas_mongo_atlas_authorizer_create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


