"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer_ai.types import BaseModel
from typing import List, Union
from typing_extensions import TypeAliasType, TypedDict


LocTypedDict = TypeAliasType("LocTypedDict", Union[str, int])


Loc = TypeAliasType("Loc", Union[str, int])


class ValidationErrorTypedDict(TypedDict):
    loc: List[LocTypedDict]
    msg: str
    type: str


class ValidationError(BaseModel):
    loc: List[Loc]

    msg: str

    type: str
