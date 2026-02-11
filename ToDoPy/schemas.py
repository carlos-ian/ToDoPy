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

class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    acess_token: str
    token_type: str