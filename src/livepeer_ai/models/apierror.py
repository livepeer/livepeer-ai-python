"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer_ai.types import BaseModel
from typing import TypedDict


class APIErrorTypedDict(TypedDict):
    msg: str
    

class APIError(BaseModel):
    msg: str
    
