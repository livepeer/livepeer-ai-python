"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer_ai.types import BaseModel
from livepeer_ai.utils import FieldMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class BodyGenLLMTypedDict(TypedDict):
    prompt: str
    model_id: NotRequired[str]
    system_msg: NotRequired[str]
    temperature: NotRequired[float]
    max_tokens: NotRequired[int]
    history: NotRequired[str]
    stream: NotRequired[bool]


class BodyGenLLM(BaseModel):
    prompt: Annotated[str, FieldMetadata(form=True)]

    model_id: Annotated[Optional[str], FieldMetadata(form=True)] = ""

    system_msg: Annotated[Optional[str], FieldMetadata(form=True)] = ""

    temperature: Annotated[Optional[float], FieldMetadata(form=True)] = 0.7

    max_tokens: Annotated[Optional[int], FieldMetadata(form=True)] = 256

    history: Annotated[Optional[str], FieldMetadata(form=True)] = "[]"

    stream: Annotated[Optional[bool], FieldMetadata(form=True)] = False
