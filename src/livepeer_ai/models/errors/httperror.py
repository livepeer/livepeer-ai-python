"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from livepeer_ai import utils
from livepeer_ai.models.components import apierror as components_apierror
from livepeer_ai.types import BaseModel


class HTTPErrorData(BaseModel):
    detail: components_apierror.APIError
    r"""Detailed error information."""


class HTTPError(Exception):
    r"""HTTP error response model."""

    data: HTTPErrorData

    def __init__(self, data: HTTPErrorData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, HTTPErrorData)
