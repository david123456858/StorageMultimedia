
from fastapi import APIRouter
from src.images.controllers.image import ControllerImage
from src.images.caseuse.image import CaseUseImage
from src.images.repository.images import RepositoryImage
from src.images.dtos.image import ImageDtoCreate, ImageDtoUpdate

route = APIRouter(prefix='/images', tags=['Images'])

def routeImages() -> APIRouter:
    
    repository = RepositoryImage()
    case_use = CaseUseImage(repository)
    controller = ControllerImage(case_use)

    @route.post('/')
    def create_image(dto: ImageDtoCreate):
        return controller.create_image(dto)

    @route.get('/')
    def get_images():
        return controller.get_all_images()

    @route.get('/{id}')
    def get_image_by_id(id: int):
        return controller.get_image_by_id(id)

    @route.put('/{id}')
    def update_image(id: int, dto: ImageDtoUpdate):
        return controller.update_image(id, dto)

    @route.delete('/{id}')
    def delete_image(id: int):
        return controller.delete_image(id)

    return route
