
# coding: utf-8

# In[1]:


#database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy

SQLALCHEMY_DATABASE_URL = "sqlite:///./jobs.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



# In[5]:


#modules.py
from sqlalchemy import Column, String

#from .database import Base


class job_details(Base):
    __tablename__ = "jobs1"

    job_id = Column(String, primary_key=True)
    job_name = Column(String)
    job_description = Column(String)


# In[17]:


#common.py

from typing import Optional
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request, Form
from pydantic import BaseModel

#from .database import SessionLocal, engine
from sqlalchemy.orm import Session

from sqlalchemy import *

metadata = MetaData()


app = FastAPI()

#models.Base.metadata.create_all(bind=engine)
metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")


@app.get("/")
def homepage(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

@app.get("/")
def homepage(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}

class jobs(BaseModel):
    title: str
    job_id: str
    job_description: str

@app.get("/jobs/{title, job_id, job_description}")
def display_job(title: str, job_id: str, job_description: str, q: Optional[str] = None):
    return {"title": title, "job_id": job_id, "job_description":job_description, "q": q}

@app.post("/jobs/{title, job_id, job_description}")
def post_job(title: str, job_id: str, job_description: str, q: Optional[str] = None):
    return {"title": title, "job_id": job_id, "job_description":job_description, "q": q}

@app.delete("/jobs/{title, job_id}")
def delete_job(title: str, job_id: str, q: Optional[str] = "job_description"):
    return {"Job deleted"}

