# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.app_authorizer_hubspot_custom_hubspot_custom_authorizer_get_authorization_url_request import AppAuthorizerHubspotCustomHubspotCustomAuthorizerGetAuthorizationUrlRequest

class TestAppAuthorizerHubspotCustomHubspotCustomAuthorizerGetAuthorizationUrlRequest(unittest.TestCase):
    """AppAuthorizerHubspotCustomHubspotCustomAuthorizerGetAuthorizationUrlRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppAuthorizerHubspotCustomHubspotCustomAuthorizerGetAuthorizationUrlRequest:
        """Test AppAuthorizerHubspotCustomHubspotCustomAuthorizerGetAuthorizationUrlRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppAuthorizerHubspotCustomHubspotCustomAuthorizerGetAuthorizationUrlRequest`
        """
        model = AppAuthorizerHubspotCustomHubspotCustomAuthorizerGetAuthorizationUrlRequest()
        if include_optional:
            return AppAuthorizerHubspotCustomHubspotCustomAuthorizerGetAuthorizationUrlRequest(
                config = openapi_client.models.app_authorizer_hubspot_custom_hubspot_custom_authorizer_get_authorization_url_request_config.appAuthorizerHubspotCustomHubspotCustomAuthorizerGetAuthorizationUrl_request_config(
                    client_id = '', 
                    redirect_uri = '', 
                    scopes = [
                        ''
                        ], 
                    optional_scopes = [
                        ''
                        ], ),
                state = '',
                service_id = ''
            )
        else:
            return AppAuthorizerHubspotCustomHubspotCustomAuthorizerGetAuthorizationUrlRequest(
                config = openapi_client.models.app_authorizer_hubspot_custom_hubspot_custom_authorizer_get_authorization_url_request_config.appAuthorizerHubspotCustomHubspotCustomAuthorizerGetAuthorizationUrl_request_config(
                    client_id = '', 
                    redirect_uri = '', 
                    scopes = [
                        ''
                        ], 
                    optional_scopes = [
                        ''
                        ], ),
        )
        """

    def testAppAuthorizerHubspotCustomHubspotCustomAuthorizerGetAuthorizationUrlRequest(self):
        """Test AppAuthorizerHubspotCustomHubspotCustomAuthorizerGetAuthorizationUrlRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
