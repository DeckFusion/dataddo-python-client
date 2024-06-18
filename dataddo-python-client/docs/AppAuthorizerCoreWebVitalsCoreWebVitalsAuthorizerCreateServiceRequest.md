# AppAuthorizerCoreWebVitalsCoreWebVitalsAuthorizerCreateServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] [default to 'core_web_vitals']
**data** | [**CoreWebVitalsDtoAuthorizer**](CoreWebVitalsDtoAuthorizer.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_core_web_vitals_core_web_vitals_authorizer_create_service_request import AppAuthorizerCoreWebVitalsCoreWebVitalsAuthorizerCreateServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerCoreWebVitalsCoreWebVitalsAuthorizerCreateServiceRequest from a JSON string
app_authorizer_core_web_vitals_core_web_vitals_authorizer_create_service_request_instance = AppAuthorizerCoreWebVitalsCoreWebVitalsAuthorizerCreateServiceRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerCoreWebVitalsCoreWebVitalsAuthorizerCreateServiceRequest.to_json())

# convert the object into a dict
app_authorizer_core_web_vitals_core_web_vitals_authorizer_create_service_request_dict = app_authorizer_core_web_vitals_core_web_vitals_authorizer_create_service_request_instance.to_dict()
# create an instance of AppAuthorizerCoreWebVitalsCoreWebVitalsAuthorizerCreateServiceRequest from a dict
app_authorizer_core_web_vitals_core_web_vitals_authorizer_create_service_request_from_dict = AppAuthorizerCoreWebVitalsCoreWebVitalsAuthorizerCreateServiceRequest.from_dict(app_authorizer_core_web_vitals_core_web_vitals_authorizer_create_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


