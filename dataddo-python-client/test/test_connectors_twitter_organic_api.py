# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.connectors_twitter_organic_api import ConnectorsTwitterOrganicApi


class TestConnectorsTwitterOrganicApi(unittest.TestCase):
    """ConnectorsTwitterOrganicApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConnectorsTwitterOrganicApi()

    def tearDown(self) -> None:
        pass

    def test_twitter_organic_controller_action_authorization(self) -> None:
        """Test case for twitter_organic_controller_action_authorization

        List of authorization objects
        """
        pass

    def test_twitter_organic_controller_action_date_range(self) -> None:
        """Test case for twitter_organic_controller_action_date_range

        List of date ranges
        """
        pass

    def test_twitter_organic_controller_action_load(self) -> None:
        """Test case for twitter_organic_controller_action_load

        Create Twitter Organic source
        """
        pass

    def test_twitter_organic_controller_action_preview(self) -> None:
        """Test case for twitter_organic_controller_action_preview

        Preview the data
        """
        pass

    def test_twitter_organic_controller_action_profile(self) -> None:
        """Test case for twitter_organic_controller_action_profile

        List of all Twitter profiles
        """
        pass

    def test_twitter_organic_controller_action_template(self) -> None:
        """Test case for twitter_organic_controller_action_template

        List details of dataset template
        """
        pass

    def test_twitter_organic_controller_action_templates(self) -> None:
        """Test case for twitter_organic_controller_action_templates

        List all Twitter Organic dataset templates
        """
        pass


if __name__ == '__main__':
    unittest.main()
