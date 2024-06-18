# CreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**data** | **object** |  | [optional] 
**config** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.create_service_request import CreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateServiceRequest from a JSON string
create_service_request_instance = CreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateServiceRequest.to_json())

# convert the object into a dict
create_service_request_dict = create_service_request_instance.to_dict()
# create an instance of CreateServiceRequest from a dict
create_service_request_from_dict = CreateServiceRequest.from_dict(create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


