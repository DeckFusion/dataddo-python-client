# RedshiftDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**storage_strategy** | **str** |  | [optional] [default to 'incremental']
**allow_empty** | **bool** |  | [optional] [default to False]
**o_auth_id** | **int** |  | [optional] 
**statement** | **str** |  | [optional] 
**storage_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.redshift_dto import RedshiftDto

# TODO update the JSON string below
json = "{}"
# create an instance of RedshiftDto from a JSON string
redshift_dto_instance = RedshiftDto.from_json(json)
# print the JSON string representation of the object
print(RedshiftDto.to_json())

# convert the object into a dict
redshift_dto_dict = redshift_dto_instance.to_dict()
# create an instance of RedshiftDto from a dict
redshift_dto_from_dict = RedshiftDto.from_dict(redshift_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


