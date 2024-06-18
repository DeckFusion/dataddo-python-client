# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.join_request import JoinRequest

class TestJoinRequest(unittest.TestCase):
    """JoinRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JoinRequest:
        """Test JoinRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JoinRequest`
        """
        model = JoinRequest()
        if include_optional:
            return JoinRequest(
                source = '',
                target = '',
                conditions = [
                    openapi_client.models.join_condition_request.JoinConditionRequest(
                        source_column = '', 
                        target_column = '', )
                    ],
                columns = [
                    openapi_client.models.join_column_request.JoinColumnRequest(
                        source = '', 
                        column = '', 
                        as = '', )
                    ]
            )
        else:
            return JoinRequest(
        )
        """

    def testJoinRequest(self):
        """Test JoinRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()