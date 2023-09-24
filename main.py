#
# FastAPI is a framework and library for implementing REST web services in Python.
# https://fastapi.tiangolo.com/
#
from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import RedirectResponse

from fastapi.staticfiles import StaticFiles
from typing import List, Union

# I like to launch directly and not use the standard FastAPI startup process.
# So, I include uvicorn
import uvicorn


from resources.students.students_resource import StudentsResource
from resources.students.students_data_service import StudentDataService
from resources.students.student_models import StudentModel, StudentRspModel
from resources.schools.school_models import SchoolRspModel, SchoolModel
from resources.schools.schools_resource import SchoolsResource

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


# ******************************
#
# DFF TODO Show the class how to do this with a service factory instead of hard code.


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


students_resource = get_student_resource()

schools_resource = SchoolsResource(config={"students_resource": students_resource})


#
# END TODO
# **************************************


@app.get("/")
async def root():
    return RedirectResponse("/static/index.html")


@app.get("/students", response_model=List[StudentRspModel])
async def get_students(uni: str = None, last_name: str = None, school_code: str = None):
    """
    Return a list of students matching a query string.

    - **uni**: student's UNI
    - **last_name**: student's last name
    - **school_code**: student's school.
    """
    result = students_resource.get_students(uni, last_name, school_code)
    return result


@app.get("/students/{uni}", response_model=Union[StudentRspModel, None])
async def get_student(uni: str):
    """
    Return a student based on UNI.

    - **uni**: student's UNI
    """
    result = None
    result = students_resource.get_students(uni)
    if len(result) == 1:
        result = result[0]
    else:
        raise HTTPException(status_code=404, detail="Not found")

    return result


@app.get("/schools", response_model=List[SchoolRspModel])
async def get_schools():
    """
    Return a list of schools.
    """
    result = schools_resource.get_schools()
    return result


@app.get("/schools/{school_code}/students", response_model=List[StudentRspModel])
async def get_schools_students(school_code, uni=None, last_name=None):
    """
    Return a list of schools.
    """
    result = schools_resource.get_schools_students(school_code, uni, last_name)
    return result




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8011)
