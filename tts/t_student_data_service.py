import json
from resources.students.students_data_service import StudentDataService


def get_data_service():

    config = {
        "data_directory": "/Users/donaldferguson/Dropbox/0-Examples/e6156-f23-template/data",
        "data_file": "students.json"
    }

    ds = StudentDataService(config)
    return ds


def t1():

    ds = get_data_service()
    students = ds.get_students(school_code="SEAS")
    print("t1: students = ", json.dumps(students, indent=2))


if __name__ == "__main__":
    t1()

    