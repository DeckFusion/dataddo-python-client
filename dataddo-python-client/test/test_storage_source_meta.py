# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.storage_source_meta import StorageSourceMeta

class TestStorageSourceMeta(unittest.TestCase):
    """StorageSourceMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StorageSourceMeta:
        """Test StorageSourceMeta
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StorageSourceMeta`
        """
        model = StorageSourceMeta()
        if include_optional:
            return StorageSourceMeta(
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
                    ]
            )
        else:
            return StorageSourceMeta(
        )
        """

    def testStorageSourceMeta(self):
        """Test StorageSourceMeta"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()