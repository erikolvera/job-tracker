from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session
from database import ApplicationModel, get_db

app = FastAPI()

class Application(BaseModel):
    company: str
    role: str
    status: str = "applied"
    notes: Optional[str] = None

@app.get("/")
def root():
    return {"message": "Job Tracker API is running"}

@app.post("/applications")
def add_application(app_data: Application, db: Session = Depends(get_db)):
    new_app = ApplicationModel(**app_data.dict())
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app

@app.get("/applications")
def get_applications(db: Session = Depends(get_db)):
    return db.query(ApplicationModel).all()

@app.get("/applications/{id}")
def get_application(id: int, db: Session = Depends(get_db)):
    application = db.query(ApplicationModel).filter(ApplicationModel.id == id).first()
    if not application:
        return {"error": "Application not found"}
    return application

@app.put("/applications/{id}")
def update_status(id: int, status: str, db: Session = Depends(get_db)):
    application = db.query(ApplicationModel).filter(ApplicationModel.id == id).first()
    if not application:
        return {"error": "Application not found"}
    application.status = status
    db.commit()
    db.refresh(application)
    return application

@app.delete("/applications/{id}")
def delete_application(id: int, db: Session = Depends(get_db)):
    application = db.query(ApplicationModel).filter(ApplicationModel.id == id).first()
    if not application:
        return {"error": "Application not found"}
    db.delete(application)
    db.commit()
    return {"message": f"Application {id} deleted"}