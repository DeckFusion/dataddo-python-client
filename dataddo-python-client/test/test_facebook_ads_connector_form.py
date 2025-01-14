# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.facebook_ads_connector_form import FacebookAdsConnectorForm

class TestFacebookAdsConnectorForm(unittest.TestCase):
    """FacebookAdsConnectorForm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FacebookAdsConnectorForm:
        """Test FacebookAdsConnectorForm
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FacebookAdsConnectorForm`
        """
        model = FacebookAdsConnectorForm()
        if include_optional:
            return FacebookAdsConnectorForm(
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
                use_dataddo_hash = True,
                account_id = '',
                campaign_id = '',
                ad_set_id = '',
                time_breakup = 'all_days',
                level = 'campaign',
                metric = ["clicks","actions.like"],
                breakdown = ["publisher_platform"],
                data_label = ["campaign_id","campaign_name"]
            )
        else:
            return FacebookAdsConnectorForm(
                connector_id = 'json',
                template_id = 'index',
                storage_strategy = 'clean',
                label = 'My Source Label',
                o_auth_id = '1234',
                date_range = '{{1d1}}',
                account_id = '',
                time_breakup = 'all_days',
                level = 'campaign',
                metric = ["clicks","actions.like"],
                data_label = ["campaign_id","campaign_name"],
        )
        """

    def testFacebookAdsConnectorForm(self):
        """Test FacebookAdsConnectorForm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
