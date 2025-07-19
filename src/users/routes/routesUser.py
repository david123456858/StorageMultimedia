from fastapi import APIRouter

from src.users.controllers.user import controllerUserAuth
from src.users.caseuse.register import caseUseCreateUser
from src.users.caseuse.login import caseUseUserLogin
route =  APIRouter(prefix='/user',tags=['users'])


## funcion que carga todas las rutas
def moduleRouterUser () -> APIRouter:
    
    ## injection depends
    caseUseCreateInstance = caseUseCreateUser()
    caseUseLoginInstance = caseUseUserLogin()
    
    controller = controllerUserAuth(caseUseLoginInstance, caseUseCreateInstance)
    
    
    @route.post('/auth/register')
    def getUser():
        return controllerUserAuth.createUser(controller)
    
    
    @route.get('/auth/login')
    def getAuth():
        return{'message':' ruta de autenticación'}
    return route 