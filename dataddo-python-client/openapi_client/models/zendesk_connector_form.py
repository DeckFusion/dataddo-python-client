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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ZendeskConnectorForm(BaseModel):
    """
    ZendeskConnectorForm
    """ # noqa: E501
    ensure_data_types: Optional[Dict[str, Any]] = Field(default=None, description="Enforcing data types", alias="ensureDataTypes")
    allow_empty: Optional[StrictBool] = Field(default=True, alias="allowEmpty")
    nullable_fields: Optional[StrictBool] = Field(default=True, alias="nullableFields")
    connector_id: StrictStr = Field(alias="connectorId")
    template_id: StrictStr = Field(alias="templateId")
    strategy: Optional[StrictStr] = Field(default=None, description="Use storageStrategy instead.")
    storage_strategy: StrictStr = Field(alias="storageStrategy")
    label: StrictStr = Field(description="Label of the source")
    o_auth_id: Optional[StrictStr] = Field(alias="oAuthId")
    url: StrictStr
    method: StrictStr
    headers: Optional[List[Any]] = Field(default=None, description="HTTP Headers of the request")
    body: Optional[StrictStr] = None
    transformation: StrictStr
    emitter: Optional[StrictStr] = None
    parameters: Optional[List[StrictStr]] = Field(default=None, description="Custom parameters supplied")
    attributes: List[StrictStr] = Field(description="Final selections of the attributes to be included in the source")
    __properties: ClassVar[List[str]] = ["ensureDataTypes", "allowEmpty", "nullableFields", "connectorId", "templateId", "strategy", "storageStrategy", "label", "oAuthId", "url", "method", "headers", "body", "transformation", "emitter", "parameters", "attributes"]

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
        """Create an instance of ZendeskConnectorForm from a JSON string"""
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
        # set to None if o_auth_id (nullable) is None
        # and model_fields_set contains the field
        if self.o_auth_id is None and "o_auth_id" in self.model_fields_set:
            _dict['oAuthId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ZendeskConnectorForm from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ensureDataTypes": obj.get("ensureDataTypes"),
            "allowEmpty": obj.get("allowEmpty") if obj.get("allowEmpty") is not None else True,
            "nullableFields": obj.get("nullableFields") if obj.get("nullableFields") is not None else True,
            "connectorId": obj.get("connectorId"),
            "templateId": obj.get("templateId"),
            "strategy": obj.get("strategy"),
            "storageStrategy": obj.get("storageStrategy"),
            "label": obj.get("label"),
            "oAuthId": obj.get("oAuthId"),
            "url": obj.get("url"),
            "method": obj.get("method"),
            "headers": obj.get("headers"),
            "body": obj.get("body"),
            "transformation": obj.get("transformation"),
            "emitter": obj.get("emitter"),
            "parameters": obj.get("parameters"),
            "attributes": obj.get("attributes")
        })
        return _obj


