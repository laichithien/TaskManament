from pydantic import BaseModel
from datetime import date
from typing import Optional
from app.models import TaskStatus

# Base Schema
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: TaskStatus

# Create Schema (Post Requests)
class TaskCreate(TaskBase):
    pass

# Update (Put Requests)
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: Optional[TaskStatus] = None

# Response (Returning data)
class TaskResponse(TaskBase):
    id: int

    class Config:
        from_attributes = True