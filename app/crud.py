# app/crud.py
from sqlalchemy.orm import Session
from app import models

# Create a new note
def create_note(db: Session, title: str, content: str):
    db_note = models.Note(title=title, content=content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

# Get all notes
def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Note).offset(skip).limit(limit).all()

# Get a note by its ID
def get_note_by_id(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id).first()

# Update a note
def update_note(db: Session, note_id: int, title: str, content: str):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if db_note:
        db_note.title = title
        db_note.content = content
        db.commit()
        db.refresh(db_note)
    return db_note

# Delete a note
def delete_note(db: Session, note_id: int):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if db_note:
        db.delete(db_note)
        db.commit()
    return db_note
