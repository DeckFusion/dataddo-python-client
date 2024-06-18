# Schedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timezone** | **str** | Timezone cron identifier | [optional] 
**minute** | **object** | Minute cron identifier | [optional] 
**hour** | **object** | Hour cron identifier | [optional] 
**day_of_month** | **object** | Day of month cron identifier | [optional] 
**month** | **object** | Month cron identifier | [optional] 
**day_of_week** | **object** | Day of week cron identifier | [optional] 
**sync_frequency** | **object** | Sync frequency (day/week/month/custom) | [optional] 

## Example

```python
from openapi_client.models.schedule import Schedule

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule from a JSON string
schedule_instance = Schedule.from_json(json)
# print the JSON string representation of the object
print(Schedule.to_json())

# convert the object into a dict
schedule_dict = schedule_instance.to_dict()
# create an instance of Schedule from a dict
schedule_from_dict = Schedule.from_dict(schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


