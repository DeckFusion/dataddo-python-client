# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.action_enqueued_dto import ActionEnqueuedDto

class TestActionEnqueuedDto(unittest.TestCase):
    """ActionEnqueuedDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActionEnqueuedDto:
        """Test ActionEnqueuedDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActionEnqueuedDto`
        """
        model = ActionEnqueuedDto()
        if include_optional:
            return ActionEnqueuedDto(
                execution_id = '',
                action_id = '',
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                action_type = None,
                connector = ''
            )
        else:
            return ActionEnqueuedDto(
        )
        """

    def testActionEnqueuedDto(self):
        """Test ActionEnqueuedDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()