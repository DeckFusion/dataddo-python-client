# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.app_authorizer_facebook_cassandra_facebook_cassandra_authorizer_get_authorization_url_request import AppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequest

class TestAppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequest(unittest.TestCase):
    """AppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequest:
        """Test AppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequest`
        """
        model = AppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequest()
        if include_optional:
            return AppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequest(
                config = openapi_client.models.app_authorizer_facebook_cassandra_facebook_cassandra_authorizer_get_authorization_url_request_config.appAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrl_request_config(
                    redirect_uri = '', 
                    scopes = [
                        ''
                        ], ),
                state = '',
                service_id = ''
            )
        else:
            return AppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequest(
        )
        """

    def testAppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequest(self):
        """Test AppAuthorizerFacebookCassandraFacebookCassandraAuthorizerGetAuthorizationUrlRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
