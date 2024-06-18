# SftpStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sftp_storage_request import SftpStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SftpStorageRequest from a JSON string
sftp_storage_request_instance = SftpStorageRequest.from_json(json)
# print the JSON string representation of the object
print(SftpStorageRequest.to_json())

# convert the object into a dict
sftp_storage_request_dict = sftp_storage_request_instance.to_dict()
# create an instance of SftpStorageRequest from a dict
sftp_storage_request_from_dict = SftpStorageRequest.from_dict(sftp_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


