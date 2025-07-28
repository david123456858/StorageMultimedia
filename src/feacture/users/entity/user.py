from src.config.db.db import Base

from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(100),unique=True)
    emailhash = Column(String(100),unique=True, index=True)
    password = Column(String(100))