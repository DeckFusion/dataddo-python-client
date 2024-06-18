# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.destinations_alloy_db_api import DestinationsAlloyDbApi


class TestDestinationsAlloyDbApi(unittest.TestCase):
    """DestinationsAlloyDbApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DestinationsAlloyDbApi()

    def tearDown(self) -> None:
        pass

    def test_app_destination_alloy_db_alloy_db_destination_action_authorization(self) -> None:
        """Test case for app_destination_alloy_db_alloy_db_destination_action_authorization

        List of authorization objects
        """
        pass

    def test_app_destination_alloy_db_alloy_db_destination_action_ssl(self) -> None:
        """Test case for app_destination_alloy_db_alloy_db_destination_action_ssl

        List of SSL options
        """
        pass

    def test_app_destination_alloy_db_alloy_db_destination_action_write_modes(self) -> None:
        """Test case for app_destination_alloy_db_alloy_db_destination_action_write_modes

        List of write modes
        """
        pass

    def test_app_destination_alloy_db_alloy_db_destination_create(self) -> None:
        """Test case for app_destination_alloy_db_alloy_db_destination_create

        Create destination
        """
        pass


if __name__ == '__main__':
    unittest.main()