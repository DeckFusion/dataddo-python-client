# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.api_debug_response import APIDebugResponse

class TestAPIDebugResponse(unittest.TestCase):
    """APIDebugResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> APIDebugResponse:
        """Test APIDebugResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `APIDebugResponse`
        """
        model = APIDebugResponse()
        if include_optional:
            return APIDebugResponse(
                status = '',
                message = '',
                started = 1.337,
                ended = 1.337,
                duration = '',
                memory_mb = 56,
                logs = [
                    null
                    ]
            )
        else:
            return APIDebugResponse(
        )
        """

    def testAPIDebugResponse(self):
        """Test APIDebugResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
