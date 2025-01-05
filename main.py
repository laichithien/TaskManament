from fastapi import FastAPI
from app.database import engine, Base
from app.routers import tasks

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include task routes
app.include_router(tasks.router)