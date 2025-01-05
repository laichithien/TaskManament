from sqlalchemy import create_engine

DATABASE_URL = "postgresql://thien:332002@localhost/taskdb"

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        print("Database connection successful!")
except Exception as e:
    print(f"Failed to connect: {e}")