# RedshiftStorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.redshift_storage_request import RedshiftStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedshiftStorageRequest from a JSON string
redshift_storage_request_instance = RedshiftStorageRequest.from_json(json)
# print the JSON string representation of the object
print(RedshiftStorageRequest.to_json())

# convert the object into a dict
redshift_storage_request_dict = redshift_storage_request_instance.to_dict()
# create an instance of RedshiftStorageRequest from a dict
redshift_storage_request_from_dict = RedshiftStorageRequest.from_dict(redshift_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


