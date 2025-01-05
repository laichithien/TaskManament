from sqlalchemy.orm import Session
from app import models, schemas

# Create a new task
def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        status=task.status
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Get a task by ID 
def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id==task_id).first()

# Get all tasks with optional filters and pagination
def get_tasks(db: Session, skip: int = 0, limit: int = 10, status: str = None):
    query = db.query(models.Task)
    if status:
        query = query.filter(models.Task.status==status)
    return query.offset(skip).limit(limit).all()


# Update a task
def update_task(db: Session, task_id: int, task: schemas.TaskUpdate):
    db_task = db.query(models.Task).filter(models.Task.id==task_id).first()
    if db_task:
        for key, value in task.dict(exclude_unset=True).item():
            setattr(db_task, key, value)
        db.commit()
        db.refresh(db_task)
    return db_task

# Delete a task 
def delete_task(db: Session, task_id: int):
    db_task = db.query(models.Task).filter(models.Task.id==task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task
