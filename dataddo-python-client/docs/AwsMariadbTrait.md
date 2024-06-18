# AwsMariadbTrait


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
from openapi_client.models.aws_mariadb_trait import AwsMariadbTrait

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMariadbTrait from a JSON string
aws_mariadb_trait_instance = AwsMariadbTrait.from_json(json)
# print the JSON string representation of the object
print(AwsMariadbTrait.to_json())

# convert the object into a dict
aws_mariadb_trait_dict = aws_mariadb_trait_instance.to_dict()
# create an instance of AwsMariadbTrait from a dict
aws_mariadb_trait_from_dict = AwsMariadbTrait.from_dict(aws_mariadb_trait_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


