# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.aws_s3_storage_request import AwsS3StorageRequest

class TestAwsS3StorageRequest(unittest.TestCase):
    """AwsS3StorageRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AwsS3StorageRequest:
        """Test AwsS3StorageRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AwsS3StorageRequest`
        """
        model = AwsS3StorageRequest()
        if include_optional:
            return AwsS3StorageRequest(
                label = '',
                type = '',
                o_auth_id = 56,
                path = ''
            )
        else:
            return AwsS3StorageRequest(
        )
        """

    def testAwsS3StorageRequest(self):
        """Test AwsS3StorageRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()