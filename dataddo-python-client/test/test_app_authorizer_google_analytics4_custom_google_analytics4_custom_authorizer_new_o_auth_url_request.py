# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.app_authorizer_google_analytics4_custom_google_analytics4_custom_authorizer_new_o_auth_url_request import AppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequest

class TestAppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequest(unittest.TestCase):
    """AppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequest:
        """Test AppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequest`
        """
        model = AppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequest()
        if include_optional:
            return AppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequest(
                config = openapi_client.models.app_authorizer_google_analytics4_custom_google_analytics4_custom_authorizer_new_o_auth_url_request_config.appAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrl_request_config(
                    client_id = '', 
                    redirect_uri = '', 
                    scopes = [
                        ''
                        ], ),
                state = '',
                service_id = ''
            )
        else:
            return AppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequest(
                config = openapi_client.models.app_authorizer_google_analytics4_custom_google_analytics4_custom_authorizer_new_o_auth_url_request_config.appAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrl_request_config(
                    client_id = '', 
                    redirect_uri = '', 
                    scopes = [
                        ''
                        ], ),
        )
        """

    def testAppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequest(self):
        """Test AppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
