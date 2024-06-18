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
from typing import Optional, Set
from typing_extensions import Self

class OneDriveStorageRequest(BaseModel):
    """
    OneDriveStorageRequest
    """ # noqa: E501
    label: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    o_auth_id: Optional[StrictInt] = None
    path: Optional[StrictStr] = None
    drive_id: Optional[StrictStr] = Field(default=None, alias="driveId")
    tenant: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["label", "type", "o_auth_id", "path", "driveId", "tenant"]

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
        """Create an instance of OneDriveStorageRequest from a JSON string"""
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
        # set to None if path (nullable) is None
        # and model_fields_set contains the field
        if self.path is None and "path" in self.model_fields_set:
            _dict['path'] = None

        # set to None if drive_id (nullable) is None
        # and model_fields_set contains the field
        if self.drive_id is None and "drive_id" in self.model_fields_set:
            _dict['driveId'] = None

        # set to None if tenant (nullable) is None
        # and model_fields_set contains the field
        if self.tenant is None and "tenant" in self.model_fields_set:
            _dict['tenant'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OneDriveStorageRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "label": obj.get("label"),
            "type": obj.get("type"),
            "o_auth_id": obj.get("o_auth_id"),
            "path": obj.get("path"),
            "driveId": obj.get("driveId"),
            "tenant": obj.get("tenant")
        })
        return _obj


