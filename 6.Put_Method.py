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

class UpdateStudent:
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None
    
@app.put("/update-student{student_id}")
def update_student(student_id : int, student: UpdateStudent):
    if student_id not in student:
        return {"Error" : "Student does not exists"}
    
    if student.name != None:
        students[student_id].name == student.name
    
    if student.age != None:
        students[student_id].age == student.age
    
    if student.year != None:
        students[student_id].year == student.year
    return student[student_id]
    