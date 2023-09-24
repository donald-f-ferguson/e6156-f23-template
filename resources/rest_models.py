from __future__ import annotations

from pydantic import BaseModel


class Link(BaseModel):
    rel: str
    href: str


