from src.feacture.multimedia.entity.multimedia import Multimedia
from src.config.db.db import dataBaseTurso

class RepositoryMultimedia:
    def __init__(self):
        self.session = dataBaseTurso._sessionLocal()

    def save(self, entity: Multimedia):
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        self.session.close()

    def update(self, entity: Multimedia):
        return None

    def findAll(self):
        return self.session.query(Multimedia).all()

    def findById(self, id: int):
        return self.session.query(Multimedia).filter(Multimedia.id == id).first()

    def delete(self, public_id: str):
        multimedia_find = self.session.query(Multimedia).filter(Multimedia.public_id == public_id)
        self.session.delete(multimedia_find)
