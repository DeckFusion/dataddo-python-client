# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.extraction_action import ExtractionAction

class TestExtractionAction(unittest.TestCase):
    """ExtractionAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExtractionAction:
        """Test ExtractionAction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExtractionAction`
        """
        model = ExtractionAction()
        if include_optional:
            return ExtractionAction(
                id = '',
                status = '',
                status_detail = '',
                duration = '',
                object_id = None,
                object_type = '',
                type = None,
                customer_id = '',
                last_execution = 56,
                next_execution = 56,
                error_count = 56,
                is_being_processed = True,
                on_error_retry_timeout = 56,
                schedule = None,
                storage = '',
                storage_strategy = ''
            )
        else:
            return ExtractionAction(
        )
        """

    def testExtractionAction(self):
        """Test ExtractionAction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
