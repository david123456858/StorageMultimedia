from fastapi import APIRouter

route = APIRouter(prefix='/images',tags=['Images'])


def routeImages()-> APIRouter:
    
    @route.get('/')
    def get_images():
        return {'message':'esta listo la ruta de images' }
    
    return route
