import models
from typing import Optional
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from pydantic import BaseModel
from .database import SessionLocal, engine
from sqlalchemy.orm import Session



app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

@app.get("/")
def homepage(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

class jobs(BaseModel):
    title: str
    job_id: str
    job_description: str

@app.get("/jobs/{title, job_id, job_description}")
def display_job(title: str, job_id: str, job_description: str, q: Optional[str] = None):
    return {"title": title, "job_id": job_id, "job_description":job_description, "q": q}

@app.post("/jobs/{title, job_id, job_description}")
def create_job(title: str, job_id: str, job_description: str, q: Optional[str] = None):
    jobs.db.append(title.dict(), job_id.dict(), job_description.dict())
    return {"title": title, "job_id": job_id, "job_description":job_description, "q": q}

@app.delete("/jobs/{title, job_id}")
def delete_job(title: str, job_id: str, q: Optional[str] = "job_description"):
    return {"Job deleted"}
