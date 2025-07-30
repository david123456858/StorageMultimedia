from datetime import datetime
from sqlalchemy import Column, Integer, String,Boolean,DateTime,ForeignKey
from sqlalchemy.orm import relationship

from src.config.db.db import Base


class Multimedia(Base):
    __tablename__ = 'multimedia'
    id = Column(Integer, primary_key=True,index=True, autoincrement=True)
    public_id = Column(String(255),unique=True)
    resource_type = Column(String(20))    
    
    is_favorite = Column(Boolean, default=False)
    is_archived = Column(Boolean, default=False)
    is_private = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)  
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    
    user_id =   Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="multimedia")
