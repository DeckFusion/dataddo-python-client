# AppAuthorizerMercadoLibreMercadoLibreAuthorizerGetAuthorizationUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**AppAuthorizerMercadoLibreMercadoLibreAuthorizerGetAuthorizationUrlRequestConfig**](AppAuthorizerMercadoLibreMercadoLibreAuthorizerGetAuthorizationUrlRequestConfig.md) |  | [optional] 
**state** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_mercado_libre_mercado_libre_authorizer_get_authorization_url_request import AppAuthorizerMercadoLibreMercadoLibreAuthorizerGetAuthorizationUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerMercadoLibreMercadoLibreAuthorizerGetAuthorizationUrlRequest from a JSON string
app_authorizer_mercado_libre_mercado_libre_authorizer_get_authorization_url_request_instance = AppAuthorizerMercadoLibreMercadoLibreAuthorizerGetAuthorizationUrlRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerMercadoLibreMercadoLibreAuthorizerGetAuthorizationUrlRequest.to_json())

# convert the object into a dict
app_authorizer_mercado_libre_mercado_libre_authorizer_get_authorization_url_request_dict = app_authorizer_mercado_libre_mercado_libre_authorizer_get_authorization_url_request_instance.to_dict()
# create an instance of AppAuthorizerMercadoLibreMercadoLibreAuthorizerGetAuthorizationUrlRequest from a dict
app_authorizer_mercado_libre_mercado_libre_authorizer_get_authorization_url_request_from_dict = AppAuthorizerMercadoLibreMercadoLibreAuthorizerGetAuthorizationUrlRequest.from_dict(app_authorizer_mercado_libre_mercado_libre_authorizer_get_authorization_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


