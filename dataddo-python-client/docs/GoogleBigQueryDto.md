# GoogleBigQueryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**storage_strategy** | **str** |  | [optional] [default to 'incremental']
**allow_empty** | **bool** |  | [optional] [default to False]
**request** | [**HttpConnectorDtoRequest**](HttpConnectorDtoRequest.md) |  | [optional] 
**o_auth_id** | **int** |  | [optional] 
**project_id** | **int** |  | [optional] 
**dataset_id** | **str** |  | [optional] 
**table_id** | **str** |  | [optional] 
**statement** | **str** |  | [optional] 
**session_read** | **bool** |  | [optional] 
**columns** | **List[object]** |  | [optional] 
**row_restriction** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.google_big_query_dto import GoogleBigQueryDto

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleBigQueryDto from a JSON string
google_big_query_dto_instance = GoogleBigQueryDto.from_json(json)
# print the JSON string representation of the object
print(GoogleBigQueryDto.to_json())

# convert the object into a dict
google_big_query_dto_dict = google_big_query_dto_instance.to_dict()
# create an instance of GoogleBigQueryDto from a dict
google_big_query_dto_from_dict = GoogleBigQueryDto.from_dict(google_big_query_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


