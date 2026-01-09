# app/main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import crud, models, database
from app.models import NoteResponse, CreateNoteResponse, UpdateNoteResponse
from app.database import SessionLocal, engine

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new note
@app.post("/notes/", response_model=NoteResponse)
def create_note(note: CreateNoteResponse, db: Session = Depends(get_db)):
    db_note = crud.create_note(db=db, title=note.title, content=note.content)
    return db_note

# Get all notes
@app.get("/notes/", response_model=list[NoteResponse])
def get_notes(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    notes = crud.get_notes(db=db, skip=skip, limit=limit)
    return notes

# Get a specific note by ID
@app.get("/notes/{note_id}", response_model=NoteResponse)
def get_note(note_id: int, db: Session = Depends(get_db)):
    db_note = crud.get_note_by_id(db=db, note_id=note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

# Update a specific note
@app.put("/notes/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, note: UpdateNoteResponse, db: Session = Depends(get_db)):
    db_note = crud.update_note(db=db, note_id=note_id, title=note.title, content=note.content)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

# Delete a note
@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    db_note = crud.delete_note(db=db, note_id=note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted"}
