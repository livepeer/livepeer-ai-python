"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .llmmessage import LLMMessage, LLMMessageTypedDict
from livepeer_ai.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class LLMChoiceTypedDict(TypedDict):
    index: int
    finish_reason: NotRequired[str]
    delta: NotRequired[LLMMessageTypedDict]
    message: NotRequired[LLMMessageTypedDict]


class LLMChoice(BaseModel):
    index: int

    finish_reason: Optional[str] = ""

    delta: Optional[LLMMessage] = None

    message: Optional[LLMMessage] = None
