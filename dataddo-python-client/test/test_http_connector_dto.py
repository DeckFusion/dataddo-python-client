# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.http_connector_dto import HttpConnectorDto

class TestHttpConnectorDto(unittest.TestCase):
    """HttpConnectorDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HttpConnectorDto:
        """Test HttpConnectorDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HttpConnectorDto`
        """
        model = HttpConnectorDto()
        if include_optional:
            return HttpConnectorDto(
                connector_id = '',
                template_id = '',
                label = '',
                storage_strategy = 'incremental',
                allow_empty = True,
                request = None
            )
        else:
            return HttpConnectorDto(
        )
        """

    def testHttpConnectorDto(self):
        """Test HttpConnectorDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
