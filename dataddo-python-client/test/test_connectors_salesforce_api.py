# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.connectors_salesforce_api import ConnectorsSalesforceApi


class TestConnectorsSalesforceApi(unittest.TestCase):
    """ConnectorsSalesforceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConnectorsSalesforceApi()

    def tearDown(self) -> None:
        pass

    def test_salesforce_controller_action_api_version(self) -> None:
        """Test case for salesforce_controller_action_api_version

        List available API versions
        """
        pass

    def test_salesforce_controller_action_attribute(self) -> None:
        """Test case for salesforce_controller_action_attribute

        Gets all available data extensions attributes
        """
        pass

    def test_salesforce_controller_action_authorization(self) -> None:
        """Test case for salesforce_controller_action_authorization

        List of authorization objects
        """
        pass

    def test_salesforce_controller_action_instance(self) -> None:
        """Test case for salesforce_controller_action_instance

        List all available instance It is possible to use centralized authentication server (login.salesforce.com) even if custom domain is used
        """
        pass

    def test_salesforce_controller_action_load(self) -> None:
        """Test case for salesforce_controller_action_load

        Create Salesforce source
        """
        pass

    def test_salesforce_controller_action_object(self) -> None:
        """Test case for salesforce_controller_action_object

        Gets all Marketing cloud data extensions
        """
        pass

    def test_salesforce_controller_action_preview(self) -> None:
        """Test case for salesforce_controller_action_preview

        Preview the data
        """
        pass


if __name__ == '__main__':
    unittest.main()
