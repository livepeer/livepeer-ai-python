"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import io
from livepeer_ai.types import BaseModel
from livepeer_ai.utils import FieldMetadata, MultipartFormMetadata
import pydantic
from typing import IO, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class BodyGenImageToTextImageTypedDict(TypedDict):
    file_name: str
    content: Union[bytes, IO[bytes], io.BufferedReader]
    content_type: NotRequired[str]


class BodyGenImageToTextImage(BaseModel):
    file_name: Annotated[
        str, pydantic.Field(alias="fileName"), FieldMetadata(multipart=True)
    ]

    content: Annotated[
        Union[bytes, IO[bytes], io.BufferedReader],
        pydantic.Field(alias=""),
        FieldMetadata(multipart=MultipartFormMetadata(content=True)),
    ]

    content_type: Annotated[
        Optional[str],
        pydantic.Field(alias="Content-Type"),
        FieldMetadata(multipart=True),
    ] = None


class BodyGenImageToTextTypedDict(TypedDict):
    image: BodyGenImageToTextImageTypedDict
    r"""Uploaded image to transform with the pipeline."""
    prompt: NotRequired[str]
    r"""Text prompt(s) to guide transformation."""
    model_id: NotRequired[str]
    r"""Hugging Face model ID used for transformation."""


class BodyGenImageToText(BaseModel):
    image: Annotated[
        BodyGenImageToTextImage,
        FieldMetadata(multipart=MultipartFormMetadata(file=True)),
    ]
    r"""Uploaded image to transform with the pipeline."""

    prompt: Annotated[Optional[str], FieldMetadata(multipart=True)] = ""
    r"""Text prompt(s) to guide transformation."""

    model_id: Annotated[Optional[str], FieldMetadata(multipart=True)] = ""
    r"""Hugging Face model ID used for transformation."""
