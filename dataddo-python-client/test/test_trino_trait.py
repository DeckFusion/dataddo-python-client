# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.trino_trait import TrinoTrait

class TestTrinoTrait(unittest.TestCase):
    """TrinoTrait unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrinoTrait:
        """Test TrinoTrait
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrinoTrait`
        """
        model = TrinoTrait()
        if include_optional:
            return TrinoTrait(
                host = '',
                port = 56,
                user = '',
                var_schema = '',
                catalog = ''
            )
        else:
            return TrinoTrait(
        )
        """

    def testTrinoTrait(self):
        """Test TrinoTrait"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()