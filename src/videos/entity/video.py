from src.config.db.db import Base
from sqlalchemy import Column, Integer, String

class Video(Base):
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    tag = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)
    format = Column(String, nullable=False)
