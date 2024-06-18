# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.flow_operation_join import FlowOperationJoin

class TestFlowOperationJoin(unittest.TestCase):
    """FlowOperationJoin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FlowOperationJoin:
        """Test FlowOperationJoin
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FlowOperationJoin`
        """
        model = FlowOperationJoin()
        if include_optional:
            return FlowOperationJoin(
                source = '',
                target = '',
                conditions = [
                    openapi_client.models.flow_operation_join_condition.FlowOperationJoinCondition(
                        source_column = '', 
                        target_column = '', )
                    ],
                columns = [
                    openapi_client.models.flow_operation_column.FlowOperationColumn(
                        source = '', 
                        column = '', 
                        as = '', )
                    ]
            )
        else:
            return FlowOperationJoin(
        )
        """

    def testFlowOperationJoin(self):
        """Test FlowOperationJoin"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
