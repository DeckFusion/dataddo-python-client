# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.pinterest_connector_form import PinterestConnectorForm

class TestPinterestConnectorForm(unittest.TestCase):
    """PinterestConnectorForm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PinterestConnectorForm:
        """Test PinterestConnectorForm
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PinterestConnectorForm`
        """
        model = PinterestConnectorForm()
        if include_optional:
            return PinterestConnectorForm(
                ensure_data_types = {"field1":"string","field2":"integer","field3":"date","field4":"float"},
                allow_empty = True,
                nullable_fields = True,
                connector_id = 'json',
                template_id = 'index',
                strategy = 'clean',
                storage_strategy = 'clean',
                label = 'My Source Label',
                o_auth_id = '1234',
                date_range = '{{1d1}}',
                report_level = 'Account',
                ad_account_ids = [
                    56
                    ],
                column = ["Total Conversions","CTR"],
                data_label = ["Ad Account ID","Campaign Name"],
                engagement_window_days = '1',
                view_window_days = '1',
                conversion_report_time = 'TIME_OF_AD_ACTION',
                granularity = 'DAY',
                click_window_days = '60'
            )
        else:
            return PinterestConnectorForm(
                connector_id = 'json',
                template_id = 'index',
                storage_strategy = 'clean',
        )
        """

    def testPinterestConnectorForm(self):
        """Test PinterestConnectorForm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()