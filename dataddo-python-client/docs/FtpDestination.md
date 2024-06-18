# FtpDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**last_use** | **datetime** |  | [optional] 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**status_detail** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.ftp_destination import FtpDestination

# TODO update the JSON string below
json = "{}"
# create an instance of FtpDestination from a JSON string
ftp_destination_instance = FtpDestination.from_json(json)
# print the JSON string representation of the object
print(FtpDestination.to_json())

# convert the object into a dict
ftp_destination_dict = ftp_destination_instance.to_dict()
# create an instance of FtpDestination from a dict
ftp_destination_from_dict = FtpDestination.from_dict(ftp_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


