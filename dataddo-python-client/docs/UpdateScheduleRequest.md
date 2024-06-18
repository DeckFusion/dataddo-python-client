# UpdateScheduleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sync_frequency** | **str** |  | [optional] 
**timezone** | **str** | Timezone schedule definition | [optional] 
**minute** | **str** | Hour schedule definition | [optional] 
**hour** | **str** | Hour schedule definition | [optional] 
**day_of_month** | **str** | Day of month schedule definition | [optional] 
**month** | **str** | Month schedule definition | [optional] 
**day_of_week** | **str** | Day of week schedule definition | [optional] 

## Example

```python
from openapi_client.models.update_schedule_request import UpdateScheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateScheduleRequest from a JSON string
update_schedule_request_instance = UpdateScheduleRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateScheduleRequest.to_json())

# convert the object into a dict
update_schedule_request_dict = update_schedule_request_instance.to_dict()
# create an instance of UpdateScheduleRequest from a dict
update_schedule_request_from_dict = UpdateScheduleRequest.from_dict(update_schedule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


