# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.app_destination_google_sheets_google_sheets_destination_action_available_spreadsheets_request import AppDestinationGoogleSheetsGoogleSheetsDestinationActionAvailableSpreadsheetsRequest

class TestAppDestinationGoogleSheetsGoogleSheetsDestinationActionAvailableSpreadsheetsRequest(unittest.TestCase):
    """AppDestinationGoogleSheetsGoogleSheetsDestinationActionAvailableSpreadsheetsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppDestinationGoogleSheetsGoogleSheetsDestinationActionAvailableSpreadsheetsRequest:
        """Test AppDestinationGoogleSheetsGoogleSheetsDestinationActionAvailableSpreadsheetsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppDestinationGoogleSheetsGoogleSheetsDestinationActionAvailableSpreadsheetsRequest`
        """
        model = AppDestinationGoogleSheetsGoogleSheetsDestinationActionAvailableSpreadsheetsRequest()
        if include_optional:
            return AppDestinationGoogleSheetsGoogleSheetsDestinationActionAvailableSpreadsheetsRequest(
                destination_id = '1'
            )
        else:
            return AppDestinationGoogleSheetsGoogleSheetsDestinationActionAvailableSpreadsheetsRequest(
        )
        """

    def testAppDestinationGoogleSheetsGoogleSheetsDestinationActionAvailableSpreadsheetsRequest(self):
        """Test AppDestinationGoogleSheetsGoogleSheetsDestinationActionAvailableSpreadsheetsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
