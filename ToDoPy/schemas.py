from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import datetime

class UserCreate(BaseModel):
    user_name: str 
    email: EmailStr
    password: str 

class UserResponse(BaseModel):
    id: int
    user_name: str
    email: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    acess_token: str
    token_type: str

class TaskStatus(str, Enum):
    TODO = "To Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"

class TaskImportance(str, Enum):
    BAIXA = "Baixa"
    RAZOAVEL = "Razoável"
    IMPORTANTE = "Importante"

class TaskCreate(BaseModel):
    title: str
    status: TaskStatus | None = "To Do"
    date: datetime 
    category: str
    importance: TaskImportance

class TaskResponse(TaskCreate):
    id: int
    owner_id: int
    title: str
    status: TaskStatus | None = "To Do"
    date: datetime 
    category: str
    importance: TaskImportance