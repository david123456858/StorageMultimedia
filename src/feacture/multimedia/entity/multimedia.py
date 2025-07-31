from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String,Boolean,DateTime,ForeignKey
from sqlalchemy.orm import relationship

from src.config.db.db import Base


class Multimedia(Base):
    """
    Modelo para archivos multimedia subidos por los usuarios.
    """
    __tablename__ = 'multimedia'
    id = Column(Integer, primary_key=True,index=True, autoincrement=True)
    public_id = Column(String(255),unique=True,index=True)
    resource_type = Column(String(20))
    
    is_favorite = Column(Boolean, default=False)
    is_archived = Column(Boolean, default=False)
    is_private = Column(Boolean, default=False)
    is_deleted = Column(Boolean, default=False)  
    
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    user_email =   Column(String, ForeignKey('users.emailhash'),index=True)
    user = relationship("User", back_populates="multimedia")
