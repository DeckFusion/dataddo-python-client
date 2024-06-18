# SageIntacctDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connector_id** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**storage_strategy** | **str** |  | [optional] [default to 'incremental']
**allow_empty** | **bool** |  | [optional] [default to False]
**request** | [**HttpConnectorDtoRequest**](HttpConnectorDtoRequest.md) |  | [optional] 
**o_auth_id** | **int** |  | [optional] 
**date_range** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sage_intacct_dto import SageIntacctDto

# TODO update the JSON string below
json = "{}"
# create an instance of SageIntacctDto from a JSON string
sage_intacct_dto_instance = SageIntacctDto.from_json(json)
# print the JSON string representation of the object
print(SageIntacctDto.to_json())

# convert the object into a dict
sage_intacct_dto_dict = sage_intacct_dto_instance.to_dict()
# create an instance of SageIntacctDto from a dict
sage_intacct_dto_from_dict = SageIntacctDto.from_dict(sage_intacct_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


