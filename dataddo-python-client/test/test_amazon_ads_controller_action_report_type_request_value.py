# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.amazon_ads_controller_action_report_type_request_value import AmazonAdsControllerActionReportTypeRequestValue

class TestAmazonAdsControllerActionReportTypeRequestValue(unittest.TestCase):
    """AmazonAdsControllerActionReportTypeRequestValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AmazonAdsControllerActionReportTypeRequestValue:
        """Test AmazonAdsControllerActionReportTypeRequestValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AmazonAdsControllerActionReportTypeRequestValue`
        """
        model = AmazonAdsControllerActionReportTypeRequestValue()
        if include_optional:
            return AmazonAdsControllerActionReportTypeRequestValue(
                ad_product = ''
            )
        else:
            return AmazonAdsControllerActionReportTypeRequestValue(
        )
        """

    def testAmazonAdsControllerActionReportTypeRequestValue(self):
        """Test AmazonAdsControllerActionReportTypeRequestValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
