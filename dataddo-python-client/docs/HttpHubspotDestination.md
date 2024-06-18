# HttpHubspotDestination


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
**o_auth_id** | **int** |  | [optional] 
**api_object** | **str** |  | [optional] 
**api_object_custom_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.http_hubspot_destination import HttpHubspotDestination

# TODO update the JSON string below
json = "{}"
# create an instance of HttpHubspotDestination from a JSON string
http_hubspot_destination_instance = HttpHubspotDestination.from_json(json)
# print the JSON string representation of the object
print(HttpHubspotDestination.to_json())

# convert the object into a dict
http_hubspot_destination_dict = http_hubspot_destination_instance.to_dict()
# create an instance of HttpHubspotDestination from a dict
http_hubspot_destination_from_dict = HttpHubspotDestination.from_dict(http_hubspot_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


