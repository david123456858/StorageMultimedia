from src.infrestructure.cloudinary.cloudinary_adapter import CloudinaryAdapter
from src.feacture.users.repository.user import repositoryUser
from src.feacture.multimedia.repository.multimedia import RepositoryMultimedia
from src.shared.utils.result import SuccessProccess, FailureProccess
from src.shared.utils.encrypt.hashed import hashing_hashlib
from src.shared.utils.cloudinary.getMultimedia import get_cloudinary_multimedia

##
# Modulo a revisar porque no estoy convencido de hacer esto asi
# 
class caseUseFindsByTags:
    """
    Caso de uso para el uso correctamente de las get por etiquetas
    """
    def __init__(self,repository:RepositoryMultimedia) -> None:
        self.repo = repository
        self.repo_user = repositoryUser()
        self.cloudinaryAdapter = CloudinaryAdapter()
    
    
    
    def find_by_tag_favorite(self,email_client:str):
        try:
            find_user = self.repo_user.find_by_email(hashing_hashlib(email_client))
            if not find_user:
                return FailureProccess(404, 'User Not Found')
            
            find_by_tag = self.repo.find_by_tag_favorite(hashing_hashlib(email_client))
            
            multimedia = self.cloudinaryAdapter.get_cloudinary_multimedia(find_by_tag)
            
            return SuccessProccess(200,multimedia)
        except Exception as e:
            print(e)
            return FailureProccess(500,'Error internal server') 
    
    
    
    def find_by_tag_archived(self,email_client:str):
        try:
            find_user = self.repo_user.find_by_email(hashing_hashlib(email_client))
            if not find_user:
                return FailureProccess(404, 'User Not Found')
            
            find_by_tag = self.repo.find_by_tag_archived(hashing_hashlib(email_client))
            
            multimedia = self.cloudinaryAdapter.get_cloudinary_multimedia(find_by_tag)
            
            return SuccessProccess(200,multimedia)
        except Exception as e:
            return FailureProccess(500,'Error internal server') 
    
    
    
    def find_by_tag_deleted(self,email_client:str):
        try:
            find_user = self.repo_user.find_by_email(hashing_hashlib(email_client))
            if not find_user:
                return FailureProccess(404, 'User Not Found')
            
            find_by_tag = self.repo.find_by_tag_deleted(hashing_hashlib(email_client))
            
            multimedia = self.cloudinaryAdapter.get_cloudinary_multimedia(find_by_tag)
            
            return SuccessProccess(200,multimedia)
        except Exception as e:
            return FailureProccess(500,'Error internal server') 
    
    
    
    def find_by_tag_private(self,email_client:str):
        try:
            find_user = self.repo_user.find_by_email(hashing_hashlib(email_client))
            if not find_user:
                return FailureProccess(404, 'User Not Found')
            
            find_by_tag = self.repo.find_by_tag_private(hashing_hashlib(email_client))
            
            multimedia = self.cloudinaryAdapter.get_cloudinary_multimedia(find_by_tag)
            
            return SuccessProccess(200,multimedia)
        except Exception as e:
            return FailureProccess(500,'Error internal server') 