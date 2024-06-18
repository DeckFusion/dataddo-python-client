# MongoStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.mongo_storage_request import MongoStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MongoStorageRequest from a JSON string
mongo_storage_request_instance = MongoStorageRequest.from_json(json)
# print the JSON string representation of the object
print(MongoStorageRequest.to_json())

# convert the object into a dict
mongo_storage_request_dict = mongo_storage_request_instance.to_dict()
# create an instance of MongoStorageRequest from a dict
mongo_storage_request_from_dict = MongoStorageRequest.from_dict(mongo_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


