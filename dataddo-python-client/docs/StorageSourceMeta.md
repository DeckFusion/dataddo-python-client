# StorageSourceMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**updated_at** | **str** | When the source was updated for the last time | [optional] 
**engine** | [**SourceEngineDTO**](SourceEngineDTO.md) |  | [optional] 
**metadata** | [**SourceMetadataDTO**](SourceMetadataDTO.md) |  | [optional] 
**columns** | [**List[SourceColumnDTO]**](SourceColumnDTO.md) |  | [optional] 

## Example

```python
from openapi_client.models.storage_source_meta import StorageSourceMeta

# TODO update the JSON string below
json = "{}"
# create an instance of StorageSourceMeta from a JSON string
storage_source_meta_instance = StorageSourceMeta.from_json(json)
# print the JSON string representation of the object
print(StorageSourceMeta.to_json())

# convert the object into a dict
storage_source_meta_dict = storage_source_meta_instance.to_dict()
# create an instance of StorageSourceMeta from a dict
storage_source_meta_from_dict = StorageSourceMeta.from_dict(storage_source_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


