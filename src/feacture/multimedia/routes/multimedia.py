from fastapi import APIRouter
from fastapi import File,UploadFile

from src.feacture.multimedia.controllers.multimedia import ControllerMultimedia
from src.feacture.multimedia.caseuse.multimedia import CaseUseMultimedia
from src.feacture.multimedia.repository.multimedia import RepositoryMultimedia
from src.feacture.multimedia.dtos.multimedia import MultimediaDtoUpdate

route = APIRouter(prefix='/multimedia', tags=['Multimedia'])

def routeMultimedia() -> APIRouter:
    repository = RepositoryMultimedia()
    case_use = CaseUseMultimedia(repository)
    controller = ControllerMultimedia(case_use)

    @route.post('/')
    async def create_multimedia(file:UploadFile = File(...)):
        return await controller.create_multimedia(file)

    @route.get('/')
    def get_multimedia():
        return controller.get_all_multimedia()

    @route.get('/{id}')
    def get_multimedia_by_id(id: int):
        return controller.get_multimedia_by_id(id)

    @route.put('/{id}')
    def update_multimedia(id: int, dto: MultimediaDtoUpdate):
        return controller.update_multimedia(id, dto)

    @route.delete('/{id}')
    def delete_multimedia(id: str):
        return controller.delete_multimedia(id)

    return route
