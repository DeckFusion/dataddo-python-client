# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.app_authorizer_aws_pgsql_aws_pgsql_authorizer_create_service_request import AppAuthorizerAwsPgsqlAwsPgsqlAuthorizerCreateServiceRequest

class TestAppAuthorizerAwsPgsqlAwsPgsqlAuthorizerCreateServiceRequest(unittest.TestCase):
    """AppAuthorizerAwsPgsqlAwsPgsqlAuthorizerCreateServiceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppAuthorizerAwsPgsqlAwsPgsqlAuthorizerCreateServiceRequest:
        """Test AppAuthorizerAwsPgsqlAwsPgsqlAuthorizerCreateServiceRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppAuthorizerAwsPgsqlAwsPgsqlAuthorizerCreateServiceRequest`
        """
        model = AppAuthorizerAwsPgsqlAwsPgsqlAuthorizerCreateServiceRequest()
        if include_optional:
            return AppAuthorizerAwsPgsqlAwsPgsqlAuthorizerCreateServiceRequest(
                service = 'aws_pgsql',
                data = openapi_client.models.aws_pgsql_dto_authorizer.AwsPgsqlDtoAuthorizer()
            )
        else:
            return AppAuthorizerAwsPgsqlAwsPgsqlAuthorizerCreateServiceRequest(
        )
        """

    def testAppAuthorizerAwsPgsqlAwsPgsqlAuthorizerCreateServiceRequest(self):
        """Test AppAuthorizerAwsPgsqlAwsPgsqlAuthorizerCreateServiceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()