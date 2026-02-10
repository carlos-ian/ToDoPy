from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, database, models
from security import get_password_hash

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    user_exists = db.query(models.User).filter(models.User.email == user.email).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Este email já está cadastrado")
    
    hashed_password = get_password_hash(user.password)

    new_user = models.User (
        user_name = user.user_name,
        email = user.email,
        hashed_password = hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@auth_router.get("/test-list")
def list_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return {"total_no_banco": len(users), "usuarios": users}