from src.feacture.multimedia.repository.multimedia import RepositoryMultimedia
from src.feacture.multimedia.dtos.multimedia import MultimediaDtoCreate, MultimediaDtoUpdate
from src.feacture.multimedia.entity.multimedia import Multimedia
from src.shared.utils.result import SuccessProccess, FailureProccess

import cloudinary.uploader as cloudy

class CaseUseMultimedia:
    def __init__(self, repository: RepositoryMultimedia):
        self.repo = repository

    async def create_multimedia(self, file):
        try:
            file_byte = await file.read()
            result = cloudy.upload(
            file_byte,
            resource_type="auto"
            )
            print(result)
            multimedia = Multimedia (
                public_id = result['public_id'],
                resource_type =  result['resource_type']
            )
            print(multimedia)
            self.repo.save(multimedia)
            return SuccessProccess(200,'multimedia saved sussesfuly')
        except Exception as e:
            print(e)
            return FailureProccess(500,'Error internal server')

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

    def delete_multimedia(self, id: str):
        print('prueba de ruta')
        return True
