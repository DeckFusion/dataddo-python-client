# AwsAuroraTraitSshConfig


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
from openapi_client.models.aws_aurora_trait_ssh_config import AwsAuroraTraitSshConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AwsAuroraTraitSshConfig from a JSON string
aws_aurora_trait_ssh_config_instance = AwsAuroraTraitSshConfig.from_json(json)
# print the JSON string representation of the object
print(AwsAuroraTraitSshConfig.to_json())

# convert the object into a dict
aws_aurora_trait_ssh_config_dict = aws_aurora_trait_ssh_config_instance.to_dict()
# create an instance of AwsAuroraTraitSshConfig from a dict
aws_aurora_trait_ssh_config_from_dict = AwsAuroraTraitSshConfig.from_dict(aws_aurora_trait_ssh_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


