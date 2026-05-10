from fastapi import FastAPI

app = FastAPI() 

"""
-> @app.get("/") - it means app object is getting some info from FastAPI instance.
-> @app - app is your FastAPI application. it controls your API.
-> .get - a HTTP method, GET - used to fetch data.
-> "/" - this is the endpoint(path), / means root url. eg : http://127.0.0.5:8000/ so here the last / is the end point,
from where the info is being fetched 
"""
@app.get("/") # this is an endpoint
def index():
    return{"name" : "First API"}

"""
-> The most basic is whatever endpoint your url will be containing, 
the function under that endpoint will be executed.

1.) .get --  method gets the information what ever you willl ask for from the database.
2.) .post -- Creates anything new, like here it can create a new student. 
3.) .put -- Updates something that already exits
4.) .delete -- deletes anything 
"""