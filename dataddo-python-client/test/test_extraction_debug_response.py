# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.extraction_debug_response import ExtractionDebugResponse

class TestExtractionDebugResponse(unittest.TestCase):
    """ExtractionDebugResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExtractionDebugResponse:
        """Test ExtractionDebugResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExtractionDebugResponse`
        """
        model = ExtractionDebugResponse()
        if include_optional:
            return ExtractionDebugResponse(
                status = '',
                message = '',
                started = 1.337,
                ended = 1.337,
                duration = '',
                memory_mb = 56,
                logs = [
                    null
                    ],
                row_count = 56,
                blob = ''
            )
        else:
            return ExtractionDebugResponse(
        )
        """

    def testExtractionDebugResponse(self):
        """Test ExtractionDebugResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
