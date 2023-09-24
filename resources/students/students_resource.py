from resources.abstract_base_resource import BaseResource
from resources.students.student_models import StudentRspModel, StudentModel
from resources.rest_models import Link
from typing import List


class StudentsResource(BaseResource):
    #
    # This code is just to get us started.
    # It is also pretty sloppy code.
    #

    def __init__(self, config):
        super().__init__()

        self.data_service = config["data_service"]

    @staticmethod
    def _generate_links(s: dict) -> StudentRspModel:

        self_link = Link(**{
            "rel": "self",
            "href": "/students/" + s['uni']
        })
        school_link = Link(**{
            "rel": "school",
            "href": "/schools/" + s['school_code']
        })

        links = [
            self_link,
            school_link
        ]
        rsp = StudentRspModel(**s, links=links)
        return rsp

    def get_students(self, uni: str = None, last_name: str = None, school_code: str = None) -> List[StudentRspModel]:

        result = self.data_service.get_students(uni, last_name, school_code)
        final_result = []

        for s in result:
            m = self._generate_links(s)
            final_result.append(m)

        return final_result

