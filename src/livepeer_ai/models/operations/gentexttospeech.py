"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer_ai.models.components import (
    audioresponse as components_audioresponse,
    httpmetadata as components_httpmetadata,
)
from livepeer_ai.types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GenTextToSpeechResponseTypedDict(TypedDict):
    http_meta: components_httpmetadata.HTTPMetadataTypedDict
    audio_response: NotRequired[components_audioresponse.AudioResponseTypedDict]
    r"""Successful Response"""


class GenTextToSpeechResponse(BaseModel):
    http_meta: Annotated[
        Optional[components_httpmetadata.HTTPMetadata], pydantic.Field(exclude=True)
    ] = None

    audio_response: Optional[components_audioresponse.AudioResponse] = None
    r"""Successful Response"""
