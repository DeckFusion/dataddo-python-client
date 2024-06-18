# SshTrait


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_ssh** | **bool** |  | [optional] 
**certificate_id** | **str** |  | [optional] 
**ssh_host** | **str** |  | [optional] 
**ssh_port** | **int** |  | [optional] 
**ssh_remote_host** | **str** |  | [optional] 
**ssh_remote_port** | **int** |  | [optional] 
**ssh_username** | **str** |  | [optional] 
**ssh_password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ssh_trait import SshTrait

# TODO update the JSON string below
json = "{}"
# create an instance of SshTrait from a JSON string
ssh_trait_instance = SshTrait.from_json(json)
# print the JSON string representation of the object
print(SshTrait.to_json())

# convert the object into a dict
ssh_trait_dict = ssh_trait_instance.to_dict()
# create an instance of SshTrait from a dict
ssh_trait_from_dict = SshTrait.from_dict(ssh_trait_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


