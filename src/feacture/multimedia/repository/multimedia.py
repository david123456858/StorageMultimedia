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

    def findById(self, id: int):
        return self.session.query(Multimedia).filter(Multimedia.id == id).first()
    
    def find_by_public_id(self,public_id:str):
        return self.session.query(Multimedia).filter(Multimedia.public_id == public_id).first()
    
    def delete(self, public_id: str):
        multimedia_find = self.session.query(Multimedia).filter(Multimedia.public_id == public_id)
        self.session.delete(multimedia_find)
