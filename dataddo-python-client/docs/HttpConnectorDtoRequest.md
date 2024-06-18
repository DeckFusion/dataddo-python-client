# HttpConnectorDtoRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**headers** | **List[str]** |  | [optional] 
**transformation** | **str** |  | [optional] 
**body** | **str** |  | [optional] 
**ensure_data_types** | **List[str]** |  | [optional] 
**emitter** | **str** |  | [optional] 
**emit_only** | **bool** |  | [optional] 
**format** | **str** |  | [optional] 
**timeout** | **int** |  | [optional] 
**sleep_time_millisecond** | **int** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.http_connector_dto_request import HttpConnectorDtoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HttpConnectorDtoRequest from a JSON string
http_connector_dto_request_instance = HttpConnectorDtoRequest.from_json(json)
# print the JSON string representation of the object
print(HttpConnectorDtoRequest.to_json())

# convert the object into a dict
http_connector_dto_request_dict = http_connector_dto_request_instance.to_dict()
# create an instance of HttpConnectorDtoRequest from a dict
http_connector_dto_request_from_dict = HttpConnectorDtoRequest.from_dict(http_connector_dto_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


