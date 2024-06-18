# GoogleMysqlTrait


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
from openapi_client.models.google_mysql_trait import GoogleMysqlTrait

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleMysqlTrait from a JSON string
google_mysql_trait_instance = GoogleMysqlTrait.from_json(json)
# print the JSON string representation of the object
print(GoogleMysqlTrait.to_json())

# convert the object into a dict
google_mysql_trait_dict = google_mysql_trait_instance.to_dict()
# create an instance of GoogleMysqlTrait from a dict
google_mysql_trait_from_dict = GoogleMysqlTrait.from_dict(google_mysql_trait_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


