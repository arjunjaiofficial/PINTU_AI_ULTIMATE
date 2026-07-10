from database.db import Base, engine
from database.models import Knowledge

def init_database():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_database()
    print("✅ PINTU AI Database Created Successfully!")