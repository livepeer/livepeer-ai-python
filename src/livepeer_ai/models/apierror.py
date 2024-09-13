"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer_ai.types import BaseModel
from typing import TypedDict


class APIErrorTypedDict(TypedDict):
    r"""API error response model."""

    msg: str
    r"""The error message."""


class APIError(BaseModel):
    r"""API error response model."""

    msg: str
    r"""The error message."""
