# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.salesforce_controller_action_object_request import SalesforceControllerActionObjectRequest

class TestSalesforceControllerActionObjectRequest(unittest.TestCase):
    """SalesforceControllerActionObjectRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SalesforceControllerActionObjectRequest:
        """Test SalesforceControllerActionObjectRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SalesforceControllerActionObjectRequest`
        """
        model = SalesforceControllerActionObjectRequest()
        if include_optional:
            return SalesforceControllerActionObjectRequest(
                o_auth_id = '0',
                instance = 'example.my.salesforce.com',
                api_version = '31.0'
            )
        else:
            return SalesforceControllerActionObjectRequest(
        )
        """

    def testSalesforceControllerActionObjectRequest(self):
        """Test SalesforceControllerActionObjectRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
