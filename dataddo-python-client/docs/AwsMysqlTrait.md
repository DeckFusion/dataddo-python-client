# AwsMysqlTrait


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
from openapi_client.models.aws_mysql_trait import AwsMysqlTrait

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMysqlTrait from a JSON string
aws_mysql_trait_instance = AwsMysqlTrait.from_json(json)
# print the JSON string representation of the object
print(AwsMysqlTrait.to_json())

# convert the object into a dict
aws_mysql_trait_dict = aws_mysql_trait_instance.to_dict()
# create an instance of AwsMysqlTrait from a dict
aws_mysql_trait_from_dict = AwsMysqlTrait.from_dict(aws_mysql_trait_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


