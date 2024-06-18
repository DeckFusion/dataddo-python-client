# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.amazon_ads_connector_form import AmazonAdsConnectorForm

class TestAmazonAdsConnectorForm(unittest.TestCase):
    """AmazonAdsConnectorForm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AmazonAdsConnectorForm:
        """Test AmazonAdsConnectorForm
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AmazonAdsConnectorForm`
        """
        model = AmazonAdsConnectorForm()
        if include_optional:
            return AmazonAdsConnectorForm(
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
                profile_id = '',
                ad_product = '',
                report_type = '',
                group_by = ["campaign","adGroup"],
                time_unit = '',
                tactic = '',
                column = ["page_impressions","page_impressions_unique"]
            )
        else:
            return AmazonAdsConnectorForm(
                connector_id = 'json',
                template_id = 'index',
                storage_strategy = 'clean',
                label = 'My Source Label',
                o_auth_id = '1234',
                date_range = '{{1d1}}',
                profile_id = '',
                ad_product = '',
                report_type = '',
                column = ["page_impressions","page_impressions_unique"],
        )
        """

    def testAmazonAdsConnectorForm(self):
        """Test AmazonAdsConnectorForm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
