# AwsS3StorageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**o_auth_id** | **int** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.aws_s3_storage_request import AwsS3StorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AwsS3StorageRequest from a JSON string
aws_s3_storage_request_instance = AwsS3StorageRequest.from_json(json)
# print the JSON string representation of the object
print(AwsS3StorageRequest.to_json())

# convert the object into a dict
aws_s3_storage_request_dict = aws_s3_storage_request_instance.to_dict()
# create an instance of AwsS3StorageRequest from a dict
aws_s3_storage_request_from_dict = AwsS3StorageRequest.from_dict(aws_s3_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


