# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.app_authorizer_alloy_db_alloy_db_authorizer_create_service_request import AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest

class TestAppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest(unittest.TestCase):
    """AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest:
        """Test AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest`
        """
        model = AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest()
        if include_optional:
            return AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest(
                service = 'alloy_db',
                data = openapi_client.models.alloy_db_dto_authorizer.AlloyDbDtoAuthorizer()
            )
        else:
            return AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest(
        )
        """

    def testAppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest(self):
        """Test AppAuthorizerAlloyDbAlloyDbAuthorizerCreateServiceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
