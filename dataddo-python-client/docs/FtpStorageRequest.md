# FtpStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ftp_storage_request import FtpStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FtpStorageRequest from a JSON string
ftp_storage_request_instance = FtpStorageRequest.from_json(json)
# print the JSON string representation of the object
print(FtpStorageRequest.to_json())

# convert the object into a dict
ftp_storage_request_dict = ftp_storage_request_instance.to_dict()
# create an instance of FtpStorageRequest from a dict
ftp_storage_request_from_dict = FtpStorageRequest.from_dict(ftp_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


