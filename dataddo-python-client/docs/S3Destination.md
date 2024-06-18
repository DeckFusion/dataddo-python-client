# S3Destination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**last_use** | **datetime** |  | [optional] 
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**status_detail** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.s3_destination import S3Destination

# TODO update the JSON string below
json = "{}"
# create an instance of S3Destination from a JSON string
s3_destination_instance = S3Destination.from_json(json)
# print the JSON string representation of the object
print(S3Destination.to_json())

# convert the object into a dict
s3_destination_dict = s3_destination_instance.to_dict()
# create an instance of S3Destination from a dict
s3_destination_from_dict = S3Destination.from_dict(s3_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


