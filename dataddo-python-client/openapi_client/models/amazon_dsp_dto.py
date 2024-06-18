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

class AmazonDspDto(BaseModel):
    """
    AmazonDspDto
    """ # noqa: E501
    connector_id: Optional[StrictStr] = None
    template_id: Optional[StrictStr] = None
    label: Optional[StrictStr] = None
    storage_strategy: Optional[StrictStr] = 'incremental'
    allow_empty: Optional[StrictBool] = False
    o_auth_id: Optional[StrictInt] = None
    date_range: Optional[StrictStr] = Field(default=None, alias="dateRange")
    profile_id: Optional[List[Any]] = Field(default=None, alias="profileId")
    metrics: Optional[List[Any]] = None
    dimensions: Optional[List[Any]] = None
    report_type: Optional[StrictStr] = Field(default=None, alias="reportType")
    time_unit: Optional[StrictStr] = Field(default=None, alias="timeUnit")
    account_id: Optional[StrictStr] = Field(default=None, alias="accountId")
    __properties: ClassVar[List[str]] = ["connector_id", "template_id", "label", "storage_strategy", "allow_empty", "o_auth_id", "dateRange", "profileId", "metrics", "dimensions", "reportType", "timeUnit", "accountId"]

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
        """Create an instance of AmazonDspDto from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AmazonDspDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "connector_id": obj.get("connector_id"),
            "template_id": obj.get("template_id"),
            "label": obj.get("label"),
            "storage_strategy": obj.get("storage_strategy") if obj.get("storage_strategy") is not None else 'incremental',
            "allow_empty": obj.get("allow_empty") if obj.get("allow_empty") is not None else False,
            "o_auth_id": obj.get("o_auth_id"),
            "dateRange": obj.get("dateRange"),
            "profileId": obj.get("profileId"),
            "metrics": obj.get("metrics"),
            "dimensions": obj.get("dimensions"),
            "reportType": obj.get("reportType"),
            "timeUnit": obj.get("timeUnit"),
            "accountId": obj.get("accountId")
        })
        return _obj


