from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

applications = []
counter= 1

class Application(BaseModel):
    company: str
    role: str
    status: str = "applied"
    notes: Optional[str] = None

@app.get("/")
def root():
    return {"messagae":"Job Tracker API is running"}

# create an application
@app.post("/applications")
def add_application(app_data: Application):
    global counter
    new_app = {"id":counter, **app_data.dict()}
    applications.append(new_app)
    counter+=1
    return new_app

#get all applications
@app.get("/applications/")
def get_applications():
    return applications

#get one application
@app.get("/applications/{id}")
def get_application(id:int):
    for app in applications:
        if app["id"] == id:
            return app
    return {"error":"Application not found"}

#update an application
@app.put("/applications/{id}")
def update_status(id:int, status:str):
    for app in applications:
        if app["id"] == id:
            app["status"] == status
        return app
    return {"error":"Application not found"}