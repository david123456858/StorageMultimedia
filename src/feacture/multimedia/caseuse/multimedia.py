from src.feacture.multimedia.repository.multimedia import RepositoryMultimedia
from src.feacture.multimedia.dtos.multimedia import  MultimediaDtoUpdate
from src.feacture.multimedia.entity.multimedia import Multimedia
from src.shared.utils.result import SuccessProccess, FailureProccess
from src.feacture.users.repository.user import repositoryUser
from src.shared.utils.encrypt.hashed import hashing_hashlib

import cloudinary.uploader as cloudy
from fastapi import UploadFile

class CaseUseMultimedia:
    def __init__(self, repository: RepositoryMultimedia):
        self.repo = repository
        self.repoUser = repositoryUser()

    async def create_multimedia(self, email_client:str ,file:UploadFile):
        try:
            
            user_find = self.repoUser.find_by_email(hashing_hashlib(email_client)) 
            if not user_find:
                return FailureProccess(404, 'User Not Found')
            
            file_byte = await file.read()
            
            result = cloudy.upload(file_byte,resource_type="auto")
            print(result) 
            multimedia = Multimedia (
                public_id = result['public_id'],
                resource_type =  result['resource_type'],
                user_email = user_find.emailhash
            )
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
