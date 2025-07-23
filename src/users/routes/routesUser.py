from fastapi import APIRouter

from src.users.controllers.user import controllerUserAuth
from src.users.caseuse.register import caseUseCreateUser
from src.users.caseuse.login import caseUseUserLogin
from src.users.dtos.user import userDtoLogin,userDtoRegiter
from src.users.repository.user import repositoryUser as RepositoryUser

route =  APIRouter(prefix='/user',tags=['users'])


#*
# this module is the begin in the aplication for part 
# *#
def moduleRouterUser () -> APIRouter:
    
    repository_user_instance = RepositoryUser() 
    ## injection depends
    caseUseCreateInstance = caseUseCreateUser(repository_user_instance)
    caseUseLoginInstance = caseUseUserLogin()
    
    controller = controllerUserAuth(caseUseLoginInstance, caseUseCreateInstance)
    
    
    @route.post('/auth/register')
    def routeAuthLogin(userCreate:userDtoRegiter):
        return controllerUserAuth.createUser(controller,userCreate,caseUseCreateInstance)
    
    
    @route.post('/auth/login')
    def routeAuthRegister(userLogin:userDtoLogin):
        return{'message':f'user Recibido {userLogin}'}
    
    return route 