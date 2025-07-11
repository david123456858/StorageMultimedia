from fastapi import APIRouter

route =  APIRouter(prefix='/user',tags=['users'])


## funcion que carga todas las rutas
def moduleRouterUser () -> APIRouter:
    
    @route.get('/')
    def getUser():
        return {'message':'esta listo la ruta de user' }
    
    
    @route.get('/auth')
    def getAuth():
        return{'message':' ruta de autenticación'}
    return route