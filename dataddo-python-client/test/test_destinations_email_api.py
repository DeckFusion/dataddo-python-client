# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.destinations_email_api import DestinationsEmailApi


class TestDestinationsEmailApi(unittest.TestCase):
    """DestinationsEmailApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DestinationsEmailApi()

    def tearDown(self) -> None:
        pass

    def test_app_destination_email_email_destination_action_attachment_formats(self) -> None:
        """Test case for app_destination_email_email_destination_action_attachment_formats

        List email attachment formats
        """
        pass

    def test_app_destination_email_email_destination_action_write_modes(self) -> None:
        """Test case for app_destination_email_email_destination_action_write_modes

        List of write modes
        """
        pass


if __name__ == '__main__':
    unittest.main()
