# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.app_authorizer_facebook_custom_facebook_custom_authorizer_new_o_auth_callback_request import AppAuthorizerFacebookCustomFacebookCustomAuthorizerNewOAuthCallbackRequest

class TestAppAuthorizerFacebookCustomFacebookCustomAuthorizerNewOAuthCallbackRequest(unittest.TestCase):
    """AppAuthorizerFacebookCustomFacebookCustomAuthorizerNewOAuthCallbackRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppAuthorizerFacebookCustomFacebookCustomAuthorizerNewOAuthCallbackRequest:
        """Test AppAuthorizerFacebookCustomFacebookCustomAuthorizerNewOAuthCallbackRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppAuthorizerFacebookCustomFacebookCustomAuthorizerNewOAuthCallbackRequest`
        """
        model = AppAuthorizerFacebookCustomFacebookCustomAuthorizerNewOAuthCallbackRequest()
        if include_optional:
            return AppAuthorizerFacebookCustomFacebookCustomAuthorizerNewOAuthCallbackRequest(
                callback_url = 'https://my.app.com/callback?code=aaaaBBBBccc1234',
                config = openapi_client.models.facebook_custom_dto_authorizer.FacebookCustomDtoAuthorizer(
                    label = '', 
                    client_id = '', 
                    client_secret = '', 
                    redirect_uri = '', )
            )
        else:
            return AppAuthorizerFacebookCustomFacebookCustomAuthorizerNewOAuthCallbackRequest(
        )
        """

    def testAppAuthorizerFacebookCustomFacebookCustomAuthorizerNewOAuthCallbackRequest(self):
        """Test AppAuthorizerFacebookCustomFacebookCustomAuthorizerNewOAuthCallbackRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()