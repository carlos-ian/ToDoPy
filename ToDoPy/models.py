from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base 
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    todos = relationship("Task", back_populates="owner")

class Task(Base):
    __tablename__ = "Task"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    status = Column(String, default="To Do")
    category = Column(String, nullable=False)
    importance = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="todos")