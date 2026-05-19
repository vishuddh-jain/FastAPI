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

'''
this .delete method deletes data or object from database
'''

@app.delete("/delete-students/{student_id}")
def delete_student(student_id : int):
    if student_id not in students:
        return {"Error" : "student does not exists"}
    
    del students[student_id]
    return{"Message" : "Student deleted succesfully"}