"""Contrat de la route de santé."""

from typing import Literal

from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: Literal["ok"]
    service: str
    database: Literal["up", "down"]
