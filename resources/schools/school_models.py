from __future__ import annotations
from pydantic import BaseModel
from typing import List

from resources.rest_models import Link


class SchoolModel(BaseModel):
    school_code: str
    school_name: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "school_code": "CC",
                    "school_name": "Columbia College"
                }
            ]
        }
    }


class SchoolRspModel(SchoolModel):
    links: List[Link] = None

