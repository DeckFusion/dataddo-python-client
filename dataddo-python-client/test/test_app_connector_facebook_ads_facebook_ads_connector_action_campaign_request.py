# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.app_connector_facebook_ads_facebook_ads_connector_action_campaign_request import AppConnectorFacebookAdsFacebookAdsConnectorActionCampaignRequest

class TestAppConnectorFacebookAdsFacebookAdsConnectorActionCampaignRequest(unittest.TestCase):
    """AppConnectorFacebookAdsFacebookAdsConnectorActionCampaignRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppConnectorFacebookAdsFacebookAdsConnectorActionCampaignRequest:
        """Test AppConnectorFacebookAdsFacebookAdsConnectorActionCampaignRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppConnectorFacebookAdsFacebookAdsConnectorActionCampaignRequest`
        """
        model = AppConnectorFacebookAdsFacebookAdsConnectorActionCampaignRequest()
        if include_optional:
            return AppConnectorFacebookAdsFacebookAdsConnectorActionCampaignRequest(
                o_auth_id = '0',
                account_id = 'act_00000000'
            )
        else:
            return AppConnectorFacebookAdsFacebookAdsConnectorActionCampaignRequest(
        )
        """

    def testAppConnectorFacebookAdsFacebookAdsConnectorActionCampaignRequest(self):
        """Test AppConnectorFacebookAdsFacebookAdsConnectorActionCampaignRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()