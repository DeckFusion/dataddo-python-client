# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.app_authorizer_shoptet_shoptet_authorizer_new_request import AppAuthorizerShoptetShoptetAuthorizerNewRequest

class TestAppAuthorizerShoptetShoptetAuthorizerNewRequest(unittest.TestCase):
    """AppAuthorizerShoptetShoptetAuthorizerNewRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppAuthorizerShoptetShoptetAuthorizerNewRequest:
        """Test AppAuthorizerShoptetShoptetAuthorizerNewRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppAuthorizerShoptetShoptetAuthorizerNewRequest`
        """
        model = AppAuthorizerShoptetShoptetAuthorizerNewRequest()
        if include_optional:
            return AppAuthorizerShoptetShoptetAuthorizerNewRequest(
                service = 'shoptet',
                data = openapi_client.models.shoptet_dto_authorizer.ShoptetDtoAuthorizer()
            )
        else:
            return AppAuthorizerShoptetShoptetAuthorizerNewRequest(
        )
        """

    def testAppAuthorizerShoptetShoptetAuthorizerNewRequest(self):
        """Test AppAuthorizerShoptetShoptetAuthorizerNewRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
