# FtpAdditionalSettingTrait


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_explicit_tls** | **bool** |  | [optional] 
**dial_timeout** | **int** |  | [optional] 
**shut_timeout** | **int** |  | [optional] 
**disable_epsv** | **bool** |  | [optional] 
**disable_utf8** | **bool** |  | [optional] 
**disable_mlsd** | **bool** |  | [optional] 
**mdtm_write** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.ftp_additional_setting_trait import FtpAdditionalSettingTrait

# TODO update the JSON string below
json = "{}"
# create an instance of FtpAdditionalSettingTrait from a JSON string
ftp_additional_setting_trait_instance = FtpAdditionalSettingTrait.from_json(json)
# print the JSON string representation of the object
print(FtpAdditionalSettingTrait.to_json())

# convert the object into a dict
ftp_additional_setting_trait_dict = ftp_additional_setting_trait_instance.to_dict()
# create an instance of FtpAdditionalSettingTrait from a dict
ftp_additional_setting_trait_from_dict = FtpAdditionalSettingTrait.from_dict(ftp_additional_setting_trait_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


