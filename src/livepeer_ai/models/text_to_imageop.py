"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .imageresponse import ImageResponse, ImageResponseTypedDict
import httpx
from livepeer_ai.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class TextToImageResponseTypedDict(TypedDict):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    image_response: NotRequired[ImageResponseTypedDict]
    r"""Successful Response"""
    

class TextToImageResponse(BaseModel):
    content_type: str
    r"""HTTP response content type for this operation"""
    status_code: int
    r"""HTTP response status code for this operation"""
    raw_response: httpx.Response
    r"""Raw HTTP response; suitable for custom response parsing"""
    image_response: Optional[ImageResponse] = None
    r"""Successful Response"""
    
