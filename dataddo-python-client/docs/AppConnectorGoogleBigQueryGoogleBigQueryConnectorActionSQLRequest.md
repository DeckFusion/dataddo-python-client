# AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionSQLRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | **List[str]** |  | [optional] 
**table_id** | **str** |  | [optional] 
**dataset_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.app_connector_google_big_query_google_big_query_connector_action_sql_request import AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionSQLRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionSQLRequest from a JSON string
app_connector_google_big_query_google_big_query_connector_action_sql_request_instance = AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionSQLRequest.from_json(json)
# print the JSON string representation of the object
print(AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionSQLRequest.to_json())

# convert the object into a dict
app_connector_google_big_query_google_big_query_connector_action_sql_request_dict = app_connector_google_big_query_google_big_query_connector_action_sql_request_instance.to_dict()
# create an instance of AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionSQLRequest from a dict
app_connector_google_big_query_google_big_query_connector_action_sql_request_from_dict = AppConnectorGoogleBigQueryGoogleBigQueryConnectorActionSQLRequest.from_dict(app_connector_google_big_query_google_big_query_connector_action_sql_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


