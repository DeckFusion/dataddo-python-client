# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.app_authorizer_microsoft_dynamics365_microsoft_dynamics365_authorizer_get_authorization_url_request_config_inner import AppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerGetAuthorizationUrlRequestConfigInner

class TestAppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerGetAuthorizationUrlRequestConfigInner(unittest.TestCase):
    """AppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerGetAuthorizationUrlRequestConfigInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerGetAuthorizationUrlRequestConfigInner:
        """Test AppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerGetAuthorizationUrlRequestConfigInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerGetAuthorizationUrlRequestConfigInner`
        """
        model = AppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerGetAuthorizationUrlRequestConfigInner()
        if include_optional:
            return AppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerGetAuthorizationUrlRequestConfigInner(
                host = 'orgdb40e000.crm.dynamics.com'
            )
        else:
            return AppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerGetAuthorizationUrlRequestConfigInner(
        )
        """

    def testAppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerGetAuthorizationUrlRequestConfigInner(self):
        """Test AppAuthorizerMicrosoftDynamics365MicrosoftDynamics365AuthorizerGetAuthorizationUrlRequestConfigInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
