# OperationRequestLimit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | [optional] 
**index** | **int** |  | [optional] 
**length** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.operation_request_limit import OperationRequestLimit

# TODO update the JSON string below
json = "{}"
# create an instance of OperationRequestLimit from a JSON string
operation_request_limit_instance = OperationRequestLimit.from_json(json)
# print the JSON string representation of the object
print(OperationRequestLimit.to_json())

# convert the object into a dict
operation_request_limit_dict = operation_request_limit_instance.to_dict()
# create an instance of OperationRequestLimit from a dict
operation_request_limit_from_dict = OperationRequestLimit.from_dict(operation_request_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


