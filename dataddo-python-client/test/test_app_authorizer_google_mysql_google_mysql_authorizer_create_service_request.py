# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.app_authorizer_google_mysql_google_mysql_authorizer_create_service_request import AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest

class TestAppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest(unittest.TestCase):
    """AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest:
        """Test AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest`
        """
        model = AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest()
        if include_optional:
            return AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest(
                service = 'google_mysql',
                data = openapi_client.models.google_mysql_dto_authorizer.GoogleMysqlDtoAuthorizer()
            )
        else:
            return AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest(
        )
        """

    def testAppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest(self):
        """Test AppAuthorizerGoogleMysqlGoogleMysqlAuthorizerCreateServiceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()