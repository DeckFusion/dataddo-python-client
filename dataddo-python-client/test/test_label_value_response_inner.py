# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.label_value_response_inner import LabelValueResponseInner

class TestLabelValueResponseInner(unittest.TestCase):
    """LabelValueResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LabelValueResponseInner:
        """Test LabelValueResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LabelValueResponseInner`
        """
        model = LabelValueResponseInner()
        if include_optional:
            return LabelValueResponseInner(
                label = '',
                value = ''
            )
        else:
            return LabelValueResponseInner(
        )
        """

    def testLabelValueResponseInner(self):
        """Test LabelValueResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()