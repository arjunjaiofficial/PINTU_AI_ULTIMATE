from database.db import SessionLocal
from database.models import Note


def add_note(text):
    db = SessionLocal()

    try:
        note = Note(content=text)
        db.add(note)
        db.commit()

    finally:
        db.close()


def get_notes():
    db = SessionLocal()

    try:
        return db.query(Note).order_by(Note.id).all()

    finally:
        db.close()