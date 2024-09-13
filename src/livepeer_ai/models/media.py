"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer_ai.types import BaseModel
from typing import TypedDict


class MediaTypedDict(TypedDict):
    r"""A media object containing information about the generated media."""

    url: str
    r"""The URL where the media can be accessed."""
    seed: int
    r"""The seed used to generate the media."""
    nsfw: bool
    r"""Whether the media was flagged as NSFW."""


class Media(BaseModel):
    r"""A media object containing information about the generated media."""

    url: str
    r"""The URL where the media can be accessed."""

    seed: int
    r"""The seed used to generate the media."""

    nsfw: bool
    r"""Whether the media was flagged as NSFW."""
