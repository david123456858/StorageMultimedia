from src.users.caseuse.login import caseUseUserLogin
from src.users.caseuse.register import caseUseCreateUser
from src.users.dtos.user import userDtoRegiter, userDtoLogin

from fastapi.responses import JSONResponse

class controllerUserAuth():
    
    def __init__(self,caseUseLogin:caseUseUserLogin, caseUseRegister:caseUseCreateUser) -> None:
        self.caseUse = caseUseLogin
        self.caseUseRegister = caseUseRegister
        pass
    
    def createUser(self,user:userDtoRegiter):
        response = self.caseUseRegister.createUser(user) # type: ignore
        
        if not response['success']:
            return JSONResponse({"error":response['error']},response['statusCode'])
        
        return JSONResponse({"message":response['value']},response['statusCode']) 
    
    def LoginUser(self,user:userDtoLogin,):
        result = self.caseUse.createLogin(user) # type: ignore
        if not result['success']:
            return JSONResponse({"error":result['error']},result['statusCode'])
        
        return JSONResponse({"message":result['value']},result['statusCode'])