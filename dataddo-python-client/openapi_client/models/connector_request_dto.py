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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ConnectorRequestDto(BaseModel):
    """
    ConnectorRequestDto
    """ # noqa: E501
    method: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    headers: Optional[List[StrictStr]] = None
    transformation: Optional[StrictStr] = None
    body: Optional[StrictStr] = None
    ensure_data_types: Optional[List[StrictStr]] = Field(default=None, alias="ensureDataTypes")
    emitter: Optional[StrictStr] = None
    emit_only: Optional[StrictBool] = Field(default=None, alias="emitOnly")
    format: Optional[StrictStr] = None
    timeout: Optional[StrictInt] = None
    sleep_time_millisecond: Optional[StrictInt] = Field(default=None, alias="sleepTimeMillisecond")
    o_auth_id: Optional[StrictInt] = Field(default=None, alias="oAuthId")
    __properties: ClassVar[List[str]] = ["method", "url", "headers", "transformation", "body", "ensureDataTypes", "emitter", "emitOnly", "format", "timeout", "sleepTimeMillisecond", "oAuthId"]

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
        """Create an instance of ConnectorRequestDto from a JSON string"""
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
        # set to None if emitter (nullable) is None
        # and model_fields_set contains the field
        if self.emitter is None and "emitter" in self.model_fields_set:
            _dict['emitter'] = None

        # set to None if o_auth_id (nullable) is None
        # and model_fields_set contains the field
        if self.o_auth_id is None and "o_auth_id" in self.model_fields_set:
            _dict['oAuthId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConnectorRequestDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "method": obj.get("method"),
            "url": obj.get("url"),
            "headers": obj.get("headers"),
            "transformation": obj.get("transformation"),
            "body": obj.get("body"),
            "ensureDataTypes": obj.get("ensureDataTypes"),
            "emitter": obj.get("emitter"),
            "emitOnly": obj.get("emitOnly"),
            "format": obj.get("format"),
            "timeout": obj.get("timeout"),
            "sleepTimeMillisecond": obj.get("sleepTimeMillisecond"),
            "oAuthId": obj.get("oAuthId")
        })
        return _obj


