from src.videos.entity.video import Video
from src.config.db.db import dataBaseTurso

class RepositoryVideo:
    def __init__(self):
        self.session = dataBaseTurso._sessionLocal()

    def save(self, entity: Video):
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        self.session.close()
        return entity

    def update(self, entity: Video):
        self.session.merge(entity)
        self.session.commit()
        self.session.refresh(entity)
        self.session.close()
        return entity

    def findAll(self) -> list[Video]:
        result = self.session.query(Video).all()
        self.session.close()
        return result

    def findById(self, id: int) -> Video | None:
        result = self.session.query(Video).filter(Video.id == id).first()
        self.session.close()
        return result

    def delete(self, id: int):
        entity = self.session.query(Video).filter(Video.id == id).first()
        if entity:
            self.session.delete(entity)
            self.session.commit()
        self.session.close()
        return entity
