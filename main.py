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
    for application in applications:
        if application["id"] == id:
            return application
    return {"error":"Application not found"}

#update an application
@app.put("/applications/{id}")
def update_status(id:int, status:str):
    print(f"Received status: '{status}'")
    for application in applications:
        if application["id"] == id:
            application["status"] == status
        return application
    return {"error":"Application not found"}

@app.delete("/applications/{id}")
def delete_application(id:int):
    for index,application in enumerare(applications):
        if application["id"] == id:
            applications.pop(index)
            return {"message": f"Application {id} deleted"}
    return {"error":"application not found"}