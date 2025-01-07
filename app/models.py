from sqlalchemy import Column, Integer, String, Text, Date, Enum, TIMESTAMP, func
from sqlalchemy.orm import relationship
from app.database import Base
import enum

# Model for database

# Enum for Task Status
class TaskStatus(str, enum.Enum):
    pending = "Pending"
    completed = "Completed"

# Task Model
class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    due_date = Column(Date, nullable=True)
    status = Column(Enum(TaskStatus), default = TaskStatus.pending)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

