from src.feacture.users.caseuse.login import caseUseUserLogin
from src.feacture.users.caseuse.register import caseUseCreateUser
from src.feacture.users.dtos.user import userDtoRegiter, userDtoLogin
from src.shared.utils.response.response_factory import ResponseFactory


class controllerUserAuth():
    
    def __init__(self,caseUseLogin:caseUseUserLogin, caseUseRegister:caseUseCreateUser) -> None:
        self.caseUse = caseUseLogin
        self.caseUseRegister = caseUseRegister
        pass
    ## AFTER DESIGN PATTERN 
    
    def createUser(self,user:userDtoRegiter):
        response = self.caseUseRegister.createUser(user)
        return ResponseFactory().create_process(response) ## with desing pattern factory for reponses http
    
    def LoginUser(self,user:userDtoLogin,):
        result = self.caseUse.createLogin(user) 
        return ResponseFactory().create_process(result)