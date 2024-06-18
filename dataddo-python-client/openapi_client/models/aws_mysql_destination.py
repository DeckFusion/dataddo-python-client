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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AwsMysqlDestination(BaseModel):
    """
    AwsMysqlDestination
    """ # noqa: E501
    id: Optional[StrictStr] = None
    customer_id: Optional[StrictStr] = None
    created_at: Optional[StrictInt] = None
    updated_at: Optional[StrictInt] = None
    last_use: Optional[datetime] = Field(default=None, alias="lastUse")
    label: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    status: Optional[StrictBool] = None
    status_detail: Optional[StrictStr] = Field(default=None, alias="statusDetail")
    o_auth_id: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["id", "customer_id", "created_at", "updated_at", "lastUse", "label", "description", "status", "statusDetail", "o_auth_id"]

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
        """Create an instance of AwsMysqlDestination from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['created_at'] = None

        # set to None if updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.updated_at is None and "updated_at" in self.model_fields_set:
            _dict['updated_at'] = None

        # set to None if last_use (nullable) is None
        # and model_fields_set contains the field
        if self.last_use is None and "last_use" in self.model_fields_set:
            _dict['lastUse'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AwsMysqlDestination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "customer_id": obj.get("customer_id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "lastUse": obj.get("lastUse"),
            "label": obj.get("label"),
            "description": obj.get("description"),
            "status": obj.get("status"),
            "statusDetail": obj.get("statusDetail"),
            "o_auth_id": obj.get("o_auth_id")
        })
        return _obj


