from database.db import SessionLocal
from database.models import Knowledge


def save_knowledge(topic, information):
    db = SessionLocal()

    try:
        item = db.query(Knowledge).filter(
            Knowledge.topic == topic.lower()
        ).first()

        if item:
            item.information = information
        else:
            db.add(
                Knowledge(
                    topic=topic.lower(),
                    information=information
                )
            )

        db.commit()

    finally:
        db.close()


def get_knowledge(topic):
    db = SessionLocal()

    try:
        item = db.query(Knowledge).filter(
            Knowledge.topic == topic.lower()
        ).first()

        if item:
            return item.information

        return None

    finally:
        db.close()