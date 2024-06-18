# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.connectors_mssql_api import ConnectorsMssqlApi


class TestConnectorsMssqlApi(unittest.TestCase):
    """ConnectorsMssqlApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConnectorsMssqlApi()

    def tearDown(self) -> None:
        pass

    def test_app_connector_mssql_mssql_connector_action_authorization(self) -> None:
        """Test case for app_connector_mssql_mssql_connector_action_authorization

        List of authorization objects
        """
        pass

    def test_app_connector_mssql_mssql_connector_action_generate_sql_queries(self) -> None:
        """Test case for app_connector_mssql_mssql_connector_action_generate_sql_queries

        Get generated SQL queries
        """
        pass

    def test_app_connector_mssql_mssql_connector_action_list_columns(self) -> None:
        """Test case for app_connector_mssql_mssql_connector_action_list_columns

        List of table columns
        """
        pass

    def test_app_connector_mssql_mssql_connector_action_list_tables(self) -> None:
        """Test case for app_connector_mssql_mssql_connector_action_list_tables

        List of database tables
        """
        pass

    def test_app_connector_mssql_mssql_connector_action_sql(self) -> None:
        """Test case for app_connector_mssql_mssql_connector_action_sql

        Get generated SQL
        """
        pass

    def test_app_connector_mssql_mssql_connector_create_source(self) -> None:
        """Test case for app_connector_mssql_mssql_connector_create_source

        Create Mssql source
        """
        pass

    def test_app_connector_mssql_mssql_connector_preview(self) -> None:
        """Test case for app_connector_mssql_mssql_connector_preview

        Data preview
        """
        pass


if __name__ == '__main__':
    unittest.main()