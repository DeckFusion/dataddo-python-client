# CreateCertificateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**file_content** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_certificate_request import CreateCertificateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCertificateRequest from a JSON string
create_certificate_request_instance = CreateCertificateRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCertificateRequest.to_json())

# convert the object into a dict
create_certificate_request_dict = create_certificate_request_instance.to_dict()
# create an instance of CreateCertificateRequest from a dict
create_certificate_request_from_dict = CreateCertificateRequest.from_dict(create_certificate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


