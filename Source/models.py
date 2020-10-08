from sqlalchemy import Column, String

from .database import Base


class job_details(Base):
    __tablename__ = "jobs"

    job_id = Column(String)
    job_name = Column(String)
    job_description = Column(String)





