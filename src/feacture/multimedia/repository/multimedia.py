from src.feacture.multimedia.entity.multimedia import Multimedia

class RepositoryMultimedia:
    def __init__(self):
        self.data = []  # Simulación de almacenamiento

    def save(self, entity: Multimedia):
        self.data.append(entity)
        return entity

    def update(self, entity: Multimedia):
        for idx, item in enumerate(self.data):
            if item.id == entity.id:
                self.data[idx] = entity
                return entity
        return None

    def findAll(self):
        return self.data

    def findById(self, id: int):
        for item in self.data:
            if item.id == id:
                return item
        return None

    def delete(self, id: int):
        self.data = [item for item in self.data if item.id != id]
