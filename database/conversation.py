from database.db import SessionLocal
from database.models import Conversation


def save_message(role, message):
    db = SessionLocal()

    try:
        chat = Conversation(
            role=role,
            message=message
        )

        db.add(chat)
        db.commit()

    finally:
        db.close()


def get_recent_messages(limit=20):
    db = SessionLocal()

    try:
        chats = (
            db.query(Conversation)
            .order_by(Conversation.id.desc())
            .limit(limit)
            .all()
        )

        chats.reverse()

        return chats

    finally:
        db.close()