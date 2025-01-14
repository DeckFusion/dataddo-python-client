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
from openapi_client.models.flow_api import FlowApi
from openapi_client.models.flow_data_quality_rule import FlowDataQualityRule
from openapi_client.models.flow_operation import FlowOperation
from openapi_client.models.flow_source import FlowSource
from openapi_client.models.flow_write_action import FlowWriteAction
from typing import Optional, Set
from typing_extensions import Self

class Flow(BaseModel):
    """
    Class Flow
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Primary key of document. The value is null when document is not persisted.")
    label: Optional[Any] = Field(default=None, description="Label")
    user_id: Optional[Any] = Field(default=None, description="User customerId instead.")
    customer_id: Optional[Any] = Field(default=None, description="Customer")
    source: Optional[List[FlowSource]] = Field(default=None, description="The list of sources that are involved in the flow")
    tag: Optional[List[StrictStr]] = None
    operation: Optional[List[FlowOperation]] = Field(default=None, description="The list of operations to be run in DPI on the data")
    rules: Optional[List[FlowDataQualityRule]] = Field(default=None, description="The list of data quality rules")
    api: Optional[FlowApi] = None
    write_action: Optional[FlowWriteAction] = None
    __properties: ClassVar[List[str]] = ["id", "label", "user_id", "customer_id", "source", "tag", "operation", "rules", "api", "write_action"]

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
        """Create an instance of Flow from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in source (list)
        _items = []
        if self.source:
            for _item in self.source:
                if _item:
                    _items.append(_item.to_dict())
            _dict['source'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in operation (list)
        _items = []
        if self.operation:
            for _item in self.operation:
                if _item:
                    _items.append(_item.to_dict())
            _dict['operation'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rules'] = _items
        # override the default output from pydantic by calling `to_dict()` of api
        if self.api:
            _dict['api'] = self.api.to_dict()
        # override the default output from pydantic by calling `to_dict()` of write_action
        if self.write_action:
            _dict['write_action'] = self.write_action.to_dict()
        # set to None if label (nullable) is None
        # and model_fields_set contains the field
        if self.label is None and "label" in self.model_fields_set:
            _dict['label'] = None

        # set to None if user_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_id is None and "user_id" in self.model_fields_set:
            _dict['user_id'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customer_id'] = None

        # set to None if api (nullable) is None
        # and model_fields_set contains the field
        if self.api is None and "api" in self.model_fields_set:
            _dict['api'] = None

        # set to None if write_action (nullable) is None
        # and model_fields_set contains the field
        if self.write_action is None and "write_action" in self.model_fields_set:
            _dict['write_action'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Flow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "label": obj.get("label"),
            "user_id": obj.get("user_id"),
            "customer_id": obj.get("customer_id"),
            "source": [FlowSource.from_dict(_item) for _item in obj["source"]] if obj.get("source") is not None else None,
            "tag": obj.get("tag"),
            "operation": [FlowOperation.from_dict(_item) for _item in obj["operation"]] if obj.get("operation") is not None else None,
            "rules": [FlowDataQualityRule.from_dict(_item) for _item in obj["rules"]] if obj.get("rules") is not None else None,
            "api": FlowApi.from_dict(obj["api"]) if obj.get("api") is not None else None,
            "write_action": FlowWriteAction.from_dict(obj["write_action"]) if obj.get("write_action") is not None else None
        })
        return _obj


