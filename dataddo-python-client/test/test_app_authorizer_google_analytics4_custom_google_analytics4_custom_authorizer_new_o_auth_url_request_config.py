# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.app_authorizer_google_analytics4_custom_google_analytics4_custom_authorizer_new_o_auth_url_request_config import AppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequestConfig

class TestAppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequestConfig(unittest.TestCase):
    """AppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequestConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequestConfig:
        """Test AppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequestConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequestConfig`
        """
        model = AppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequestConfig()
        if include_optional:
            return AppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequestConfig(
                client_id = '',
                redirect_uri = '',
                scopes = [
                    ''
                    ]
            )
        else:
            return AppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequestConfig(
                client_id = '',
                redirect_uri = '',
        )
        """

    def testAppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequestConfig(self):
        """Test AppAuthorizerGoogleAnalytics4CustomGoogleAnalytics4CustomAuthorizerNewOAuthUrlRequestConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
