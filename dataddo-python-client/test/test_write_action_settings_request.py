# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.write_action_settings_request import WriteActionSettingsRequest

class TestWriteActionSettingsRequest(unittest.TestCase):
    """WriteActionSettingsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WriteActionSettingsRequest:
        """Test WriteActionSettingsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WriteActionSettingsRequest`
        """
        model = WriteActionSettingsRequest()
        if include_optional:
            return WriteActionSettingsRequest(
                write_mode = '',
                unique_columns = [
                    ''
                    ]
            )
        else:
            return WriteActionSettingsRequest(
        )
        """

    def testWriteActionSettingsRequest(self):
        """Test WriteActionSettingsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()