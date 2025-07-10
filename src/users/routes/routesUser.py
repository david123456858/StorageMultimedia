from fastapi import APIRouter

route =  APIRouter(prefix='/user',tags=['users'])

def moduleRouterUser () -> APIRouter:
    
    @route.get('/')
    def getUser():
        return {'message':'esta listo la ruta de user' }
    
    return route