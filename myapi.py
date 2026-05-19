from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

students = {
    1 : {
        "name" : "John",
        "Age" : 15,
        "year" : "year 11"
    }  
}

app = FastAPI()

class Student(BaseModel): # this is the main class, basically for the POST method, while creating a new student
    name : str
    age: int
    year: str

class UpdateStudent(BaseModel): # this is class for updating any student information, this is made so that everytime we don't need to update everthing
    name :  Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None


@app.get("/")
def index():
    return{"name" : "First API"}


@app.get("/get-student/{student_id}") # Path parameter is (student_id) as an endpoint.
def get_student(student_id : int = Path(description= "provide a valid student id you want to view", gt = 0, lt=3)):
    return students[student_id]


@app.get("/get-by-name/{stuednt_id}") # combining path and query parameter in this function
def get_student(*,student_id : int, name : Optional[str] = None, test : int): # this is the Query parameter(name) not added in path(url) as endpoint
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data" : "Not Found"}


# Creating New Student from student_id
@app.post("/create-student/{student_id}")
def create_student(student_id : int, student : Student): # Here student data type is Student class as student_id data type is int
    if student_id in students:
        return {"Error" : "Student already exists"}
    students[student_id] = student
    return students[student_id]
# Currently we are not connected to a database therefore the data is not being stored   


# Updating student information
@app.put("/update-students/{student_id}")
def update_students(student_id : int, student: UpdateStudent):
    if student_id not in students:
        return {"Error" : "Student id does not exists"}
    
    if student.name != None:
        students[student_id].name = student.name
    
    if student.age != None:
        students[student_id].age = student.age
    
    if student.year != None:
        students[student_id].year = student.year
    
    return students[student_id]


@app.delete("/delete-students/{student_id}")
def delete_student(student_id : int):
    if student_id not in students:
        return {"Error" : "student does not exists"}
    
    del students[student_id]
    return{"Message" : "Student deleted succesfully"}
    