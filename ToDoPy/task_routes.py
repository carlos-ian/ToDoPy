from fastapi import APIRouter
from fastapi import Depends, status
from sqlalchemy.orm import Session
import database, schemas, models
from security import get_current_user

task_router = APIRouter(prefix="/tasks", tags=["tasks"])

@task_router.post("/create", response_model=schemas.TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: schemas.TaskCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    new_task = models.Task(
        title=task.title,           
        date=task.date,             
        status=task.status,         
        category=task.category,
        importance=task.importance,
        owner_id=current_user.id   
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@task_router.get("/get", response_model=list[schemas.TaskResponse])
def read_task(db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.Task).filter(models.Task.owner_id == current_user.id).all()
