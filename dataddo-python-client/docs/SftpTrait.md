# SftpTrait


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**timeout** | **int** |  | [optional] 
**certificate_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sftp_trait import SftpTrait

# TODO update the JSON string below
json = "{}"
# create an instance of SftpTrait from a JSON string
sftp_trait_instance = SftpTrait.from_json(json)
# print the JSON string representation of the object
print(SftpTrait.to_json())

# convert the object into a dict
sftp_trait_dict = sftp_trait_instance.to_dict()
# create an instance of SftpTrait from a dict
sftp_trait_from_dict = SftpTrait.from_dict(sftp_trait_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


