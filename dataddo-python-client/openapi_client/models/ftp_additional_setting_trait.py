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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class FtpAdditionalSettingTrait(BaseModel):
    """
    FtpAdditionalSettingTrait
    """ # noqa: E501
    disable_explicit_tls: Optional[StrictBool] = Field(default=None, alias="disableExplicitTLS")
    dial_timeout: Optional[StrictInt] = Field(default=None, alias="dialTimeout")
    shut_timeout: Optional[StrictInt] = Field(default=None, alias="shutTimeout")
    disable_epsv: Optional[StrictBool] = Field(default=None, alias="disableEPSV")
    disable_utf8: Optional[StrictBool] = Field(default=None, alias="disableUTF8")
    disable_mlsd: Optional[StrictBool] = Field(default=None, alias="disableMLSD")
    mdtm_write: Optional[StrictBool] = Field(default=None, alias="MDTMWrite")
    __properties: ClassVar[List[str]] = ["disableExplicitTLS", "dialTimeout", "shutTimeout", "disableEPSV", "disableUTF8", "disableMLSD", "MDTMWrite"]

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
        """Create an instance of FtpAdditionalSettingTrait from a JSON string"""
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
        """Create an instance of FtpAdditionalSettingTrait from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "disableExplicitTLS": obj.get("disableExplicitTLS"),
            "dialTimeout": obj.get("dialTimeout"),
            "shutTimeout": obj.get("shutTimeout"),
            "disableEPSV": obj.get("disableEPSV"),
            "disableUTF8": obj.get("disableUTF8"),
            "disableMLSD": obj.get("disableMLSD"),
            "MDTMWrite": obj.get("MDTMWrite")
        })
        return _obj

