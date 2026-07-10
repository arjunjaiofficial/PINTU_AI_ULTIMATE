from database.db import SessionLocal
from database.models import UserMemory


def remember(key, value):
    db = SessionLocal()

    try:
        key = str(key).strip().lower()
        value = str(value).strip()

        item = db.query(UserMemory).filter(
            UserMemory.key == key
        ).first()

        if item:
            item.value = value
        else:
            item = UserMemory(
                key=key,
                value=value
            )
            db.add(item)

        db.commit()

    finally:
        db.close()


def recall(key):
    db = SessionLocal()

    try:
        key = str(key).strip().lower()

        item = db.query(UserMemory).filter(
            UserMemory.key == key
        ).first()

        if item:
            return item.value

        return None

    finally:
        db.close()


def delete_memory(key):
    db = SessionLocal()

    try:
        key = str(key).strip().lower()

        item = db.query(UserMemory).filter(
            UserMemory.key == key
        ).first()

        if item:
            db.delete(item)
            db.commit()

    finally:
        db.close()