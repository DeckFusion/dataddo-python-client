# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.writer_debug_response_all_of_connection_result import WriterDebugResponseAllOfConnectionResult

class TestWriterDebugResponseAllOfConnectionResult(unittest.TestCase):
    """WriterDebugResponseAllOfConnectionResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WriterDebugResponseAllOfConnectionResult:
        """Test WriterDebugResponseAllOfConnectionResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WriterDebugResponseAllOfConnectionResult`
        """
        model = WriterDebugResponseAllOfConnectionResult()
        if include_optional:
            return WriterDebugResponseAllOfConnectionResult(
                config = [
                    null
                    ],
                result = [
                    null
                    ]
            )
        else:
            return WriterDebugResponseAllOfConnectionResult(
        )
        """

    def testWriterDebugResponseAllOfConnectionResult(self):
        """Test WriterDebugResponseAllOfConnectionResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()