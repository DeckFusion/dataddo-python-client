# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.schedule import Schedule

class TestSchedule(unittest.TestCase):
    """Schedule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Schedule:
        """Test Schedule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Schedule`
        """
        model = Schedule()
        if include_optional:
            return Schedule(
                timezone = '',
                minute = None,
                hour = None,
                day_of_month = None,
                month = None,
                day_of_week = None,
                sync_frequency = None
            )
        else:
            return Schedule(
        )
        """

    def testSchedule(self):
        """Test Schedule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
