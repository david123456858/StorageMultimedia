from fastapi import APIRouter
from fastapi import File,UploadFile
from pydantic import EmailStr

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
    async def create_multimedia(email_client:EmailStr, file:UploadFile = File(...)):
        return await controller.create_multimedia(email_client,file)

    @route.get('/')
    def get_multimedia(email_client:EmailStr,page:int,size_page):
        return controller.get_all_multimedia(email_client,page,size_page)

    @route.get('/{id}')
    def get_multimedia_by_id(id: int):
        return controller.get_multimedia_by_id(id)

    @route.patch('/{id}')
    def update_multimedia(id:EmailStr, dto: MultimediaDtoUpdate):
        return controller.update_multimedia(id, dto)

    @route.delete('/{id}')
    def delete_multimedia(id: str):
        return controller.delete_multimedia(id)

    return route
