# ServiceListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**service** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**last_action** | **int** |  | [optional] 
**status** | **bool** |  | [optional] 
**status_detail** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**service_type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_list_response import ServiceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceListResponse from a JSON string
service_list_response_instance = ServiceListResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceListResponse.to_json())

# convert the object into a dict
service_list_response_dict = service_list_response_instance.to_dict()
# create an instance of ServiceListResponse from a dict
service_list_response_from_dict = ServiceListResponse.from_dict(service_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


