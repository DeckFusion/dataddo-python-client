# ConnectorListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**categories** | **List[str]** |  | [optional] 
**group** | **str** |  | [optional] 
**customers** | **List[int]** |  | [optional] 
**created_at** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**services** | **List[object]** |  | [optional] 
**priority** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.connector_list_response import ConnectorListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectorListResponse from a JSON string
connector_list_response_instance = ConnectorListResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectorListResponse.to_json())

# convert the object into a dict
connector_list_response_dict = connector_list_response_instance.to_dict()
# create an instance of ConnectorListResponse from a dict
connector_list_response_from_dict = ConnectorListResponse.from_dict(connector_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


