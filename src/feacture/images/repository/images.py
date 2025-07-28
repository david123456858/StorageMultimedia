from src.feacture.images.entity.image import Image
from src.config.db.db import dataBaseTurso

class RepositoryImage:
    def __init__(self):
        self.session = dataBaseTurso._sessionLocal()

    def save(self, entity: Image):
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        self.session.close()
        return entity

    def update(self, entity: Image):
        self.session.merge(entity)
        self.session.commit()
        self.session.refresh(entity)
        self.session.close()
        return entity

    def findAll(self) -> list[Image]:
        result = self.session.query(Image).all()
        self.session.close()
        return result

    def findById(self, id: int) -> Image | None:
        result = self.session.query(Image).filter(Image.id == id).first()
        self.session.close()
        return result

    def delete(self, id: int):
        entity = self.session.query(Image).filter(Image.id == id).first()
        if entity:
            self.session.delete(entity)
            self.session.commit()
        self.session.close()
        return entity
