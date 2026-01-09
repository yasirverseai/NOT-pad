# app/models.py
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base
from datetime import datetime

# SQLAlchemy model for the database
class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Pydantic model for the response
class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # This tells Pydantic to treat the SQLAlchemy model as a dictionary

# Pydantic model for the create note response
class CreateNoteResponse(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True

# Pydantic model for the update note response
class UpdateNoteResponse(BaseModel):
    title: str
    content: str

    class Config:
        orm_mode = True