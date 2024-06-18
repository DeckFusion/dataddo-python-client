# SourceMetadataDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_bin_log_file** | **str** |  | [optional] 
**last_position** | **int** |  | [optional] 
**last_processed_timestamp** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.source_metadata_dto import SourceMetadataDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SourceMetadataDTO from a JSON string
source_metadata_dto_instance = SourceMetadataDTO.from_json(json)
# print the JSON string representation of the object
print(SourceMetadataDTO.to_json())

# convert the object into a dict
source_metadata_dto_dict = source_metadata_dto_instance.to_dict()
# create an instance of SourceMetadataDTO from a dict
source_metadata_dto_from_dict = SourceMetadataDTO.from_dict(source_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


