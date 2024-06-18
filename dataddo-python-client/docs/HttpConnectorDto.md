# HttpConnectorDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**storage_strategy** | **str** |  | [optional] [default to 'incremental']
**allow_empty** | **bool** |  | [optional] [default to False]
**request** | [**HttpConnectorDtoRequest**](HttpConnectorDtoRequest.md) |  | [optional] 

## Example

```python
from openapi_client.models.http_connector_dto import HttpConnectorDto

# TODO update the JSON string below
json = "{}"
# create an instance of HttpConnectorDto from a JSON string
http_connector_dto_instance = HttpConnectorDto.from_json(json)
# print the JSON string representation of the object
print(HttpConnectorDto.to_json())

# convert the object into a dict
http_connector_dto_dict = http_connector_dto_instance.to_dict()
# create an instance of HttpConnectorDto from a dict
http_connector_dto_from_dict = HttpConnectorDto.from_dict(http_connector_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


