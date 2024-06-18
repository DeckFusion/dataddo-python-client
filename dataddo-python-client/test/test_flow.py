# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.flow import Flow

class TestFlow(unittest.TestCase):
    """Flow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Flow:
        """Test Flow
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Flow`
        """
        model = Flow()
        if include_optional:
            return Flow(
                id = '',
                label = None,
                user_id = None,
                customer_id = None,
                source = [
                    openapi_client.models.flow_source.FlowSource(
                        source_id = null, )
                    ],
                tag = [
                    ''
                    ],
                operation = [
                    openapi_client.models.flow_operation.FlowOperation(
                        name = '', 
                        output = '', 
                        union = null, 
                        left_join = null, 
                        inner_join = null, 
                        view = null, 
                        filter = null, 
                        limit = null, 
                        format = null, 
                        sort = null, )
                    ],
                rules = [
                    openapi_client.models.flow_data_quality_rule.FlowDataQualityRule(
                        column_id = '', 
                        rule = '', 
                        action = '', )
                    ],
                api = None,
                write_action = None
            )
        else:
            return Flow(
        )
        """

    def testFlow(self):
        """Test Flow"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
