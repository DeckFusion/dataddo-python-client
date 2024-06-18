# SftpUserAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**object_id** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**status_detail** | **str** |  | [optional] 
**service_type** | **str** |  | [optional] 
**last_use** | **datetime** |  | [optional] 
**identifier** | **str** |  | [optional] 
**hash** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**timeout** | **int** |  | [optional] 
**certificate_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sftp_user_auth import SftpUserAuth

# TODO update the JSON string below
json = "{}"
# create an instance of SftpUserAuth from a JSON string
sftp_user_auth_instance = SftpUserAuth.from_json(json)
# print the JSON string representation of the object
print(SftpUserAuth.to_json())

# convert the object into a dict
sftp_user_auth_dict = sftp_user_auth_instance.to_dict()
# create an instance of SftpUserAuth from a dict
sftp_user_auth_from_dict = SftpUserAuth.from_dict(sftp_user_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


