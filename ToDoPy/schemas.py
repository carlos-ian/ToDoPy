from pydantic import BaseModel, EmailStr

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