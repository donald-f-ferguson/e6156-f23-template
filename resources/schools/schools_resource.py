from resources.abstract_base_resource import BaseResource
from resources.schools.school_models import SchoolRspModel, SchoolModel
from resources.rest_models import Link
from typing import List
from resources.students.students_resource import StudentsResource


class SchoolsResource(BaseResource):
    #
    # This code is just to get us started.
    # It is also pretty sloppy code.
    #

    def __init__(self, config=None):
        super().__init__()
        s_resource: StudentsResource = config.get("students_resource", None)
        self.student_resource = s_resource

        self.schools = []

        self.schools.append(SchoolRspModel(school_code="CC",
                                           school_name="Columbia College"))
        self.schools.append(SchoolRspModel(school_code="SEAS", school_name="School of Engineering and Applied Sciences"))
        self.schools.append(SchoolRspModel(school_code="BN", school_name="Barnard College"))
        self.schools.append(SchoolRspModel(school_code="GSAS", school_name="Graduate School of Arts and Sciences"))
        self.schools.append(SchoolRspModel(school_code="GS", school_name="General Studies"))

        for s in self.schools:
            s.links = [
                Link(rel="students", href="/schools/" + s.school_code + "/students"),
                Link(rel="self", href="/schools/" + s.school_code)
            ]

    def get_schools(self) -> List[SchoolRspModel]:
        return self.schools

    def get_schools_students(self, school_code, uni=None, last_name=None):
        result = self.student_resource.get_students(uni, last_name, school_code)
        return result


