"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .media import Media, MediaTypedDict
from livepeer_ai.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ImageResponseTypedDict(TypedDict):
    r"""Response model for image generation."""

    images: List[MediaTypedDict]
    r"""The generated images."""


class ImageResponse(BaseModel):
    r"""Response model for image generation."""

    images: List[Media]
    r"""The generated images."""
