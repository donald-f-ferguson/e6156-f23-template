from __future__ import annotations
from pydantic import BaseModel
from typing import List

from resources.rest_models import Link


class StudentModel(BaseModel):
    uni: str
    first_name: str
    last_name: str
    email: str
    school_code: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "uni": "kxl2398",
                    "first_name": "Iolande",
                    "last_name": "Birkin",
                    "email": "ibirkin0@amazon.co.jp",
                    "school_code": "BN"
                }
            ]
        }
    }


class StudentRspModel(StudentModel):
    links: List[Link] = None



