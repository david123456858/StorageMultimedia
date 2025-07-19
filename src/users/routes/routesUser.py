from fastapi import APIRouter

from src.users.controllers.user import controllerUserAuth
from src.users.caseuse.register import caseUseCreateUser
from src.users.caseuse.login import caseUseUserLogin
from src.users.dtos.user import userDtoLogin,userDtoRegiter


route =  APIRouter(prefix='/user',tags=['users'])


#*
# this module is the begin in the aplication for part 
# *#
def moduleRouterUser () -> APIRouter:
    
    ## injection depends
    caseUseCreateInstance = caseUseCreateUser()
    caseUseLoginInstance = caseUseUserLogin()
    
    controller = controllerUserAuth(caseUseLoginInstance, caseUseCreateInstance)
    
    
    @route.post('/auth/register')
    def routeAuthLogin(userCreate:userDtoRegiter):
        return controllerUserAuth.createUser(controller)
    
    
    @route.post('/auth/login')
    def routeAuthRegister(userLogin:userDtoLogin):
        return{'message':f'user Recibido {userLogin}'}
    
    return route 