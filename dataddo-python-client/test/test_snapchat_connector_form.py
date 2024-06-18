# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.snapchat_connector_form import SnapchatConnectorForm

class TestSnapchatConnectorForm(unittest.TestCase):
    """SnapchatConnectorForm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SnapchatConnectorForm:
        """Test SnapchatConnectorForm
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SnapchatConnectorForm`
        """
        model = SnapchatConnectorForm()
        if include_optional:
            return SnapchatConnectorForm(
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
                organization_id = '12345',
                account_id = '12345',
                metrics = ["Impressions","Spend"],
                labels = ["Stats ID","Report ID"],
                breakdown = 'campaign',
                action_report_time = 'conversion',
                swipe_up_attribution_window = '1_DAY',
                view_attribution_window = '1_DAY'
            )
        else:
            return SnapchatConnectorForm(
                connector_id = 'json',
                template_id = 'index',
                storage_strategy = 'clean',
                label = 'My Source Label',
                o_auth_id = '1234',
                date_range = '{{1d1}}',
                organization_id = '12345',
                account_id = '12345',
                metrics = ["Impressions","Spend"],
                labels = ["Stats ID","Report ID"],
                breakdown = 'campaign',
                action_report_time = 'conversion',
                swipe_up_attribution_window = '1_DAY',
                view_attribution_window = '1_DAY',
        )
        """

    def testSnapchatConnectorForm(self):
        """Test SnapchatConnectorForm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
