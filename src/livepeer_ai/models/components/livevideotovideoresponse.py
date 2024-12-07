"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer_ai.types import BaseModel
from typing_extensions import TypedDict


class LiveVideoToVideoResponseTypedDict(TypedDict):
    r"""Response model for live video-to-video generation."""

    subscribe_url: str
    r"""Source URL of the incoming stream to subscribe to"""
    publish_url: str
    r"""Destination URL of the outgoing stream to publish to"""


class LiveVideoToVideoResponse(BaseModel):
    r"""Response model for live video-to-video generation."""

    subscribe_url: str
    r"""Source URL of the incoming stream to subscribe to"""

    publish_url: str
    r"""Destination URL of the outgoing stream to publish to"""
