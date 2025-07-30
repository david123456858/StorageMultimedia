from src.feacture.multimedia.repository.multimedia import RepositoryMultimedia
from src.feacture.multimedia.dtos.multimedia import MultimediaDtoCreate, MultimediaDtoUpdate
from src.feacture.multimedia.entity.multimedia import Multimedia

class CaseUseMultimedia:
    def __init__(self, repository: RepositoryMultimedia):
        self.repo = repository

    def create_multimedia(self, dto: MultimediaDtoCreate):
        multimedia = Multimedia(id=len(self.repo.data)+1, name=dto.name, url=dto.url, type=dto.type)
        return self.repo.save(multimedia)

    def get_all_multimedia(self):
        return self.repo.findAll()

    def get_multimedia_by_id(self, id: int):
        return self.repo.findById(id)

    def update_multimedia(self, id: int, dto: MultimediaDtoUpdate):
        multimedia = self.repo.findById(id)
        if not multimedia:
            return None
        if dto.name is not None:
            multimedia.name = dto.name
        if dto.url is not None:
            multimedia.url = dto.url
        if dto.type is not None:
            multimedia.type = dto.type
        return self.repo.update(multimedia)

    def delete_multimedia(self, id: int):
        self.repo.delete(id)
        return True
