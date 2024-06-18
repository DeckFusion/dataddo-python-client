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
from openapi_client.models.app_authorizer_tik_tok_custom_tik_tok_custom_authorizer_get_authorization_url_request_config import AppAuthorizerTikTokCustomTikTokCustomAuthorizerGetAuthorizationUrlRequestConfig
from typing import Optional, Set
from typing_extensions import Self

class AppAuthorizerTikTokCustomTikTokCustomAuthorizerGetAuthorizationUrlRequest(BaseModel):
    """
    AppAuthorizerTikTokCustomTikTokCustomAuthorizerGetAuthorizationUrlRequest
    """ # noqa: E501
    config: AppAuthorizerTikTokCustomTikTokCustomAuthorizerGetAuthorizationUrlRequestConfig
    state: Optional[StrictStr] = None
    service_id: Optional[StrictStr] = Field(default=None, alias="serviceId")
    __properties: ClassVar[List[str]] = ["config", "state", "serviceId"]

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
        """Create an instance of AppAuthorizerTikTokCustomTikTokCustomAuthorizerGetAuthorizationUrlRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppAuthorizerTikTokCustomTikTokCustomAuthorizerGetAuthorizationUrlRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "config": AppAuthorizerTikTokCustomTikTokCustomAuthorizerGetAuthorizationUrlRequestConfig.from_dict(obj["config"]) if obj.get("config") is not None else None,
            "state": obj.get("state"),
            "serviceId": obj.get("serviceId")
        })
        return _obj


