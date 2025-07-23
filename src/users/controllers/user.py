from src.users.caseuse.login import caseUseUserLogin
from src.users.caseuse.register import caseUseCreateUser
from src.users.dtos.user import userDtoRegiter, userDtoLogin

from fastapi.responses import JSONResponse

class controllerUserAuth():
    
    def __init__(self,caseUseLogin:caseUseUserLogin, caseUseRegister:caseUseCreateUser) -> None:
        self.caseUse = caseUseLogin
        self.caseUseRegister = caseUseCreateUser
        pass
    
    def createUser(self,user:userDtoRegiter,caseUse:caseUseCreateUser):
        response = caseUseCreateUser.createUser(caseUse,user)
        
        if not response['success']:
            return JSONResponse({"error":response['error']},response['statusCode'])
        
        return JSONResponse({"message":response['value']},response['statusCode']) 
    
    def LoginUser(self):
        result = caseUseUserLogin.createLogin(self.caseUse,"deberia ir dto")
        return {}