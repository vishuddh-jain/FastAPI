from fastapi import FastAPI, Path

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

# fro this path parameter we will need 'Path' module to be imported
@app.get("/get-students/{student_id}") # Passing a parameter to get info. of a particular student.
# like giving parameter while entering url.
def get_student(student_id : int = Path(description="enter a valid student id", gt =0,lt=3)): 
    return students[student_id]

"""
-> gt = greater than   :  lt = less than
-> gte = greater than or equal to   :  lte = less than or equal to  
-> .Path() is used to add validation & metadata to path parameter.
-> student_id : int - means student id must be integer
-> path(....) adds extra rules and information
"""
