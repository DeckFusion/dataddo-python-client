# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.source_column_dto import SourceColumnDTO
from openapi_client.models.source_engine_dto import SourceEngineDTO
from openapi_client.models.source_metadata_dto import SourceMetadataDTO
from typing import Optional, Set
from typing_extensions import Self

class StorageSourceMeta(BaseModel):
    """
    StorageSourceMeta
    """ # noqa: E501
    id: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = Field(default=None, description="When the source was updated for the last time", alias="updatedAt")
    engine: Optional[SourceEngineDTO] = None
    metadata: Optional[SourceMetadataDTO] = None
    columns: Optional[List[SourceColumnDTO]] = None
    __properties: ClassVar[List[str]] = ["id", "updatedAt", "engine", "metadata", "columns"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of StorageSourceMeta from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of engine
        if self.engine:
            _dict['engine'] = self.engine.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in columns (list)
        _items = []
        if self.columns:
            for _item in self.columns:
                if _item:
                    _items.append(_item.to_dict())
            _dict['columns'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StorageSourceMeta from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "updatedAt": obj.get("updatedAt"),
            "engine": SourceEngineDTO.from_dict(obj["engine"]) if obj.get("engine") is not None else None,
            "metadata": SourceMetadataDTO.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "columns": [SourceColumnDTO.from_dict(_item) for _item in obj["columns"]] if obj.get("columns") is not None else None
        })
        return _obj

