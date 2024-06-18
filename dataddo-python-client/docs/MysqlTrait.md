# MysqlTrait


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
**extra_params** | **Dict[str, str]** | string&gt; | [optional] 

## Example

```python
from openapi_client.models.mysql_trait import MysqlTrait

# TODO update the JSON string below
json = "{}"
# create an instance of MysqlTrait from a JSON string
mysql_trait_instance = MysqlTrait.from_json(json)
# print the JSON string representation of the object
print(MysqlTrait.to_json())

# convert the object into a dict
mysql_trait_dict = mysql_trait_instance.to_dict()
# create an instance of MysqlTrait from a dict
mysql_trait_from_dict = MysqlTrait.from_dict(mysql_trait_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


