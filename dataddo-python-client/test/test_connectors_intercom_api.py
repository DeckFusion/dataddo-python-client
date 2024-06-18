# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.connectors_intercom_api import ConnectorsIntercomApi


class TestConnectorsIntercomApi(unittest.TestCase):
    """ConnectorsIntercomApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConnectorsIntercomApi()

    def tearDown(self) -> None:
        pass

    def test_app_connector_intercom_intercom_connector_action_authorization(self) -> None:
        """Test case for app_connector_intercom_intercom_connector_action_authorization

        List of authorization objects
        """
        pass

    def test_app_connector_intercom_intercom_connector_action_date_range(self) -> None:
        """Test case for app_connector_intercom_intercom_connector_action_date_range

        Method for listing date range
        """
        pass

    def test_app_connector_intercom_intercom_connector_create_source(self) -> None:
        """Test case for app_connector_intercom_intercom_connector_create_source

        Create Intercom source
        """
        pass

    def test_app_connector_intercom_intercom_connector_preview(self) -> None:
        """Test case for app_connector_intercom_intercom_connector_preview

        Data preview
        """
        pass


if __name__ == '__main__':
    unittest.main()