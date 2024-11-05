"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .mediaurl import MediaURL, MediaURLTypedDict
from livepeer_ai.types import BaseModel
from typing_extensions import TypedDict


class AudioResponseTypedDict(TypedDict):
    r"""Response model for audio generation."""

    audio: MediaURLTypedDict
    r"""The generated audio."""


class AudioResponse(BaseModel):
    r"""Response model for audio generation."""

    audio: MediaURL
    r"""The generated audio."""
