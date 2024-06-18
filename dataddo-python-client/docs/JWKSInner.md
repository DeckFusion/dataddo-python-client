# JWKSInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** |  | [optional] 
**kty** | **str** |  | [optional] 
**use** | **str** |  | [optional] 
**key_ops** | **str** |  | [optional] 
**kid** | **str** |  | [optional] 
**crv** | **str** |  | [optional] 
**x** | **str** |  | [optional] 
**y** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.jwks_inner import JWKSInner

# TODO update the JSON string below
json = "{}"
# create an instance of JWKSInner from a JSON string
jwks_inner_instance = JWKSInner.from_json(json)
# print the JSON string representation of the object
print(JWKSInner.to_json())

# convert the object into a dict
jwks_inner_dict = jwks_inner_instance.to_dict()
# create an instance of JWKSInner from a dict
jwks_inner_from_dict = JWKSInner.from_dict(jwks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


