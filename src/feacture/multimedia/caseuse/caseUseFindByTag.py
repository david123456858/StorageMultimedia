from src.feacture.users.repository.user import repositoryUser
from src.feacture.multimedia.repository.multimedia import RepositoryMultimedia
from src.shared.utils.result import SuccessProccess, FailureProccess
from src.shared.utils.encrypt.hashed import hashing_hashlib

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
    
    def find_by_tag_favorite(self,email_client:str):
        try:
            find_user = self.repo_user.find_by_email(hashing_hashlib(email_client))
            if not find_user:
                return FailureProccess(404, 'User Not Found')
            
            find_by_tag = self.repo.find_by_tag_favorite(find_user)
            return SuccessProccess(200,find_by_tag)
        except Exception as e:
            return FailureProccess(500,'Error internal server') 
    
    def find_by_tag_archived(self,email_client:str):
        try:
            find_user = self.repo_user.find_by_email(hashing_hashlib(email_client))
            if not find_user:
                return FailureProccess(404, 'User Not Found')
            
            find_by_tag = self.repo.find_by_tag_archived(find_user)
            return SuccessProccess(200,find_by_tag)
        except Exception as e:
            return FailureProccess(500,'Error internal server') 
    
    def find_by_tag_deleted(self,email_client:str):
        try:
            find_user = self.repo_user.find_by_email(hashing_hashlib(email_client))
            if not find_user:
                return FailureProccess(404, 'User Not Found')
            
            find_by_tag = self.repo.find_by_tag_deleted(find_user)
            return SuccessProccess(200,find_by_tag)
        except Exception as e:
            return FailureProccess(500,'Error internal server') 
    
    def find_by_tag_private(self,email_client:str):
        try:
            find_user = self.repo_user.find_by_email(hashing_hashlib(email_client))
            if not find_user:
                return FailureProccess(404, 'User Not Found')
            
            find_by_tag = self.repo.find_by_tag_private(find_user)
            return SuccessProccess(200,find_by_tag)
        except Exception as e:
            return FailureProccess(500,'Error internal server') 