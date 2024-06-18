# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.panoply_destination import PanoplyDestination

class TestPanoplyDestination(unittest.TestCase):
    """PanoplyDestination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PanoplyDestination:
        """Test PanoplyDestination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PanoplyDestination`
        """
        model = PanoplyDestination()
        if include_optional:
            return PanoplyDestination(
                id = '',
                customer_id = '',
                created_at = 56,
                updated_at = 56,
                last_use = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                label = '',
                description = '',
                status = True,
                status_detail = '',
                o_auth_id = 56,
                project_id = '',
                dataset_id = ''
            )
        else:
            return PanoplyDestination(
        )
        """

    def testPanoplyDestination(self):
        """Test PanoplyDestination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
