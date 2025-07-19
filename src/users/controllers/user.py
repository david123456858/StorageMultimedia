from src.users.caseuse.login import caseUseUserLogin
from src.users.caseuse.register import caseUseCreateUser

class controllerUserAuth():
    
    def __init__(self,caseUseLogin:caseUseUserLogin, caseUseRegister:caseUseCreateUser) -> None:
        self.caseUse = caseUseLogin
        self.caseUseRegister = caseUseCreateUser
        pass
    
    async def createUser(self):
        ## Logica del cretae
        
        
        return {}
    
    async def LoginUser(self):
        result = caseUseUserLogin.createLogin(self.caseUse,"deberia ir dto")
        return {}