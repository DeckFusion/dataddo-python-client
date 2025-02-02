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

class WriteAction(BaseModel):
    """
    WriteAction
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Primary key of document. The value is null when document is not persisted.")
    status: Optional[StrictStr] = None
    status_detail: Optional[StrictStr] = None
    duration: Optional[StrictStr] = Field(default=None, description="Duration")
    object_id: Optional[Any] = Field(default=None, description="Object ID")
    object_type: Optional[StrictStr] = Field(default=None, description="Object type")
    type: Optional[StrictStr] = Field(default=None, description="Action type")
    customer_id: Optional[StrictStr] = Field(default=None, description="Customer ID")
    last_execution: Optional[StrictInt] = Field(default=None, description="Last execution timestamp")
    next_execution: Optional[StrictInt] = Field(default=None, description="Next execution timestamp. Makes sense only for actions with schedule, otherwise it is null. It is computed and updated based on the schedule change or when action is executed.")
    error_count: Optional[StrictInt] = Field(default=None, description="Error iteration count")
    is_being_processed: Optional[StrictBool] = Field(default=None, description="Is the action currently being processed?")
    on_error_retry_timeout: Optional[StrictInt] = Field(default=None, description="After how many seconds the action should be retried if it is failed. Default is 0 meaning run retry on next Dispatcher's tick.  Example: set to 60*60*2 to retry action not earlier than 2hrs after failure")
    schedule: Optional[Any] = Field(default=None, description="Action Schedule settings")
    write_mode: Optional[StrictStr] = None
    stream: Optional[StrictBool] = None
    skip_bulk: Optional[StrictBool] = Field(default=None, alias="skipBulk")
    unique_columns: Optional[List[Any]] = None
    setup_instructions: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "status", "status_detail", "duration", "object_id", "object_type", "type", "customer_id", "last_execution", "next_execution", "error_count", "is_being_processed", "on_error_retry_timeout", "schedule", "write_mode", "stream", "skipBulk", "unique_columns", "setup_instructions"]

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
        """Create an instance of WriteAction from a JSON string"""
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
        # set to None if duration (nullable) is None
        # and model_fields_set contains the field
        if self.duration is None and "duration" in self.model_fields_set:
            _dict['duration'] = None

        # set to None if object_id (nullable) is None
        # and model_fields_set contains the field
        if self.object_id is None and "object_id" in self.model_fields_set:
            _dict['object_id'] = None

        # set to None if last_execution (nullable) is None
        # and model_fields_set contains the field
        if self.last_execution is None and "last_execution" in self.model_fields_set:
            _dict['last_execution'] = None

        # set to None if next_execution (nullable) is None
        # and model_fields_set contains the field
        if self.next_execution is None and "next_execution" in self.model_fields_set:
            _dict['next_execution'] = None

        # set to None if schedule (nullable) is None
        # and model_fields_set contains the field
        if self.schedule is None and "schedule" in self.model_fields_set:
            _dict['schedule'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WriteAction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "status": obj.get("status"),
            "status_detail": obj.get("status_detail"),
            "duration": obj.get("duration"),
            "object_id": obj.get("object_id"),
            "object_type": obj.get("object_type"),
            "type": obj.get("type"),
            "customer_id": obj.get("customer_id"),
            "last_execution": obj.get("last_execution"),
            "next_execution": obj.get("next_execution"),
            "error_count": obj.get("error_count"),
            "is_being_processed": obj.get("is_being_processed"),
            "on_error_retry_timeout": obj.get("on_error_retry_timeout"),
            "schedule": obj.get("schedule"),
            "write_mode": obj.get("write_mode"),
            "stream": obj.get("stream"),
            "skipBulk": obj.get("skipBulk"),
            "unique_columns": obj.get("unique_columns"),
            "setup_instructions": obj.get("setup_instructions")
        })
        return _obj


