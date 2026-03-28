from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..dependencies import get_current_user, admin_required

router = APIRouter(prefix="/api/v1/tasks", tags=["Tasks"])


@router.post("/")
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    new_task = models.Task(**task.dict(), user_id=user["user_id"])
    db.add(new_task)
    db.commit()
    return {"message": "Task created"}


@router.get("/")
def get_tasks(db: Session = Depends(get_db), user=Depends(get_current_user)):
    if user["role"] == "admin":
        return db.query(models.Task).all()
    return db.query(models.Task).filter(models.Task.user_id == user["user_id"]).all()


@router.put("/{task_id}")
def update_task(task_id: int, task: schemas.TaskUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    if user["role"] != "admin" and db_task.user_id != user["user_id"]:
        raise HTTPException(status_code=403, detail="Not allowed")

    for key, value in task.dict(exclude_unset=True).items():
        setattr(db_task, key, value)

    db.commit()
    return {"message": "Task updated"}


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    if user["role"] != "admin" and db_task.user_id != user["user_id"]:
        raise HTTPException(status_code=403, detail="Not allowed")

    db.delete(db_task)
    db.commit()
    return {"message": "Task deleted"}