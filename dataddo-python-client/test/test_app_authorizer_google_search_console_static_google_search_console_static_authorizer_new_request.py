# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.app_authorizer_google_search_console_static_google_search_console_static_authorizer_new_request import AppAuthorizerGoogleSearchConsoleStaticGoogleSearchConsoleStaticAuthorizerNewRequest

class TestAppAuthorizerGoogleSearchConsoleStaticGoogleSearchConsoleStaticAuthorizerNewRequest(unittest.TestCase):
    """AppAuthorizerGoogleSearchConsoleStaticGoogleSearchConsoleStaticAuthorizerNewRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppAuthorizerGoogleSearchConsoleStaticGoogleSearchConsoleStaticAuthorizerNewRequest:
        """Test AppAuthorizerGoogleSearchConsoleStaticGoogleSearchConsoleStaticAuthorizerNewRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppAuthorizerGoogleSearchConsoleStaticGoogleSearchConsoleStaticAuthorizerNewRequest`
        """
        model = AppAuthorizerGoogleSearchConsoleStaticGoogleSearchConsoleStaticAuthorizerNewRequest()
        if include_optional:
            return AppAuthorizerGoogleSearchConsoleStaticGoogleSearchConsoleStaticAuthorizerNewRequest(
                service = 'google_search_console_static',
                data = openapi_client.models.google_search_console_static_dto_authorizer.GoogleSearchConsoleStaticDtoAuthorizer()
            )
        else:
            return AppAuthorizerGoogleSearchConsoleStaticGoogleSearchConsoleStaticAuthorizerNewRequest(
        )
        """

    def testAppAuthorizerGoogleSearchConsoleStaticGoogleSearchConsoleStaticAuthorizerNewRequest(self):
        """Test AppAuthorizerGoogleSearchConsoleStaticGoogleSearchConsoleStaticAuthorizerNewRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
