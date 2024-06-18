# coding: utf-8

"""
    Dataddo Headless BETA API

    Dataddo Headless BETA API

    The version of the OpenAPI document: 1.0.0-beta.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ActionStatusEnum(str, Enum):
    """
    ActionStatusEnum
    """

    """
    allowed enum values
    """
    LIVE = 'live'
    BROKEN = 'broken'
    RETRYING = 'retrying'
    RUNNING = 'running'
    INACTIVE = 'inactive'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ActionStatusEnum from a JSON string"""
        return cls(json.loads(json_str))

