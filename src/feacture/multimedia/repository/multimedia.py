from src.feacture.multimedia.entity.multimedia import Multimedia
from src.config.db.db import dataBaseTurso

from datetime import timezone,datetime

class RepositoryMultimedia:
    def __init__(self):
        self.session = dataBaseTurso._sessionLocal()

    def save(self, entity: Multimedia):
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        self.session.close()

    def update(self, entity: Multimedia):
        self.session.commit()
        result = self.session.refresh(entity)
        return result

    def findAll(self):
        return self.session.query(Multimedia).filter(
                Multimedia.is_archived==False,
                Multimedia.is_deleted==False,
                Multimedia.is_private==False
            ).all()
        
    def find_paginated(self,email_client:str,page:int,size_page:int):
        return self.session.query(Multimedia)\
            .filter(
                Multimedia.user_email == email_client,
                Multimedia.is_archived == False,
                Multimedia.is_deleted == False,
                Multimedia.is_private == False
            )\
            .order_by(Multimedia.created_at.desc())\
            .offset((page - 1) * size_page)\
            .limit(size_page)\
            .all()
        
    def findById(self, id: int):
        return self.session.query(Multimedia).filter(Multimedia.id == id).first()
    
    def find_by_public_id(self,public_id:str):
        return self.session.query(Multimedia).filter(Multimedia.public_id == public_id).first()
    
    def delete(self, public_id: str):
        multimedia_find = self.session.query(Multimedia).filter(Multimedia.public_id == public_id).first()
        self.session.delete(multimedia_find)
        self.session.commit()
    
    def delete_all(self,public_id):
        self.session.query(Multimedia)\
            .filter(Multimedia.public_id.in_(public_id))\
            .delete(synchronize_session=False)
        self.session.commit()
        
    def find_by_tag_favorite(self,email_client:str):
        return self.session.query(Multimedia)\
            .filter(Multimedia.user_email == email_client,
                    Multimedia.is_favorite==True)\
            .order_by(Multimedia.updated_at)\
            .all()
    
    def find_by_tag_archived(self,email_client:str):
        return self.session.query(Multimedia)\
            .filter(Multimedia.user_email == email_client,
                    Multimedia.is_archived==True)\
            .order_by(Multimedia.updated_at)\
            .all()
            
    def find_by_tag_private(self,email_client:str):
        return self.session.query(Multimedia)\
            .filter(Multimedia.user_email == email_client,
                    Multimedia.is_private==True)\
            .order_by(Multimedia.updated_at)\
            .all()

    def find_by_tag_deleted(self,email_client:str):
        return self.session.query(Multimedia)\
            .filter(Multimedia.user_email == email_client,
                    Multimedia.is_deleted==True)\
            .order_by(Multimedia.updated_at)\
            .all()