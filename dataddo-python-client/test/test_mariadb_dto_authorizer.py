# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.mariadb_dto_authorizer import MariadbDtoAuthorizer

class TestMariadbDtoAuthorizer(unittest.TestCase):
    """MariadbDtoAuthorizer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MariadbDtoAuthorizer:
        """Test MariadbDtoAuthorizer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MariadbDtoAuthorizer`
        """
        model = MariadbDtoAuthorizer()
        if include_optional:
            return MariadbDtoAuthorizer(
                host = '',
                port = 56,
                username = '',
                database = '',
                ssh_config = None,
                ssl = '',
                tls = '',
                use_ssh = True,
                certificate_id = '',
                ssh_host = '',
                ssh_port = 56,
                ssh_remote_host = '',
                ssh_remote_port = 56,
                ssh_username = '',
                ssh_password = '',
                password = '',
                label = ''
            )
        else:
            return MariadbDtoAuthorizer(
        )
        """

    def testMariadbDtoAuthorizer(self):
        """Test MariadbDtoAuthorizer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
