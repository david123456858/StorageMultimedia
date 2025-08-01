from src.feacture.multimedia.repository.multimedia import RepositoryMultimedia
from src.feacture.multimedia.dtos.multimedia import  MultimediaDtoUpdate
from src.feacture.multimedia.entity.multimedia import Multimedia
from src.shared.utils.result import SuccessProccess, FailureProccess
from src.feacture.users.repository.user import repositoryUser
from src.shared.utils.encrypt.hashed import hashing_hashlib


from cloudinary.uploader import upload , destroy
from cloudinary.utils import cloudinary_url
from fastapi import UploadFile

class CaseUseMultimedia:
    """
    Caso de uso general del modulo multimedia
    """
    def __init__(self, repository: RepositoryMultimedia):
        self.repo = repository
        self.repoUser = repositoryUser()

    async def create_multimedia(self, email_client:str ,file:UploadFile):
        try:
            
            user_find = self.repoUser.find_by_email(hashing_hashlib(email_client)) 
            if not user_find:
                return FailureProccess(404, 'User Not Found')
            
            file_byte = await file.read()
            
            result = upload(file_byte,resource_type="auto")
            
            multimedia = Multimedia (
                public_id = result['public_id'],
                resource_type =  result['resource_type'],
                user_email = user_find.emailhash
            )
            self.repo.save(multimedia)
            return SuccessProccess(200,'multimedia saved sussesfuly')
        except Exception as e:
            return FailureProccess(500, f'Cloudinary error: {str(e)}')

    def get_all_multimedia(self,email_client:str,page:int,size_page:int):
        try:
            result = self.repo.find_paginated(hashing_hashlib(email_client), page ,size_page)
            
            data = []
            for value in result:
                url,_ = cloudinary_url(value.public_id, resource_type=value.resource_type)
                thumbail_url,_ = cloudinary_url(
                    value.public_id,
                    resource_type=value.resource_type,
                    transformation=[
                        {'width': 300, 'height': 300, 'crop': 'fill'},
                        {'quality': 'auto'},
                        {'format': 'auto'}
                    ]
                )
                
                data.append({
                    'id': value.id,
                    'public_id': value.public_id,
                    'resource_type': value.resource_type,
                    'created_at': value.created_at,
                    'url': url,
                    'thumbnail_url': thumbail_url
                })
                
            return SuccessProccess(200,data)
        except Exception as e : 
            return FailureProccess(500,'Error internal server') 

    def get_multimedia_by_id(self, id: int):
        return self.repo.findById(id)

    def update_multimedia(self, public_id:str, dto: MultimediaDtoUpdate):
        try:
            ## part of clodinary
            
            ## part of database
            multimedia = self.repo.find_by_public_id(public_id)
            for key , value in dto.model_dump(exclude_none=True).items():
                setattr(multimedia,key,value)
                
            self.repo.update(multimedia)    
            return SuccessProccess(200,'ok')
        except Exception as e:   
            return FailureProccess(500,'Error internal Server')

    def delete_multimedia(self, public_id: str):
        try:
            multimedia_find =  self.repo.find_by_public_id(public_id)
            if not multimedia_find :
                return FailureProccess(404,'resource of multimedia don´t find')
            
            detroy_image = destroy(public_id)
            
            self.repo.update(multimedia_find)
            return SuccessProccess(200,'')
        except Exception as e:
            return FailureProccess(500,'')
