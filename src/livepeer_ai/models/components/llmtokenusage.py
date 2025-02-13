"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer_ai.types import BaseModel
from typing_extensions import TypedDict


class LLMTokenUsageTypedDict(TypedDict):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class LLMTokenUsage(BaseModel):
    prompt_tokens: int

    completion_tokens: int

    total_tokens: int
