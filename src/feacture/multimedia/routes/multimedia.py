from fastapi import APIRouter
from src.feacture.multimedia.controllers.multimedia import ControllerMultimedia
from src.feacture.multimedia.caseuse.multimedia import CaseUseMultimedia
from src.feacture.multimedia.repository.multimedia import RepositoryMultimedia
from src.feacture.multimedia.dtos.multimedia import MultimediaDtoCreate, MultimediaDtoUpdate

route = APIRouter(prefix='/multimedia', tags=['Multimedia'])

def routeMultimedia() -> APIRouter:
    repository = RepositoryMultimedia()
    case_use = CaseUseMultimedia(repository)
    controller = ControllerMultimedia(case_use)

    @route.post('/')
    def create_multimedia(dto: MultimediaDtoCreate):
        return controller.create_multimedia(dto)

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
    def delete_multimedia(id: int):
        return controller.delete_multimedia(id)

    return route
