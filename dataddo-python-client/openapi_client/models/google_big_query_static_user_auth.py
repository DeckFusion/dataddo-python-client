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

class GoogleBigQueryStaticUserAuth(BaseModel):
    """
    GoogleBigQueryStaticUserAuth
    """ # noqa: E501
    id: Optional[StrictInt] = None
    customer_id: Optional[StrictStr] = None
    created_at: Optional[StrictInt] = None
    updated_at: Optional[StrictInt] = None
    label: Optional[StrictStr] = None
    object_id: Optional[StrictStr] = Field(default=None, alias="objectId")
    status: Optional[StrictBool] = None
    status_detail: Optional[StrictStr] = None
    service_type: Optional[StrictStr] = None
    last_use: Optional[datetime] = None
    identifier: Optional[StrictStr] = None
    hash: Optional[StrictStr] = None
    static_key: Optional[StrictStr] = Field(default=None, alias="staticKey")
    client_id: Optional[StrictStr] = Field(default=None, alias="clientId")
    client_secret: Optional[StrictStr] = Field(default=None, alias="clientSecret")
    redirect_uri: Optional[StrictStr] = Field(default=None, alias="redirectUri")
    __properties: ClassVar[List[str]] = ["id", "customer_id", "created_at", "updated_at", "label", "objectId", "status", "status_detail", "service_type", "last_use", "identifier", "hash", "staticKey", "clientId", "clientSecret", "redirectUri"]

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
        """Create an instance of GoogleBigQueryStaticUserAuth from a JSON string"""
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
            _dict['last_use'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GoogleBigQueryStaticUserAuth from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "customer_id": obj.get("customer_id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "label": obj.get("label"),
            "objectId": obj.get("objectId"),
            "status": obj.get("status"),
            "status_detail": obj.get("status_detail"),
            "service_type": obj.get("service_type"),
            "last_use": obj.get("last_use"),
            "identifier": obj.get("identifier"),
            "hash": obj.get("hash"),
            "staticKey": obj.get("staticKey"),
            "clientId": obj.get("clientId"),
            "clientSecret": obj.get("clientSecret"),
            "redirectUri": obj.get("redirectUri")
        })
        return _obj


