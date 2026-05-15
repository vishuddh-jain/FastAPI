from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI() 

# Creating a local database of students.
students = {        
    1 : {
        "name" : "John",
        "Age" : 15,
        "year" : "year 11"
    }  
}

@app.get("/") # this is an endpoint
def index():
    return{"name" : "First API"}

# for this path parameter we will need 'Path' module to be imported
@app.get("/get-students/{student_id}") # Passing a parameter to get info. of a particular student.
# like giving parameter while entering url.
def get_student(student_id : int = Path(description="enter a valid student id", gt =0,lt=3)): 
    return students[student_id]


'''
In path parameter we need to add that variable in url itself whereas in query para. we don't define it in url.
Basically like: google.com/results?search=Python , this (search=Python) combination after "?" is the query.
You can see there is no "/" after results but "?" in above url, which shows results endpoint contains query
'''
@app.get("/get-by-name/{stuednt_id}") 
def get_student(*,student_id : int, name : Optional[str] = None, test : int): # this is the Query parameter(name) not added in path(url) as endpoint
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data" : "Not Found"}

'''
-> we cannot use multiple param/arguments here in any sequence, like :def get_student(name: Optional[str]:None, test:int).
-> here required argument can't come after optional you've to change their places OR just add "*" as first param. like:
                def get_students(*, name : Optional[str] = None, test : int).
-> Optional is not a required parameter.
'''
