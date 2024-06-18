# MicrosoftAdsCustomUserAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**created_at** | **int** |  | [optional] 
**updated_at** | **int** |  | [optional] 
**label** | **str** |  | [optional] 
**object_id** | **str** |  | [optional] 
**status** | **bool** |  | [optional] 
**status_detail** | **str** |  | [optional] 
**service_type** | **str** |  | [optional] 
**last_use** | **datetime** |  | [optional] 
**identifier** | **str** |  | [optional] 
**hash** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**developer_token** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.microsoft_ads_custom_user_auth import MicrosoftAdsCustomUserAuth

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftAdsCustomUserAuth from a JSON string
microsoft_ads_custom_user_auth_instance = MicrosoftAdsCustomUserAuth.from_json(json)
# print the JSON string representation of the object
print(MicrosoftAdsCustomUserAuth.to_json())

# convert the object into a dict
microsoft_ads_custom_user_auth_dict = microsoft_ads_custom_user_auth_instance.to_dict()
# create an instance of MicrosoftAdsCustomUserAuth from a dict
microsoft_ads_custom_user_auth_from_dict = MicrosoftAdsCustomUserAuth.from_dict(microsoft_ads_custom_user_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

