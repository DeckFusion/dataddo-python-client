# Api


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary key of document. The value is null when document is not persisted. | [optional] 
**customer_id** | **str** | Customer identifier | [optional] 
**app** | **str** | Dashboard app type | [optional] 
**last** | **object** | Last execution | [optional] 

## Example

```python
from openapi_client.models.api import Api

# TODO update the JSON string below
json = "{}"
# create an instance of Api from a JSON string
api_instance = Api.from_json(json)
# print the JSON string representation of the object
print(Api.to_json())

# convert the object into a dict
api_dict = api_instance.to_dict()
# create an instance of Api from a dict
api_from_dict = Api.from_dict(api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


