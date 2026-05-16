# Here we are going to implement "POST" method

from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {        
    1 : {
        "name" : "John",
        "Age" : 15,
        "year" : "year 11"
    }  
}

class Student(BaseModel):
    name : str
    age : int
    year : str

'''
-> we have made this class so that every student we create should have a blueprint like this class Student
'''

@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student):
    if student_id in students:
        return {"Error" : "Student already exists"}
    students[student_id] = student
    return students[student_id]

'''
-> Now you will be thinking what's this "student" and "Student", so you've to import BaseModel from pydantic.
-> First you've ton define a blueprint/basemodel how your entry is going to look like & that's why we've made this class. 
'''


