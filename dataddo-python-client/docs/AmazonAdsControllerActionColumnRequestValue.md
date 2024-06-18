# AmazonAdsControllerActionColumnRequestValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_type** | **str** |  | [optional] 
**time_unit** | **str** |  | [optional] 
**group_by** | **List[object]** |  | [optional] 

## Example

```python
from openapi_client.models.amazon_ads_controller_action_column_request_value import AmazonAdsControllerActionColumnRequestValue

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonAdsControllerActionColumnRequestValue from a JSON string
amazon_ads_controller_action_column_request_value_instance = AmazonAdsControllerActionColumnRequestValue.from_json(json)
# print the JSON string representation of the object
print(AmazonAdsControllerActionColumnRequestValue.to_json())

# convert the object into a dict
amazon_ads_controller_action_column_request_value_dict = amazon_ads_controller_action_column_request_value_instance.to_dict()
# create an instance of AmazonAdsControllerActionColumnRequestValue from a dict
amazon_ads_controller_action_column_request_value_from_dict = AmazonAdsControllerActionColumnRequestValue.from_dict(amazon_ads_controller_action_column_request_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


