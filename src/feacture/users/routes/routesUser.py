from fastapi import APIRouter

from src.feacture.users.controllers.user import controllerUserAuth
from src.feacture.users.caseuse.register import caseUseCreateUser
from src.feacture.users.caseuse.login import caseUseUserLogin
from src.feacture.users.dtos.user import userDtoLogin,userDtoRegiter
from src.feacture.users.repository.user import repositoryUser as RepositoryUser

route =  APIRouter(prefix='/user',tags=['users'])

# this module is the begin in the aplication for part 

def moduleRouterUser () -> APIRouter:
    
    repository_user_instance = RepositoryUser() 
    
    caseUseCreateInstance = caseUseCreateUser(repository_user_instance)
    caseUseLoginInstance = caseUseUserLogin(repository_user_instance)
    
    controller = controllerUserAuth(caseUseLoginInstance, caseUseCreateInstance)
    
    
    @route.post('/register')
    def routeAuthLogin(userCreate:userDtoRegiter):
        return controller.createUser(userCreate) # type: ignore
    
    
    @route.post('/login')
    def routeAuthRegister(userLogin:userDtoLogin):
        return controller.LoginUser(userLogin)  # type: ignore
    
    return route 