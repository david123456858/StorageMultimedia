from src.users.caseuse.login import caseUseUserLogin
from src.users.caseuse.register import caseUseCreateUser
from src.users.dtos.user import userDtoRegiter, userDtoLogin

class controllerUserAuth():
    
    def __init__(self,caseUseLogin:caseUseUserLogin, caseUseRegister:caseUseCreateUser) -> None:
        self.caseUse = caseUseLogin
        self.caseUseRegister = caseUseCreateUser
        pass
    
    async def createUser(self,user:userDtoRegiter,caseUse:caseUseCreateUser):
        return await caseUseCreateUser.createUser(caseUse,user)
    
    async def LoginUser(self):
        result = caseUseUserLogin.createLogin(self.caseUse,"deberia ir dto")
        return {}