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
from typing import Optional, Set
from typing_extensions import Self

class Schedule(BaseModel):
    """
    Schedule
    """ # noqa: E501
    timezone: Optional[StrictStr] = Field(default=None, description="Timezone cron identifier")
    minute: Optional[Any] = Field(default=None, description="Minute cron identifier")
    hour: Optional[Any] = Field(default=None, description="Hour cron identifier")
    day_of_month: Optional[Any] = Field(default=None, description="Day of month cron identifier")
    month: Optional[Any] = Field(default=None, description="Month cron identifier")
    day_of_week: Optional[Any] = Field(default=None, description="Day of week cron identifier")
    sync_frequency: Optional[Any] = Field(default=None, description="Sync frequency (day/week/month/custom)")
    __properties: ClassVar[List[str]] = ["timezone", "minute", "hour", "day_of_month", "month", "day_of_week", "sync_frequency"]

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
        """Create an instance of Schedule from a JSON string"""
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
        # set to None if minute (nullable) is None
        # and model_fields_set contains the field
        if self.minute is None and "minute" in self.model_fields_set:
            _dict['minute'] = None

        # set to None if hour (nullable) is None
        # and model_fields_set contains the field
        if self.hour is None and "hour" in self.model_fields_set:
            _dict['hour'] = None

        # set to None if day_of_month (nullable) is None
        # and model_fields_set contains the field
        if self.day_of_month is None and "day_of_month" in self.model_fields_set:
            _dict['day_of_month'] = None

        # set to None if month (nullable) is None
        # and model_fields_set contains the field
        if self.month is None and "month" in self.model_fields_set:
            _dict['month'] = None

        # set to None if day_of_week (nullable) is None
        # and model_fields_set contains the field
        if self.day_of_week is None and "day_of_week" in self.model_fields_set:
            _dict['day_of_week'] = None

        # set to None if sync_frequency (nullable) is None
        # and model_fields_set contains the field
        if self.sync_frequency is None and "sync_frequency" in self.model_fields_set:
            _dict['sync_frequency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Schedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "timezone": obj.get("timezone"),
            "minute": obj.get("minute"),
            "hour": obj.get("hour"),
            "day_of_month": obj.get("day_of_month"),
            "month": obj.get("month"),
            "day_of_week": obj.get("day_of_week"),
            "sync_frequency": obj.get("sync_frequency")
        })
        return _obj


