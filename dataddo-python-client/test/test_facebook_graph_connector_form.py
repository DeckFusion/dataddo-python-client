# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.facebook_graph_connector_form import FacebookGraphConnectorForm

class TestFacebookGraphConnectorForm(unittest.TestCase):
    """FacebookGraphConnectorForm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FacebookGraphConnectorForm:
        """Test FacebookGraphConnectorForm
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FacebookGraphConnectorForm`
        """
        model = FacebookGraphConnectorForm()
        if include_optional:
            return FacebookGraphConnectorForm(
                ensure_data_types = {"field1":"string","field2":"integer","field3":"date","field4":"float"},
                allow_empty = True,
                nullable_fields = True,
                connector_id = 'json',
                template_id = 'index',
                strategy = 'clean',
                storage_strategy = 'clean',
                label = 'My Source Label',
                o_auth_id = '1234',
                url = 'https://www.dataddo.com',
                method = 'GET',
                headers = {"Accept":"application/json"},
                body = '',
                transformation = '',
                emitter = '',
                parameters = {"parameter":"value"},
                attributes = ["field1","field2","fields3"],
                cursor = ''
            )
        else:
            return FacebookGraphConnectorForm(
                connector_id = 'json',
                template_id = 'index',
                storage_strategy = 'clean',
                label = 'My Source Label',
                o_auth_id = '1234',
                url = 'https://www.dataddo.com',
                method = 'GET',
                transformation = '',
                attributes = ["field1","field2","fields3"],
        )
        """

    def testFacebookGraphConnectorForm(self):
        """Test FacebookGraphConnectorForm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()