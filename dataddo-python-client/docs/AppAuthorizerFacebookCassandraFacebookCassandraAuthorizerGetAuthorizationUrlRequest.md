# AppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**AppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequestConfig**](AppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequestConfig.md) |  | [optional] 
**state** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.app_authorizer_facebook_cassandra_facebook_cassandra_authorizer_get_authorization_url_request import AppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequest from a JSON string
app_authorizer_facebook_cassandra_facebook_cassandra_authorizer_get_authorization_url_request_instance = AppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequest.from_json(json)
# print the JSON string representation of the object
print(AppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequest.to_json())

# convert the object into a dict
app_authorizer_facebook_cassandra_facebook_cassandra_authorizer_get_authorization_url_request_dict = app_authorizer_facebook_cassandra_facebook_cassandra_authorizer_get_authorization_url_request_instance.to_dict()
# create an instance of AppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequest from a dict
app_authorizer_facebook_cassandra_facebook_cassandra_authorizer_get_authorization_url_request_from_dict = AppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequest.from_dict(app_authorizer_facebook_cassandra_facebook_cassandra_authorizer_get_authorization_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


