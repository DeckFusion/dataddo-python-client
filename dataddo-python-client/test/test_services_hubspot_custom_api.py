# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.services_hubspot_custom_api import ServicesHubspotCustomApi


class TestServicesHubspotCustomApi(unittest.TestCase):
    """ServicesHubspotCustomApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ServicesHubspotCustomApi()

    def tearDown(self) -> None:
        pass

    def test_app_authorizer_hubspot_custom_hubspot_custom_authorizer_get_authorization_url(self) -> None:
        """Test case for app_authorizer_hubspot_custom_hubspot_custom_authorizer_get_authorization_url

        Builds redirect URL
        """
        pass

    def test_app_authorizer_hubspot_custom_hubspot_custom_authorizer_new_o_auth_callback(self) -> None:
        """Test case for app_authorizer_hubspot_custom_hubspot_custom_authorizer_new_o_auth_callback

        Processes callback URL
        """
        pass


if __name__ == '__main__':
    unittest.main()
