# MongoTraitAuthorizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dsn** | **str** |  | [optional] 
**database** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.mongo_trait_authorizer import MongoTraitAuthorizer

# TODO update the JSON string below
json = "{}"
# create an instance of MongoTraitAuthorizer from a JSON string
mongo_trait_authorizer_instance = MongoTraitAuthorizer.from_json(json)
# print the JSON string representation of the object
print(MongoTraitAuthorizer.to_json())

# convert the object into a dict
mongo_trait_authorizer_dict = mongo_trait_authorizer_instance.to_dict()
# create an instance of MongoTraitAuthorizer from a dict
mongo_trait_authorizer_from_dict = MongoTraitAuthorizer.from_dict(mongo_trait_authorizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


