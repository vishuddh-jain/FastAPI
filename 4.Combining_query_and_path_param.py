# For this you just've to add student_id as path param. in ur; as endpoint and put it in the function 

# LIKE:
from fastapi import FastAPI, Path
from typing import Optional

students = {        
    1 : {
        "name" : "John",
        "Age" : 15,
        "year" : "year 11"
    }  
}

def get_students(*,student_id : int, name : Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data" : "Not Found"}
