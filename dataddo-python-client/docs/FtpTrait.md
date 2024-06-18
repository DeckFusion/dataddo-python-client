# FtpTrait


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**timeout** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.ftp_trait import FtpTrait

# TODO update the JSON string below
json = "{}"
# create an instance of FtpTrait from a JSON string
ftp_trait_instance = FtpTrait.from_json(json)
# print the JSON string representation of the object
print(FtpTrait.to_json())

# convert the object into a dict
ftp_trait_dict = ftp_trait_instance.to_dict()
# create an instance of FtpTrait from a dict
ftp_trait_from_dict = FtpTrait.from_dict(ftp_trait_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


