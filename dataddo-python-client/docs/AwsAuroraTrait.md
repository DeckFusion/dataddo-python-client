# AwsAuroraTrait


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**username** | **str** |  | [optional] 
**database** | **str** |  | [optional] 
**ssh_config** | [**AwsAuroraTraitSshConfig**](AwsAuroraTraitSshConfig.md) |  | [optional] 
**ssl** | **str** |  | [optional] 
**tls** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.aws_aurora_trait import AwsAuroraTrait

# TODO update the JSON string below
json = "{}"
# create an instance of AwsAuroraTrait from a JSON string
aws_aurora_trait_instance = AwsAuroraTrait.from_json(json)
# print the JSON string representation of the object
print(AwsAuroraTrait.to_json())

# convert the object into a dict
aws_aurora_trait_dict = aws_aurora_trait_instance.to_dict()
# create an instance of AwsAuroraTrait from a dict
aws_aurora_trait_from_dict = AwsAuroraTrait.from_dict(aws_aurora_trait_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


