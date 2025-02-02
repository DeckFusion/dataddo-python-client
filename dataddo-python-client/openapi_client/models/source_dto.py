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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.source import Source
from openapi_client.models.source_column_dto import SourceColumnDTO
from openapi_client.models.source_engine_dto import SourceEngineDTO
from openapi_client.models.storage_source_meta import StorageSourceMeta
from typing import Optional, Set
from typing_extensions import Self

class SourceDTO(BaseModel):
    """
    SourceDTO
    """ # noqa: E501
    source: Optional[Source] = None
    storage: Optional[StorageSourceMeta] = None
    engine: Optional[SourceEngineDTO] = None
    column: Optional[List[SourceColumnDTO]] = None
    id: Optional[StrictStr] = None
    customer_id: Optional[StrictStr] = None
    label: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    created: Optional[StrictInt] = Field(default=None, description="Timestamp")
    template_id: Optional[StrictStr] = None
    connector_id: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["source", "storage", "engine", "column", "id", "customer_id", "label", "description", "type", "created", "template_id", "connector_id"]

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
        """Create an instance of SourceDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of storage
        if self.storage:
            _dict['storage'] = self.storage.to_dict()
        # override the default output from pydantic by calling `to_dict()` of engine
        if self.engine:
            _dict['engine'] = self.engine.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in column (list)
        _items = []
        if self.column:
            for _item in self.column:
                if _item:
                    _items.append(_item.to_dict())
            _dict['column'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SourceDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "source": Source.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "storage": StorageSourceMeta.from_dict(obj["storage"]) if obj.get("storage") is not None else None,
            "engine": SourceEngineDTO.from_dict(obj["engine"]) if obj.get("engine") is not None else None,
            "column": [SourceColumnDTO.from_dict(_item) for _item in obj["column"]] if obj.get("column") is not None else None,
            "id": obj.get("id"),
            "customer_id": obj.get("customer_id"),
            "label": obj.get("label"),
            "description": obj.get("description"),
            "type": obj.get("type"),
            "created": obj.get("created"),
            "template_id": obj.get("template_id"),
            "connector_id": obj.get("connector_id")
        })
        return _obj


