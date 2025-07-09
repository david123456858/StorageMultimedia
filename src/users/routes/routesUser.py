from fastapi import APIRouter

route =  APIRouter(prefix='users',tags=['users'])

def moduleRouterUser () -> APIRouter:
    
    @route.get('/user')
    def getUser():
        return { }
    
    return route