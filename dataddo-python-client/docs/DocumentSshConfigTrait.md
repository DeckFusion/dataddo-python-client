# DocumentSshConfigTrait


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**certificate_id** | **str** |  | [optional] 
**remote_host** | **str** |  | [optional] 
**remote_port** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.document_ssh_config_trait import DocumentSshConfigTrait

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentSshConfigTrait from a JSON string
document_ssh_config_trait_instance = DocumentSshConfigTrait.from_json(json)
# print the JSON string representation of the object
print(DocumentSshConfigTrait.to_json())

# convert the object into a dict
document_ssh_config_trait_dict = document_ssh_config_trait_instance.to_dict()
# create an instance of DocumentSshConfigTrait from a dict
document_ssh_config_trait_from_dict = DocumentSshConfigTrait.from_dict(document_ssh_config_trait_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


