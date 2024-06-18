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

class MongoDtoAuthorizer(BaseModel):
    """
    MongoDtoAuthorizer
    """ # noqa: E501
    dsn: Optional[StrictStr] = None
    database: Optional[StrictStr] = None
    use_ssh: Optional[StrictBool] = Field(default=None, alias="useSSH")
    certificate_id: Optional[StrictStr] = Field(default=None, alias="certificateId")
    ssh_host: Optional[StrictStr] = Field(default=None, alias="sshHost")
    ssh_port: Optional[StrictInt] = Field(default=None, alias="sshPort")
    ssh_remote_host: Optional[StrictStr] = Field(default=None, alias="sshRemoteHost")
    ssh_remote_port: Optional[StrictInt] = Field(default=None, alias="sshRemotePort")
    ssh_username: Optional[StrictStr] = Field(default=None, alias="sshUsername")
    ssh_password: Optional[StrictStr] = Field(default=None, alias="sshPassword")
    label: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["dsn", "database", "useSSH", "certificateId", "sshHost", "sshPort", "sshRemoteHost", "sshRemotePort", "sshUsername", "sshPassword", "label"]

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
        """Create an instance of MongoDtoAuthorizer from a JSON string"""
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
        # set to None if certificate_id (nullable) is None
        # and model_fields_set contains the field
        if self.certificate_id is None and "certificate_id" in self.model_fields_set:
            _dict['certificateId'] = None

        # set to None if ssh_host (nullable) is None
        # and model_fields_set contains the field
        if self.ssh_host is None and "ssh_host" in self.model_fields_set:
            _dict['sshHost'] = None

        # set to None if ssh_port (nullable) is None
        # and model_fields_set contains the field
        if self.ssh_port is None and "ssh_port" in self.model_fields_set:
            _dict['sshPort'] = None

        # set to None if ssh_remote_host (nullable) is None
        # and model_fields_set contains the field
        if self.ssh_remote_host is None and "ssh_remote_host" in self.model_fields_set:
            _dict['sshRemoteHost'] = None

        # set to None if ssh_remote_port (nullable) is None
        # and model_fields_set contains the field
        if self.ssh_remote_port is None and "ssh_remote_port" in self.model_fields_set:
            _dict['sshRemotePort'] = None

        # set to None if ssh_username (nullable) is None
        # and model_fields_set contains the field
        if self.ssh_username is None and "ssh_username" in self.model_fields_set:
            _dict['sshUsername'] = None

        # set to None if ssh_password (nullable) is None
        # and model_fields_set contains the field
        if self.ssh_password is None and "ssh_password" in self.model_fields_set:
            _dict['sshPassword'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MongoDtoAuthorizer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dsn": obj.get("dsn"),
            "database": obj.get("database"),
            "useSSH": obj.get("useSSH"),
            "certificateId": obj.get("certificateId"),
            "sshHost": obj.get("sshHost"),
            "sshPort": obj.get("sshPort"),
            "sshRemoteHost": obj.get("sshRemoteHost"),
            "sshRemotePort": obj.get("sshRemotePort"),
            "sshUsername": obj.get("sshUsername"),
            "sshPassword": obj.get("sshPassword"),
            "label": obj.get("label")
        })
        return _obj


