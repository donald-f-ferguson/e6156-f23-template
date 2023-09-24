from resources.students.students_resource import StudentsResource
from resources.students.students_data_service import StudentDataService
import json


def get_data_service():

    config = {
        "data_directory": "/Users/donaldferguson/Dropbox/0-Examples/e6156-f23-template/data",
        "data_file": "students.json"
    }

    ds = StudentDataService(config)
    return ds


def get_student_resource():
    ds = get_data_service()
    config = {
        "data_service": ds
    }
    res = StudentsResource(config)
    return res


def t1():

    s = get_student_resource()
    res = s.get_students(school_code="SEAS")
    print("t1: res = ", json.dumps(res, indent=2, default=str))


if __name__ == "__main__":
    t1()
