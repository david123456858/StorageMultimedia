from src.config.db.db import Base
from sqlalchemy import Column, Integer, String

class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    tag = Column (String, nullable=False) 
    url = Column(String, nullable=False)
