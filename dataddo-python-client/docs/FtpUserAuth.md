# FtpUserAuth


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

## Example

```python
from openapi_client.models.ftp_user_auth import FtpUserAuth

# TODO update the JSON string below
json = "{}"
# create an instance of FtpUserAuth from a JSON string
ftp_user_auth_instance = FtpUserAuth.from_json(json)
# print the JSON string representation of the object
print(FtpUserAuth.to_json())

# convert the object into a dict
ftp_user_auth_dict = ftp_user_auth_instance.to_dict()
# create an instance of FtpUserAuth from a dict
ftp_user_auth_from_dict = FtpUserAuth.from_dict(ftp_user_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


