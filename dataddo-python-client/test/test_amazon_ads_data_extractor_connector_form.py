# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.amazon_ads_data_extractor_connector_form import AmazonAdsDataExtractorConnectorForm

class TestAmazonAdsDataExtractorConnectorForm(unittest.TestCase):
    """AmazonAdsDataExtractorConnectorForm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AmazonAdsDataExtractorConnectorForm:
        """Test AmazonAdsDataExtractorConnectorForm
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AmazonAdsDataExtractorConnectorForm`
        """
        model = AmazonAdsDataExtractorConnectorForm()
        if include_optional:
            return AmazonAdsDataExtractorConnectorForm(
                ensure_data_types = {"field1":"string","field2":"integer","field3":"date","field4":"float"},
                allow_empty = True,
                nullable_fields = True,
                connector_id = 'json',
                template_id = 'index',
                strategy = 'clean',
                storage_strategy = 'clean',
                label = 'My Source Label',
                flow = '',
                token = ''
            )
        else:
            return AmazonAdsDataExtractorConnectorForm(
                connector_id = 'json',
                template_id = 'index',
                storage_strategy = 'clean',
                label = 'My Source Label',
                flow = '',
                token = '',
        )
        """

    def testAmazonAdsDataExtractorConnectorForm(self):
        """Test AmazonAdsDataExtractorConnectorForm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
