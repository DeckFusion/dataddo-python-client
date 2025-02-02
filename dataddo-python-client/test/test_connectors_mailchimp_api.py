# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.connectors_mailchimp_api import ConnectorsMailchimpApi


class TestConnectorsMailchimpApi(unittest.TestCase):
    """ConnectorsMailchimpApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConnectorsMailchimpApi()

    def tearDown(self) -> None:
        pass

    def test_mailchimp_controller_action_authorization(self) -> None:
        """Test case for mailchimp_controller_action_authorization

        List of authorization objects
        """
        pass

    def test_mailchimp_controller_action_dc(self) -> None:
        """Test case for mailchimp_controller_action_dc

        List of data centers
        """
        pass

    def test_mailchimp_controller_action_list(self) -> None:
        """Test case for mailchimp_controller_action_list

        List of contacts
        """
        pass

    def test_mailchimp_controller_action_load(self) -> None:
        """Test case for mailchimp_controller_action_load

        Create Mailchimp User source
        """
        pass

    def test_mailchimp_controller_action_preview(self) -> None:
        """Test case for mailchimp_controller_action_preview

        Preview the data
        """
        pass

    def test_mailchimp_controller_action_template(self) -> None:
        """Test case for mailchimp_controller_action_template

        List details of dataset template
        """
        pass

    def test_mailchimp_controller_action_templates(self) -> None:
        """Test case for mailchimp_controller_action_templates

        List all Mailchimp dataset templates
        """
        pass


if __name__ == '__main__':
    unittest.main()
