# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.app_authorizer_mongo_mongo_authorizer_create_service_request import AppAuthorizerMongoMongoAuthorizerCreateServiceRequest

class TestAppAuthorizerMongoMongoAuthorizerCreateServiceRequest(unittest.TestCase):
    """AppAuthorizerMongoMongoAuthorizerCreateServiceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppAuthorizerMongoMongoAuthorizerCreateServiceRequest:
        """Test AppAuthorizerMongoMongoAuthorizerCreateServiceRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppAuthorizerMongoMongoAuthorizerCreateServiceRequest`
        """
        model = AppAuthorizerMongoMongoAuthorizerCreateServiceRequest()
        if include_optional:
            return AppAuthorizerMongoMongoAuthorizerCreateServiceRequest(
                service = 'mongo',
                data = openapi_client.models.mongo_dto_authorizer.MongoDtoAuthorizer()
            )
        else:
            return AppAuthorizerMongoMongoAuthorizerCreateServiceRequest(
        )
        """

    def testAppAuthorizerMongoMongoAuthorizerCreateServiceRequest(self):
        """Test AppAuthorizerMongoMongoAuthorizerCreateServiceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
