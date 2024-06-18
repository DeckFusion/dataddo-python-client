# MariadbTrait


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
from openapi_client.models.mariadb_trait import MariadbTrait

# TODO update the JSON string below
json = "{}"
# create an instance of MariadbTrait from a JSON string
mariadb_trait_instance = MariadbTrait.from_json(json)
# print the JSON string representation of the object
print(MariadbTrait.to_json())

# convert the object into a dict
mariadb_trait_dict = mariadb_trait_instance.to_dict()
# create an instance of MariadbTrait from a dict
mariadb_trait_from_dict = MariadbTrait.from_dict(mariadb_trait_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


