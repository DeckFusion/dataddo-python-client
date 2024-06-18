# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.source_dto import SourceDTO

class TestSourceDTO(unittest.TestCase):
    """SourceDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SourceDTO:
        """Test SourceDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SourceDTO`
        """
        model = SourceDTO()
        if include_optional:
            return SourceDTO(
                source = openapi_client.models.source.Source(
                    id = '', 
                    label = '', 
                    description = '', 
                    type = '', 
                    customer_id = '', 
                    created = 56, ),
                storage = openapi_client.models.storage_source_meta.StorageSourceMeta(
                    id = '', 
                    updated_at = '', 
                    engine = openapi_client.models.source_engine_dto.SourceEngineDTO(
                        name = '', 
                        region = '', 
                        encryption_key = '', ), 
                    metadata = openapi_client.models.source_metadata_dto.SourceMetadataDTO(
                        last_bin_log_file = '', 
                        last_position = 56, 
                        last_processed_timestamp = 56, ), 
                    columns = [
                        openapi_client.models.source_column_dto.SourceColumnDTO(
                            column_id = '', 
                            label = '', 
                            hash = '', 
                            size = 56, 
                            type = '', )
                        ], ),
                engine = openapi_client.models.source_engine_dto.SourceEngineDTO(
                    name = '', 
                    region = '', 
                    encryption_key = '', ),
                column = [
                    openapi_client.models.source_column_dto.SourceColumnDTO(
                        column_id = '', 
                        label = '', 
                        hash = '', 
                        size = 56, 
                        type = '', )
                    ],
                id = '',
                customer_id = '',
                label = '',
                description = '',
                type = '',
                created = 56,
                template_id = '',
                connector_id = ''
            )
        else:
            return SourceDTO(
        )
        """

    def testSourceDTO(self):
        """Test SourceDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
