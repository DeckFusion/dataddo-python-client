# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.databricks_storage_request import DatabricksStorageRequest

class TestDatabricksStorageRequest(unittest.TestCase):
    """DatabricksStorageRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatabricksStorageRequest:
        """Test DatabricksStorageRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatabricksStorageRequest`
        """
        model = DatabricksStorageRequest()
        if include_optional:
            return DatabricksStorageRequest(
                label = '',
                type = '',
                o_auth_id = 56
            )
        else:
            return DatabricksStorageRequest(
        )
        """

    def testDatabricksStorageRequest(self):
        """Test DatabricksStorageRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()